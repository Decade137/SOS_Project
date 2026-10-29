screen reading():
    add Solid(page_tone())
    viewport id "bodyvp":
        xfill True
        yfill True
        mousewheel True
        child_size (None, 32767)
        vbox:
            xfill True
            vbox:
                xsize COLUMN
                xalign 0.5
                null height 72
                hbox:
                    spacing 14
                    add Solid(ACCENT) xysize (28, 2) yalign 0.5
                    text sos_section style "sos_section" substitute False
                null height 16
                text sos_title style "sos_title" substitute False
                null height 40
                vbox:
                    spacing 22
                    for paragraph in revealed_paragraphs():
                        if paragraph["kind"] == "heading":
                            if not paragraph["first"]:
                                null height 18
                            text paragraph["text"] style "sos_heading" substitute False
                        else:
                            text paragraph["text"]:
                                style "sos_body"
                                color paragraph["color"]
                                substitute False
                if sos_revealed and sos_picture:
                    null height 36
                    frame:
                        style "sos_picture"
                        vbox:
                            spacing 4
                            for line in sos_picture:
                                hbox:
                                    spacing 4
                                    for cell in line["text"][::2]:
                                        if cell == "■":
                                            add Solid(line["color"]) xysize (14, 14)
                                        else:
                                            null width 14 height 14
                if sos_revealed and sos_mode == "choose":
                    null height 40
                    use choice_list(COLUMN)
                null height 36
                text (reading_hint()) style "sos_hint" substitute False
                null height 96
    vbar value YScrollValue("bodyvp") style "sos_scroll"
    use page_keys


screen title_page():
    add Solid(page_tone())
    vbox:
        xalign 0.5
        yalign 0.42
        hbox:
            xalign 0.5
            spacing 6
            for day in range(17, 32):
                add Solid(ACCENT if day == 31 else "#2a3040") xysize (14, 14)
        null height 12
        text "08 · 17  —  08 · 31" style "sos_title_meta" xalign 0.5
        null height 44
        text sos_title style "sos_title_big" xalign 0.5 substitute False
        null height 16
        text "暑假的最后一天" style "sos_title_meta" xalign 0.5
        null height 64
        hbox:
            xalign 0.5
            use choice_list(300)
        null height 36
        for paragraph in sos_paragraphs:
            text paragraph["text"]:
                style "sos_title_note"
                color paragraph["color"]
                xalign 0.5
                substitute False
    text "非官方同人作品    ·    W/S 选择    ·    Enter 确认" style "sos_hint" xalign 0.5 yalign 0.96
    use page_keys


screen choice_list(width):
    vbox:
        xsize width
        spacing 4
        for index, item in enumerate(sos_choices):
            if item.get("label"):
                null height 14
                hbox:
                    spacing 14
                    text item["text"] style "sos_choice_label" yalign 0.5 substitute False
                    add Solid(RULE) xysize (width - 60, 1) yalign 0.5
                null height 4
            else:
                textbutton item["text"]:
                    style "sos_choice"
                    background choice_background(index, item)
                    sensitive item.get("enabled", True)
                    action Function(sos_pick, index)
                    hovered Function(sos_hover, index)
                    text_color choice_color(index, item)
                    text_insensitive_color DISABLED


screen page_keys():
    if sos_result is not None:
        timer 0.01 action Return(sos_result)
    elif not sos_revealed:
        timer 0.02 repeat True action Function(sos_tick)
        key "dismiss" action Function(sos_reveal_all)
        key "mouseup_1" action Function(sos_reveal_all)
    else:
        key "K_w" action Function(sos_move, -1)
        key "K_UP" action Function(sos_move, -1)
        key "K_s" action Function(sos_move, 1)
        key "K_DOWN" action Function(sos_move, 1)
        key "K_RETURN" action Function(sos_confirm)
        key "K_KP_ENTER" action Function(sos_confirm)
        if sos_mode == "continue":
            key "K_SPACE" action Function(sos_confirm)
            key "mouseup_1" action Function(sos_confirm)


screen say(who, what):
    text what


screen choice(items):
    pass


screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#05070ad0")
    frame:
        style "sos_dialog"
        vbox:
            spacing 28
            text message style "sos_dialog_text" substitute False
            hbox:
                xalign 1.0
                spacing 12
                textbutton "取消" style "sos_dialog_button" action no_action
                textbutton "确定" style "sos_dialog_button" action yes_action


