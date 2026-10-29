init python:
    import base64
    import hashlib
    import io
    import json
    import os
    import re
    import subprocess
    import tempfile

    import story_data

    BODY = "#e4dfd4"
    DIALOGUE = "#8fd3e0"
    MARK = "#e8c547"
    MUTED = "#7d8594"
    PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
    SAVE_VERSION = 4
    MAX_SAVE_BYTES = 4 * 1024 * 1024

    scenes, clue_index, handout_index, outcomes = story_data.validate()

    sos_section = ""
    sos_title = ""
    sos_paragraphs = []
    sos_flat = ""
    sos_picture = []
    sos_choices = []
    sos_mode = "continue"
    sos_prompt = "Enter 继续"
    sos_selected = 0
    sos_total = 0
    sos_count = 0
    sos_revealed = True
    sos_result = None
    sos_body = ""
    sos_screen = "reading"
    sos_tone = "night"
    sos_state = None
    cleanup_armed = False
    animate_scene = True


    class SaveError(Exception):
        pass


    def boot_state():
        global sos_state, cleanup_armed, animate_scene
        sos_state = {
            "scene": story_data.START_SCENE,
            "outcome": None,
            "clues": set(),
            "handouts": set(),
            "flags": set(),
            "text": {},
        }
        cleanup_armed = False
        animate_scene = True


    def escape_text(text):
        return text.replace("{", "{{")


    def render_placeholders(text, values):
        def replace(match):
            key = match.group(1)
            if key not in values:
                raise RuntimeError("缺少剧情文本变量：" + key)
            return values[key]
        return PLACEHOLDER.sub(replace, text.strip())


    def paragraphs_from(text, values, color=None):
        rendered = render_placeholders(text, values)
        paragraphs = []
        for block in rendered.replace("\r\n", "\n").split("\n"):
            dialogue = block.startswith("“") or ("：“" in block)
            paragraphs.append({
                "text": block,
                "color": color or (DIALOGUE if dialogue else BODY),
            })
        return paragraphs


    def append_variants(paragraphs, variants):
        for extra in active_variants(variants):
            paragraphs.extend(paragraphs_from(extra, sos_state["text"]))
        return paragraphs


    def flags_match(variant, flags):
        return all(flag in flags for flag in variant["require"]) and not any(
            flag in flags for flag in variant["exclude"])


    def active_variants(variants):
        flags = sos_state["flags"]
        return [variant["text"] for variant in variants or [] if flags_match(variant, flags)]


    def flatten(paragraphs):
        parts = []
        for index, paragraph in enumerate(paragraphs):
            if index:
                parts.append("\n")
            parts.append(paragraph["text"])
        return "".join(parts)


    def tagged(paragraphs, count):
        left = count
        chunks = []
        for index, paragraph in enumerate(paragraphs):
            if index:
                if left <= 0:
                    break
                left -= 1
                chunks.append("\n")
            if left <= 0:
                break
            piece = paragraph["text"][:left]
            left -= len(piece)
            if piece:
                chunks.append("{color=%s}%s{/color}" % (paragraph["color"], escape_text(piece)))
        return "".join(chunks)


    def revealed_paragraphs():
        left = sos_count
        shown = []
        for index, paragraph in enumerate(sos_paragraphs):
            if index:
                if left <= 0:
                    break
                left -= 1
            if left <= 0:
                break
            piece = paragraph["text"][:left]
            left -= len(piece)
            if piece:
                shown.append({
                    "text": piece.replace("{", "{{"),
                    "color": paragraph["color"],
                    "kind": paragraph.get("kind", "body"),
                    "first": not shown,
                })
        return shown


    def snap_after_reveal():
        snap_viewport(sos_mode == "choose")


    def first_enabled(choices):
        for index, item in enumerate(choices):
            if item.get("id") and item.get("enabled", True):
                return index
        return 0


    def begin_page(section, title, paragraphs, picture, mode, prompt, animate, choices=None):
        global sos_section, sos_title, sos_paragraphs, sos_flat, sos_picture
        global sos_choices, sos_mode, sos_prompt, sos_selected, sos_total
        global sos_count, sos_revealed, sos_result, sos_body, sos_screen, sos_tone
        sos_section = section
        sos_title = title
        sos_screen = "reading"
        sos_tone = "night"
        sos_paragraphs = paragraphs
        sos_flat = flatten(paragraphs)
        sos_picture = picture or []
        sos_choices = choices or []
        sos_mode = mode
        sos_prompt = prompt
        sos_selected = first_enabled(sos_choices)
        sos_total = len(sos_flat)
        sos_revealed = (not animate) or sos_total == 0
        sos_count = sos_total if sos_revealed else 0
        sos_result = None
        sos_body = tagged(sos_paragraphs, sos_count)


    def snap_viewport(to_end):
        try:
            widget = renpy.get_widget("reading", "bodyvp")
            if widget is None:
                return
            adjustment = widget.yadjustment
            adjustment.value = adjustment.range if to_end else 0
        except Exception:
            return


    def sos_tick():
        global sos_count, sos_revealed, sos_body
        if sos_revealed:
            return
        count = sos_count
        if count >= sos_total:
            sos_revealed = True
            sos_body = tagged(sos_paragraphs, sos_total)
            snap_after_reveal()
            return
        count += 1
        while count < sos_total and sos_flat[count - 1].isspace():
            count += 1
        sos_count = count
        sos_body = tagged(sos_paragraphs, count)
        if count >= sos_total:
            sos_revealed = True
            snap_after_reveal()
        else:
            snap_viewport(True)


    def sos_reveal_all():
        global sos_count, sos_revealed, sos_body
        sos_count = sos_total
        sos_revealed = True
        sos_body = tagged(sos_paragraphs, sos_total)
        snap_after_reveal()


    def sos_move(delta):
        global sos_selected
        if not sos_choices:
            return
        index = sos_selected
        for _ in sos_choices:
            index = (index + delta) % len(sos_choices)
            item = sos_choices[index]
            if item.get("id") and item.get("enabled", True):
                sos_selected = index
                return


    def sos_hover(index):
        global sos_selected
        item = sos_choices[index]
        if item.get("id") and item.get("enabled", True):
            sos_selected = index


    def sos_confirm():
        global sos_result
        if not sos_revealed:
            sos_reveal_all()
            return
        if sos_mode == "continue":
            sos_result = "continue"
            return
        item = sos_choices[sos_selected]
        if not item.get("id") or not item.get("enabled", True):
            return
        sos_result = item["id"]


    def sos_pick(index):
        sos_hover(index)
        sos_confirm()


    def show_page():
        global sos_result
        sos_result = None
        return renpy.call_screen(sos_screen)


    def choice_available(choice):
        flags = sos_state["flags"]
        clues = sos_state["clues"]
        return all(clue_id in clues for clue_id in choice["require_clues"]) and all(
            flag in flags for flag in choice["require_flags"]) and not any(
            flag in flags for flag in choice["exclude_flags"])


    def scene_menu(scene):
        items = []
        for choice in scene["choices"]:
            if choice_available(choice):
                items.append({"id": choice["id"], "text": "·  " + choice["text"], "enabled": True})
        if not items:
            raise RuntimeError("场景 %s 没有可选项。" % scene["id"])
        items.append({"id": None, "text": "其他", "enabled": False, "label": True})
        items.append({"id": "0", "text": "·  重读已发现的线索与手稿", "enabled": True})
        items.append({"id": "Q", "text": "·  保存并退出", "enabled": True})
        return items


    def show_hook():
        begin_page("序章", "夏末的门", paragraphs_from(story_data.HOOK, sos_state["text"]),
                   [], "continue", "Enter 继续", True)


    def show_scene():
        scene = scenes[sos_state["scene"]]
        paragraphs = paragraphs_from(scene["text"], sos_state["text"])
        append_variants(paragraphs, scene["variants"])
        begin_page("剧情", scene["title"], paragraphs, scene["picture"], "choose", "",
                   animate_scene, scene_menu(scene))


    def show_journal():
        paragraphs = []
        for clue in story_data.CLUES:
            if clue["id"] not in sos_state["clues"]:
                continue
            paragraphs.append({"text": "线索 · " + clue["title"], "color": MARK, "kind": "heading"})
            paragraphs.extend(paragraphs_from(clue["text"], sos_state["text"]))
        for handout in story_data.HANDOUTS:
            if handout["id"] not in sos_state["handouts"]:
                continue
            paragraphs.append({"text": "手稿 · " + handout["title"], "color": MARK, "kind": "heading"})
            paragraphs.extend(paragraphs_from(handout["text"], sos_state["text"]))
            for extra in active_variants(handout["variants"]):
                paragraphs.extend(paragraphs_from(extra, sos_state["text"]))
        if not paragraphs:
            paragraphs = [{"text": "尚无可重读的材料。", "color": MUTED}]
        begin_page("档案", "已发现的材料", paragraphs, [], "continue", "Enter 继续", False)


    def show_ending():
        global sos_tone
        outcome = outcomes[sos_state["outcome"]]
        paragraphs = paragraphs_from(outcome["text"], sos_state["text"])
        append_variants(paragraphs, outcome["variants"])
        begin_page("结局", outcome["title"], paragraphs, [], "continue", "Enter 结束", True)
        sos_tone = outcome["id"]


    def apply_choice(choice_id):
        global cleanup_armed
        scene = scenes[sos_state["scene"]]
        choice = next(item for item in scene["choices"] if item["id"] == choice_id)
        if not choice_available(choice):
            raise RuntimeError("这个选项现在不能选。")
        if choice["outcome"] == "E01":
            if (sos_state["scene"] != "S15" or choice["id"] != "O15a"
                    or "P_RETURN_PENDING" not in sos_state["flags"]
                    or "K10" not in sos_state["clues"]):
                raise RuntimeError("送返结局缺少两次确认。")
            cleanup_armed = True
        sos_state["clues"].update(choice["clues"])
        sos_state["handouts"].update(choice["handouts"])
        sos_state["flags"].update(choice["flags"])
        if choice["set_text"] is not None:
            key, value = choice["set_text"]
            sos_state["text"][key] = value
        begin_page("行动", "我的选择", paragraphs_from(choice["feedback"], sos_state["text"]),
                   [], "continue", "Enter 继续", True)
        if choice["outcome"] is not None:
            sos_state["outcome"] = choice["outcome"]
            return "e01" if choice["outcome"] == "E01" else "ending"
        sos_state["scene"] = choice["next"]
        sos_state["outcome"] = None
        return "scene"


    def save_path():
        base = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
        folder = os.path.join(base, "SOS_Project")
        os.makedirs(folder, exist_ok=True)
        return os.path.join(folder, "save.json")


    def exported_state():
        return {
            "version": SAVE_VERSION,
            "scene": sos_state["scene"],
            "outcome": sos_state["outcome"],
            "clues": sorted(sos_state["clues"]),
            "handouts": sorted(sos_state["handouts"]),
            "flags": sorted(sos_state["flags"]),
            "text": dict(sos_state["text"]),
        }


    def texts_for(data):
        flags = set(data["flags"])
        found = [scenes[data["scene"]]["text"]]
        for variant in scenes[data["scene"]]["variants"]:
            if flags_match(variant, flags):
                found.append(variant["text"])
        for handout_id in data["handouts"]:
            handout = handout_index[handout_id]
            found.append(handout["text"])
            for variant in handout["variants"]:
                if flags_match(variant, flags):
                    found.append(variant["text"])
        if data["outcome"] is not None:
            outcome = outcomes[data["outcome"]]
            found.append(outcome["text"])
            for variant in outcome["variants"]:
                if flags_match(variant, flags):
                    found.append(variant["text"])
        return found


    def read_save():
        path = save_path()
        if not os.path.isfile(path):
            raise SaveError("没有存档。")
        if os.path.getsize(path) > MAX_SAVE_BYTES:
            raise SaveError("存档无法读取。新游戏会覆盖现有文件。")
        try:
            with io.open(path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, UnicodeError, json.JSONDecodeError):
            raise SaveError("存档无法读取。新游戏会覆盖现有文件。")
        if not isinstance(data, dict) or data.get("version") != SAVE_VERSION:
            raise SaveError("存档无法读取。新游戏会覆盖现有文件。")
        scene_id = data.get("scene")
        outcome_id = data.get("outcome")
        clue_ids = data.get("clues")
        handout_ids = data.get("handouts")
        flags = data.get("flags")
        text = data.get("text")
        if (scene_id not in scenes or not isinstance(clue_ids, list)
                or not isinstance(handout_ids, list) or not isinstance(flags, list)
                or not isinstance(text, dict)
                or (outcome_id is not None and outcome_id not in outcomes)
                or any(item not in clue_index for item in clue_ids)
                or any(item not in handout_index for item in handout_ids)
                or (scene_id == "S15" and "P_RETURN_PENDING" not in flags)
                or (scene_id == "S16" and "P_STAY_PENDING" not in flags)):
            raise SaveError("存档包含无法识别的剧情状态。")
        values = {str(key): value for key, value in text.items() if isinstance(value, str)}
        data = {
            "scene": scene_id,
            "outcome": outcome_id,
            "clues": clue_ids,
            "handouts": handout_ids,
            "flags": flags,
            "text": values,
        }
        for text_block in texts_for(data):
            for match in PLACEHOLDER.finditer(text_block):
                if match.group(1) not in values:
                    raise SaveError("存档缺少剧情文本变量。")
        return data


    def inspect_save():
        if not os.path.isfile(save_path()):
            return False, None
        try:
            read_save()
        except SaveError as error:
            return True, str(error)
        return True, None


    def save_game():
        payload = json.dumps(exported_state(), ensure_ascii=False).encode("utf-8")
        if len(payload) > MAX_SAVE_BYTES:
            raise SaveError("存档数据超过大小上限。")
        path = save_path()
        handle = tempfile.NamedTemporaryFile(dir=os.path.dirname(path), prefix=".save-", suffix=".tmp", delete=False)
        temp = handle.name
        try:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
            handle.close()
            os.replace(temp, path)
        except Exception:
            handle.close()
            if os.path.isfile(temp):
                os.remove(temp)
            raise


    def delete_save():
        path = save_path()
        if os.path.isfile(path):
            os.remove(path)


    def load_game():
        data = read_save()
        sos_state["scene"] = data["scene"]
        sos_state["outcome"] = data["outcome"]
        sos_state["clues"] = set(data["clues"])
        sos_state["handouts"] = set(data["handouts"])
        sos_state["flags"] = set(data["flags"])
        sos_state["text"] = dict(data["text"])


    def prepare_menu():
        global sos_screen
        exists, error = inspect_save()
        if error:
            note = error + " 新游戏会覆盖现有文件。"
        elif exists:
            note = "已发现存档。新游戏会覆盖现有进度。"
        else:
            note = "请选择旅程的起点。"
        paragraphs = [
            {"text": note, "color": BODY},
            {"text": "阅读时任意键可补完文字。", "color": MUTED},
        ]
        load_enabled = exists and error is None
        choices = [
            {"id": "1", "text": "·  新游戏", "enabled": True},
            {"id": "2", "text": "·  读存档" if load_enabled else "·  读存档  ·  暂不可用", "enabled": load_enabled},
            {"id": "3", "text": "·  退出", "enabled": True},
        ]
        begin_page("开始", story_data.TITLE, paragraphs, [], "choose", "", False, choices)
        sos_screen = "title_page"


    def schedule_exe_delete():
        if not renpy.windows:
            return
        exe = os.path.abspath(os.path.join(renpy.config.basedir, "SOS_Project.exe"))
        if (os.path.basename(exe).lower() != "sos_project.exe"
                or os.path.normcase(os.path.dirname(exe)) != os.path.normcase(os.path.abspath(renpy.config.basedir))
                or not os.path.isfile(exe)):
            return
        try:
            with io.open(exe, "rb") as handle:
                digest = hashlib.sha256(handle.read()).hexdigest().upper()
        except OSError:
            return
        powershell = os.path.join(os.environ.get("SystemRoot", r"C:\Windows"),
                                  "System32", "WindowsPowerShell", "v1.0", "powershell.exe")
        if not os.path.isfile(powershell):
            return
        command = (
            "$gameExe = '%s'; $expectedHash = '%s'; "
            "for ($attempt = 0; $attempt -lt 300; $attempt++) { "
            "if (-not [System.IO.File]::Exists($gameExe)) { break }; "
            "try { $stream = [System.IO.File]::OpenRead($gameExe); "
            "try { $hasher = [System.Security.Cryptography.SHA256]::Create(); "
            "try { $actualHash = [System.BitConverter]::ToString($hasher.ComputeHash($stream)).Replace('-', '') } "
            "finally { $hasher.Dispose() } } finally { $stream.Dispose() }; "
            "if ($actualHash -ne $expectedHash) { break }; "
            "[System.IO.File]::Delete($gameExe); "
            "if (-not [System.IO.File]::Exists($gameExe)) { break } "
            "} catch {} [System.Threading.Thread]::Sleep(200) }"
        ) % (exe.replace("'", "''"), digest)
        encoded = base64.b64encode(command.encode("utf-16le")).decode("ascii")
        try:
            subprocess.Popen(
                [powershell, "-NoProfile", "-NonInteractive", "-EncodedCommand", encoded],
                creationflags=0x08000000)
        except OSError:
            return


    def show_cleanup_result():
        global sos_tone
        delete_save()
        schedule_exe_delete()
        sos_tone = "E01"


    def play():
        global animate_scene
        boot_state()
        while True:
            prepare_menu()
            picked = show_page()
            if picked in (None, "3"):
                renpy.quit()
            if picked == "1":
                boot_state()
                show_hook()
                show_page()
                save_game()
                break
            if picked == "2":
                try:
                    load_game()
                except SaveError:
                    continue
                break
        if sos_state["outcome"] is not None:
            show_ending()
            show_page()
            renpy.quit()
        while True:
            show_scene()
            picked = show_page()
            if picked == "Q":
                save_game()
                renpy.quit()
            if picked == "0":
                show_journal()
                show_page()
                animate_scene = False
                continue
            kind = apply_choice(picked)
            show_page()
            if kind == "e01":
                show_ending()
                show_page()
                if cleanup_armed:
                    show_cleanup_result()
                renpy.quit()
            if kind == "ending":
                save_game()
                show_ending()
                show_page()
                renpy.quit()
            save_game()
            animate_scene = True


    boot_state()