screen notify(message):
    zorder 100
    frame:
        style "sos_notify"
        text message style "sos_hint" color CHOICE substitute False
    timer 3.25 action Hide("notify")


style sos_section is text:
    font "fonts/NotoSansSC-Regular.ttf"
    size 16
    color "#7d8594"
    kerning 3

style sos_title is text:
    font "fonts/NotoSerifSC-Bold.ttf"
    size 38
    color "#f2ede2"
    kerning 1

style sos_body is text:
    font "fonts/NotoSerifSC-Regular.ttf"
    size 25
    line_spacing 18

style sos_heading is text:
    font "fonts/NotoSansSC-Regular.ttf"
    size 19
    color "#e8c547"
    kerning 2

style sos_hint is text:
    font "fonts/NotoSansSC-Regular.ttf"
    size 16
    color "#5b6270"
    kerning 1

style sos_picture is frame:
    background "#0b0d12"
    padding (32, 24)
    xalign 0.5

style sos_choice is button:
    background None
    padding (18, 8, 12, 8)
    xfill True

style sos_choice_text is text:
    font "fonts/NotoSansSC-Regular.ttf"
    size 23
    color "#c9c4b8"
    line_spacing 8
    text_align 0.0
    language "japanese-normal"

style sos_choice_label is text:
    font "fonts/NotoSansSC-Regular.ttf"
    size 15
    color "#5b6270"
    kerning 4

style sos_scroll is vbar:
    xalign 1.0
    xoffset -6
    xsize 4
    yfill True
    bar_vertical True
    bar_invert False
    base_bar Solid("#ffffff08")
    thumb Solid("#ffffff2a")
    unscrollable "hide"

style sos_title_big is text:
    font "fonts/NotoSerifSC-Bold.ttf"
    size 58
    color "#f2ede2"
    kerning 6

style sos_title_meta is text:
    font "fonts/NotoSansSC-Regular.ttf"
    size 16
    color "#7d8594"
    kerning 3

style sos_title_note is text:
    font "fonts/NotoSansSC-Regular.ttf"
    size 16
    kerning 1

style sos_dialog is frame:
    background "#1a1f2a"
    padding (40, 32)
    xsize 560
    xalign 0.5
    yalign 0.5

style sos_dialog_text is text:
    font "fonts/NotoSerifSC-Regular.ttf"
    size 22
    color "#f2ede2"
    line_spacing 10

style sos_dialog_button is button:
    background None
    hover_background "#e8c54722"
    padding (20, 8, 20, 8)

style sos_dialog_button_text is text:
    font "fonts/NotoSansSC-Regular.ttf"
    size 20
    color "#c9c4b8"
    hover_color "#8fd3e0"

style sos_notify is frame:
    background "#1a1f2ae6"
    padding (24, 12)
    xalign 0.5
    yalign 0.06


init python:
    COLUMN = 820
    ACCENT = "#e8c547"
    SELECT = "#8fd3e0"
    CHOICE = "#c9c4b8"
    DISABLED = "#4b5260"
    RULE = "#262c38"
    PAGE_TONES = {
        "night": "#12151c",
        "E01": "#0d1521",
        "E02": "#1b1610",
        "E03": "#17121f",
    }
    CHOICE_MARK = Fixed(Solid("#e8c54712"), Solid(ACCENT, xmaximum=3))

    def page_tone():
        return PAGE_TONES.get(sos_tone, PAGE_TONES["night"])

    def choice_background(index, item):
        if index == sos_selected and item.get("enabled", True):
            return CHOICE_MARK
        return None

    def choice_color(index, item):
        if not item.get("enabled", True):
            return DISABLED
        if index == sos_selected:
            return SELECT
        return CHOICE

    def reading_hint():
        if not sos_revealed:
            return "任意键补完文字"
        if sos_mode == "choose":
            return "W/S 或 ↑↓ 选择   ·   Enter 确认   ·   也可点击"
        return sos_prompt

    style.default.font = "fonts/NotoSansSC-Regular.ttf"
    style.default.size = 26
    style.default.color = "#e4dfd4"
    style.default.language = "japanese-normal"
