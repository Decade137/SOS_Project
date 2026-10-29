"""Player-facing scenario 0 data. Derived from Scenarios/00-zero-floor.md.

Keeper notes stay in the Markdown module and are not loaded here.
Long scene text lives in story_prose.py and story_long.py.
"""

import story_long as longer
import story_more2 as more
import story_more3 as more3
import story_prose as prose

TITLE = "凉宫春日的心愿"
START_SCENE = "S00"

HOOK = prose.HOOK.strip()

YELLOW = "#f0d040"
DARK_YELLOW = "#b8860b"
DARK_RED = "#8b2e2e"
DARK_GRAY = "#6e6e6e"
RED = "#d24a4a"
DARK_CYAN = "#1f8f8f"


def _variant(text, require=(), exclude=()):
    return {"text": text.strip(), "require": list(require), "exclude": list(exclude)}


def _choice(choice_id, text, feedback, next_scene=None, outcome=None, clues=(),
            handouts=(), flags=(), require_clues=(), require_flags=(),
            exclude_flags=(), exclude=(), set_text=None):
    exclude_flags = list(exclude_flags) + list(exclude)
    if (next_scene is None) == (outcome is None):
        raise RuntimeError(f"选项 {choice_id} 必须指向场景或结局之一。")
    return {
        "id": choice_id,
        "text": text,
        "feedback": feedback.strip(),
        "next": next_scene,
        "outcome": outcome,
        "clues": list(clues),
        "handouts": list(handouts),
        "flags": list(flags),
        "require_clues": list(require_clues),
        "require_flags": list(require_flags),
        "exclude_flags": list(exclude_flags),
        "set_text": set_text,
    }


def _scene(scene_id, title, text, choices, picture=None, variants=()):
    return {
        "id": scene_id,
        "title": title,
        "text": text.strip(),
        "choices": choices,
        "picture": picture,
        "variants": list(variants),
    }


def _picture(*rows):
    return [{"color": color, "text": text} for color, text in rows]


def _t(*parts):
    return "\n\n".join(part.strip() for part in parts if part and part.strip())


CLUES = [
    {"id": "K01", "title": "没有第六人的八月", "text": "这个八月已经重复了一万五千多次。长门记得每一次。那些八月里都没有第六个人。这一次从八月二十日起出现偏差，原因未确定。我在八月三十一日下午三点十七分出现。"},
    {"id": "K02", "title": "我身上的两样东西", "text": "我身上只有一部没有信号的手机和一张车票。车票印着一座他们没听说过的城市，日期是 2026 年 8 月 31 日。春日看见它们时，像对上了什么，又把话咽了回去。"},
    {"id": "K03", "title": "不是那边的人", "text": "长门借替我翻字典碰过我的手腕。我没有接入思念体的线路，不是那边的终端。能追溯到的最早记录，是今天十五点十七分，活动室铁皮柜的门口。十五点十六分，那扇门还是一只普通的铁皮柜。更早的部分没有。"},
    {"id": "K04", "title": "不是从任何时候来的", "text": "朝比奈的装置没有找到时间移动的痕迹。我不是从过去或未来来的。我的时间像是从今天下午三点十七分才开始。秒针倒走过一次，倒走的时候人没有被搬走。"},
    {"id": "K05", "title": "三点十七分的闭锁空间", "text": "我不是超能力者。今天十五点十七分，活动室里出现过一个不到一秒的闭锁空间，里面没有神人。它不像不满，更像一声满足的叹气。"},
    {"id": "K06", "title": "八月二十日的那一页", "text": "春日的笔记本里，八月二十日那一页写着异世界人应该带着的东西：会发光的薄板、一张谁都看不懂的票，还有“那个人得已经认识我们”。三样都和我对得上。阿虚在 18:40 用我的手机拍下了这一页。那天页边还没有后来那一行。"},
    {"id": "K07", "title": "多出来的那一行", "text": "我在 20:10 说了一句此前没人说过的话。20:50，八月二十日那一页的页边多出了这句话：{{PHRASE}}是春日的笔迹。阿虚 18:40 拍的照片里没有这一行。长门记得的八月二十日也没有。"},
    {"id": "K08", "title": "阿虚的既视感", "text": "阿虚记得在之前的某一次八月，听我在活动室说过这句话：{{PHRASE}}他还记得我坐在那把折叠椅上。长门的记录里，之前的任何一次八月都没有第六个人。"},
    {"id": "K09", "title": "我记得的臂章", "text": "春日给我的“异世界人”臂章是今天晚上才做的，之前任何一次八月都不存在。可我记得它，记得它一直放在活动室左手边那只抽屉里，和记得他们每个人的脸一样清楚。"},
    {"id": "K10", "title": "零点", "text": "零点前，朝比奈能在铁皮柜门上开一次回去的窗口。五人回去，这个为我分出来的八月就会合上，我也在里面。五人留下，零点后这里变成真正的九月，他们再也回不去，原来的世界里他们从八月三十一日起消失。要是零点时春日还觉得暑假没过完，一切会回到八月十七日，连我一起重来。"},
    {"id": "K11", "title": "第六只杯子", "text": "我进门以前，桌上已经有一只倒好的热茶。杯底有两圈水渍，外圈先干。春日认定是她倒的。朝比奈端着的茶壶那时还是满的。长门记下的是：十五点十分以前，第六人并不存在。"},
    {"id": "K12", "title": "空抽屉", "text": "二十二点三十一分，活动室左手抽屉是空的。拉手缺了一角。我记得“异世界人”臂章在那只抽屉里放了很多年。这条臂章是今晚才缝上的，布是新的。红线看起来比布更早。"},
    {"id": "K13", "title": "柜里的十五点十六分", "text": "十八点四十分，阿虚打开我的相册。里面已经有一张十五点十六分的照片，从铁皮柜里面往外拍。五个人都在，没有第六个，镜头前也没有手。柜门内侧有一道新刮痕，高度和照片里的亮痕一样。阿虚说这张不是他拍的。"},
]

HANDOUTS = [
    {"id": "H01", "title": "春日的笔记本（八月二十日）", "text": """
八月二十日，阴。无聊。

这个暑假：游泳、烟花、夜里看星星……全部完成。可是好像还少一样。

异世界人应该带着的东西：
· 会发光的薄板
· 一张谁都看不懂的票
还有，那个人得已经认识我们。

（要是明天就来就好了。算了，暑假最后一天来也行。）
""".strip(), "variants": []},
    {"id": "H01_REVISED", "title": "春日的笔记本（多出来的一行）", "text": """
同一本笔记本，同一页，同一块咖啡渍。

页边多了一行字，是春日的笔迹：{{PHRASE}}

阿虚 18:40 用我的手机拍下的照片里，这一行不存在。长门记得八月二十日春日写这一页时的样子，那时也没有这一行。
""".strip(), "variants": []},
    {"id": "H02", "title": "异世界人入团考试成绩单", "text": """
主考官：凉宫春日

第一关　图书馆　语言：半通过（由长门代念）
第二关　车站前　迷路：未能迷路，酌情通过
第三关　坡顶　　夕阳：发呆十七秒，通过

结论：外星人 ×　未来人 ×　超能力者 ×　异世界人 ○

背面是我按听到的先后抄的时间。亲自在场的那一关，和回来以后听来的两关，都在上面。抄完以后长门只核过时间，没有写原因。
""".strip(), "variants": []},
    {"id": "H03", "title": "长门的记录", "text": """
序列：八月十七日至三十一日，重复一万五千余次。

既往序列中的同行者：五人。第六人：无。

本序列偏差起点：八月二十日。偏差内容：未确定。

第六人最早记录：八月三十一日 15:17，活动室铁皮柜门口。

第六人与思念体的连接：无。

注：只记录可观测的事，不记录原因。
""".strip(), "variants": [
        _variant("第六人的时间痕迹：无跨时间移动。秒针倒走一次，人未被搬走。（朝比奈确认）", require=["P_K04"]),
        _variant("15:17，活动室内：小型闭锁空间一次，持续不足一秒，无神人。（古泉确认）", require=["P_K05"]),
        _variant("15:10 前，杯底外圈已干。当时第六人：无。满壶与“是我倒的”不一致。", require=["P_K11"]),
        _variant("15:16，相册中有柜内向外的照片一张。画面无第六人。拍摄者无记录。", require=["P_K13"]),
        _variant("20:50，阿虚的记忆：内容为第六人在既往序列中说过的话。既往序列中不存在第六人。", require=["P_K08"]),
        _variant("20:31，左手抽屉：空。22:30，臂章为当日晚间新制。第六人记忆中，它早已在该抽屉。", require=["P_K12"]),
        _variant("补记：入口无记录。随身物品与八月二十日的清单一致。15:16 的照片里也没有入口。", require=["R_ISEKAI"]),
        _variant("补记：15:17 的闭锁空间与凉宫春日既往的闭锁空间属同一类。不是终端。", require=["R_TERMINAL"]),
        _variant("补记：本序列内无人移动时间。照片与本记录未变。变化的是笔记本、阿虚的记忆，以及第六人关于臂章的记忆。", require=["R_TIME"]),
        _variant("补记：热茶与干痕说明有人在等。记录中的第六人仍从 15:17 才出现。等的动作在，等的人不在。", require=["R_WAITED"]),
        _variant("补记：若下午的记录是错的，18:40 的照片与 20:31 的空抽屉也应一起错。它们没有错。", require=["R_ALWAYS"]),
        _variant("补记：15:16 的照片不能证明第六人已在柜内。画面与记录都没有这个人。", require=["R_PHOTO"]),
    ]},
    {"id": "H04", "title": "阿虚写下的三条路", "text": """
一、回去。零点前开柜门。我们五个回原来的八月。这边会合上，你也在里面。

二、留下。不开门。零点以后是九月。我们五个留在这里，那边的我们从八月三十一日起就不见了。你留下。

三、什么都不做，等零点。要是那家伙觉得暑假还没完，就从八月十七日再来一遍。你也在。

写完了。怎么选是你的事，别让我们替你选。
""".strip(), "variants": []},
    {"id": "H05", "title": "朝比奈的纸巾", "text": """
时间移动　无
从过去　无
从未来　无
起点　15:17
更早　无记录
秒针倒走了一次
倒走的时候，人没有被搬走

发车表闪过 8 月 17 日。站名我读不出。
""".strip(), "variants": [
        _variant("后来把车票上的字对过。字形相同。我仍读不出。读得出的人自己知道。", require=["P_CITY"]),
    ]},
    {"id": "H06", "title": "三次时长", "text": """
15:17　0.8 秒　无神人
17:41　3.2 秒　无神人
20:51　7.1 秒　无神人

下一次，未记录。
""".strip(), "variants": []},
]


def _go(choice_id, text, feedback, dest, flags=(), require=(), exclude=(), clues=(), handouts=()):
    return _choice(
        choice_id, text, feedback, dest,
        flags=list(flags), require_flags=list(require), exclude_flags=list(exclude),
        clues=list(clues), handouts=list(handouts),
    )


SCENES = [
    _scene("S00", "三点十七分", _t(prose.S00, prose.EXTRAS["S00"]), [
        _go("O00a", "我先看清屋里的每一个人。", "五个人，五种反应。只有窗边那个短发少女，看我的时间比看别人都长。她多看的那一秒，目光在桌角那只已经倒好的杯子上，不在我脸上。", "S01", flags=["P_BASELINE_EYES"]),
        _go("O00b", "我先低头看一眼手机上的时间。", "屏幕上是 2026 年 8 月 31 日，15:17，没有信号。墙上的挂钟也指着三点十七分。秒数对得上。年份对不上。相册的图标在角落里，我没有点开。", "S01", flags=["P_BASELINE_SCREEN"]),
    ]),
    _scene("S01", "从柜子里来的人", _t(prose.S01, prose.EXTRAS["S01"]), [
        _go("O01a", "我说：我认得你们每一个人，也认得这间屋子。", "发带少女的眼睛亮得吓人：“连我们都认得？那就更是异世界人了！”她抓住我的袖子。扶椅子的男生没有笑。他问我认得到什么程度。高个男生仍在微笑，目光却先落到了发带少女身上。", "S01W", flags=["P_OPEN"]),
        _go("O01b", "我说：我也不知道自己怎么会在这里，让我先坐一下。", "女仆装少女把那只已经倒好的茶往我手边推了推，又停住，像这杯不该由她来递。扶椅子的男生点点头，站到我和发带少女中间。我没说出自己认得他们。这句话压在舌头底下。", "S01W", flags=["P_CAUTIOUS"]),
    ]),
    _scene("S01W", "第六只杯子", _t(prose.S01W, prose.EXTRAS["S01W"]), [
        _go("O01w1", "我问：这杯茶是谁倒的？", "发带少女说是她倒的，说得没有缝。女仆装少女把满壶抬高了一寸，茶汤贴着壶盖响。扶椅子的男生看见了那一寸。他没有替她说出来。短发少女在书页上又点了一个小点。", "S02", clues=["K11"], flags=["P_CUP_ASK", "P_K11"]),
        _go("O01w2", "我把杯子转过来，只数木纹上的干痕，不问。", "外圈干透，发白。内圈才深。两圈圆心重合，大小不重合。这只杯子在我进门以前就放过一次，进门前不久又放过一次。我把杯子转回原位。没有人要求我解释这两圈。短发少女看着干痕，没有看我。", "S02", clues=["K11"], flags=["P_CUP_RING", "P_K11"]),
    ]),
    _scene("S02", "日历上的红圈", _t(prose.S02, prose.EXTRAS["S02"]), [
        _go("O02a", "我什么也没说。", "长门把“10 / 20”那一页转向我，只转半寸，又收回去。阿虚看见了，没有帮我圆。春日还在哼她自己的那半句。", "S03", require=["P_OPEN"], flags=["A_CLING", "A_FAR", "A_SNEAK", "A_SIDE", "A_SHOW", "A_CAN_TELL", "A_QUIET"]),
        _go("O02b", "我顺着他说：说不定真的不止一次。", "古泉把笑从我身上拿掉，只对春日笑：“暑假最后一天，谁都会有这种感觉。”他把她的注意力拨回白板。阿虚盯着我：“你刚才那句，什么意思。”", "S03", require=["P_OPEN"], flags=["A_CLING", "A_ASK", "A_HIDE", "A_COLD", "A_SHOW", "A_CAN_TELL", "A_ECHO"]),
        _go("O02c", "我什么也没说。", "阿虚替我把话接走，说自己睡糊涂了。长门重新打开书，不再看我。20 号的浅勾还在她眼角的余光里。", "S03", require=["P_CAUTIOUS"], flags=["A_EXAM", "A_GUARD", "A_CARE", "A_SMILE", "A_NSHOW", "A_QUIET"]),
        _go("O02d", "我顺着他说：说不定真的不止一次。", "古泉把我身边的椅子挪开半步。阿虚低声问：“是随口说的？”春日终于听见“一次”这个字，说一次就够了，团员不需要预习暑假。", "S03", require=["P_CAUTIOUS"], flags=["A_EXAM", "A_WORRY", "A_TEA", "A_COLD", "A_NSHOW", "A_ECHO"]),
    ], variants=[
        _variant("春日从我进门起就抓着我的袖子。阿虚站到窗边，不跟我并排。", require=["P_OPEN"]),
        _variant("阿虚把椅子转到我和春日中间。朝比奈把茶又往我手边推了推，推到一半想起那杯不是她倒的，手停住。", require=["P_CAUTIOUS"]),
    ]),
    _scene("S03", "异世界人入团考试", _t(prose.S03, prose.EXTRAS["S03"]), [
        _go("O03a", "我跟长门去图书馆。", "春日点头，抓起马克笔就要出门。袖子还在她手里。", "S03B", clues=["K02"], flags=["A_WITH_Y"], require=["A_CLING"]),
        _go("O03b", "我跟长门去图书馆。", "春日在白板上写下“考生”，在下面点了两点。两点都是红的。第六个铅笔点仍在另一面。", "S03B", clues=["K02"], flags=["A_WITH_Y"], require=["A_EXAM"]),
        _go("O03c", "我跟朝比奈去车站前。", "春日已经走到门口，回头等我。袖子还被她抓着。", "S03B", clues=["K02"], flags=["A_WITH_M"], require=["A_CLING"]),
        _go("O03d", "我跟朝比奈去车站前。", "春日把“车站前”三个字圈起来：“这一关，我看着。”", "S03B", clues=["K02"], flags=["A_WITH_M"], require=["A_EXAM"]),
        _go("O03e", "我跟古泉去坡顶。", "春日拉着我的袖子往外走。古泉跟在后面，人却更靠近她。", "S03B", clues=["K02"], flags=["A_WITH_K"], require=["A_CLING"]),
        _go("O03f", "我跟古泉去坡顶。", "春日说：“坡顶那关，考生单独走。”古泉笑着让出半步路。", "S03B", clues=["K02"], flags=["A_WITH_K"], require=["A_EXAM"]),
    ], variants=[
        _variant("她的手还抓着我的袖子。", require=["A_CLING"]),
        _variant("阿虚走在我和春日中间。", require=["A_EXAM"]),
    ]),
    _scene("S03B", "秒表和浅勾", longer.S02B, [
        _go("O3b1", "我用黑掉的屏幕去照八月二十日那一格。", "黑屏幕照出我的眼睛，照不出铅粉。铅粉在纸上。20 号的勾比两边都轻。春日的红笔描过 31 号，没有描它。长门看了我照过去的角度，没有出声。", "S03L", flags=["P_INK"]),
        _go("O3b2", "我问阿虚：秒表为什么会停在十五点十七分？", "他按到第五次，秒表装死，停在零上。“它挑数字。”他说，“挑的还是你进门的数字。我拒绝把这个叫科学。我也拒绝把它叫没关系。”春日在门口喊出发。秒表被她丢进化妆包，丢进去以后还响了一下。", "S03L", flags=["P_WATCH"]),
    ]),
    _scene("S03L", "留着的灯", longer.S03L, [
        _go("O3ly1", "我记下公告栏上那个白茬的图钉孔。", "木头茬是白的。没有人承认拔过图钉。春日只看自己的名字。白茬在她目光外面。我跟着长门那一侧走。", "S03Y", flags=["P_PIN"], require=["A_WITH_Y"]),
        _go("O3ly2", "我问阿虚：灯为什么留着。", "“他说留灯是为了回来的人。”阿虚说，“我没问回来的人包不包括现在出门的这些。有些句子他只说半句。”图书馆的冷气已经能从路口闻见。", "S03Y", flags=["P_LIGHT"], require=["A_WITH_Y"]),
        _go("O3lm1", "我记下公告栏上那个白茬的图钉孔。", "木头茬是白的。春日走过的时候没有停在日期上。8 月 20 日仍在右下角。车站的方向更热。", "S03M", flags=["P_PIN"], require=["A_WITH_M"]),
        _go("O3lm2", "我问阿虚：灯为什么留着。", "“为了回来的人。”他重复古泉没说完的那半句，然后自己皱眉，“我讨厌这种半句。走吧。广场晒得很具体。”", "S03M", flags=["P_LIGHT"], require=["A_WITH_M"]),
        _go("O3lk1", "我记下公告栏上那个白茬的图钉孔。", "白茬放不久。不久的东西最容易被当成一直都在。坡在城的另一头。蝉已经在那边叫满了。", "S03K", flags=["P_PIN"], require=["A_WITH_K"]),
        _go("O3lk2", "我问阿虚：灯为什么留着。", "他看了一眼还亮着的活动室窗户。“留着就留着。”他说，“你要是在坡上回头看这盏灯，团长会说你作弊。她还没规定，但她会规定。”", "S03K", flags=["P_LIGHT"], require=["A_WITH_K"]),
    ]),
    _scene("S03Y", "去图书馆的路", _t(prose.S03Y, prose.EXTRAS["S03Y"]), [
        _go("O3ya", "我看清她书签上的“20”，和后面那两个字。", "是“偏差”。她把书签推进去的时候，拇指压住了这两个字。压住不是涂掉。字还在。阿虚说别太配合。我把这两个字记住，没有念出来。", "S04Y", flags=["P_PENCIL"]),
        _go("O3yb", "我问阿虚：图书馆那关，到底有什么需要查的？", "“团长的题，不用查。”他说，“她的结论写在出门以前。你要查的话，别让她看见你在查她。”长门的书签不再露角。公告栏上的铅笔日期被塑料膜压住，风一过，膜响，字还是 8 月 20 日。", "S04Y", flags=["P_ASK_LIB"]),
    ]),
    _scene("S03M", "去车站的路", _t(prose.S03M, prose.EXTRAS["S03M"]), [
        _go("O3ma", "我记住信号灯从 12 跳到 17 的那一下。", "12，17，11。中间那个 17 没有属于任何一次正常的倒计时。长门的眼睛在小屏上停过，和乱跳一样短。阿虚说是太阳晒的。灯自己恢复了。恢复不把 17 从我眼睛里拿掉。", "S04M", flags=["P_SIGNAL"]),
        _go("O3mb", "我看着朝比奈按住口袋的那只手。", "硬角每三步碰一次她的手腕。她按回去的力度一次比一次轻，像怕按出声。古泉用遮阳棚的颜色挡住春日的视线。广播里那个被切断的站名尾音，我没有再去追。", "S04M", flags=["P_POCKET_WATCH"]),
    ]),
    _scene("S03K", "去坡顶的路", _t(prose.S03K, prose.EXTRAS["S03K"]), [
        _go("O3ka", "我问古泉：你的手机现在是几点？", "“和墙钟一致。”他说。他没有把屏幕转过来。口袋里那一下震动已经过去了。他补了一句：“坡上如果再震，你就当没听见。听见了也别在风里问。”", "S04K", flags=["P_ASK_TIME"]),
        _go("O3kb", "我数那一拍里，蝉停了多久。", "不到一秒。全部的蝉，不是一只。停完又叫，叫得比停之前更齐。长门的拇指在书页上留下一道白印。白印被她按平。贩卖机上那个一闪的 8 月 17 日，没有人再提。", "S04K", flags=["P_CICADA"]),
    ]),
    _scene("S04Y", "图书馆", _t(prose.S04Y, prose.EXTRAS["S04Y"]), [
        _go("O04a", "我指着她记录上八月二十日那一行。", "她看了我一眼，把那一行转向我。空着的偏差内容对着我。她补了一句，只有我听见：“缝不是我打开的。铅笔字也不是今天写的。”", "S05W", clues=["K01", "K03"], flags=["A_POINTED", "A_CAN_TELL"], require=["A_SHOW"]),
        _go("O04b", "我不指。", "她把书合上。那一句她没有添。借书卡的角从书里露出一个日期，又被她按回去。", "S05W", clues=["K01", "K03"], flags=["A_SKIP"], require=["A_SHOW"]),
        _go("O04c", "我指着八月二十日那一行。", "她把记录从阿虚那边转向我。空行对着我。阿虚的眉毛动了一下。他没有问我为什么知道要指这一行。", "S05W", clues=["K01", "K03"], flags=["A_POINTED", "A_CAN_TELL"], require=["A_NSHOW"]),
        _go("O04d", "我不指。", "记录仍朝着阿虚。她没有看我。我抱着的那本字典页边上，“认识我们”四个字还沾在指腹上，一点铅粉。", "S05W", clues=["K01", "K03"], flags=["A_SKIP"], require=["A_NSHOW"]),
    ], variants=[
        _variant("长门回来时，把记录转到我这边。八月二十日那一行是空的，前后都是重复的八月。", require=["A_SHOW"]),
        _variant("长门回来时，把记录只转向阿虚。我在对面。她没有看我。", require=["A_NSHOW"]),
    ]),
    _scene("S04M", "车站前", _t(prose.S04M, prose.EXTRAS["S04M"]), [
        _go("O05a", "我去追发车表上那一行日期。", "我退回半步，残影还在。整座城市的名字和车票上的字一笔一笔对上。他们读不出的那些字，我读得出。春日把我拽回队里。成绩单上没有缺考。残影在我被拽走以后灭了。", "S05W", clues=["K04"], handouts=["H05"], flags=["A_PULLED", "P_K04", "P_CITY"], require=["A_CLING"]),
        _go("O05b", "我留在她身边，不追那一行。", "队形没变。她的手还抓着我的袖子。发车表已经是这个镇的站名。偏旁还在眼睛里，名字没有对完。朝比奈把纸巾按进掌心。", "S05W", clues=["K04"], handouts=["H05"], flags=["A_FORMATION", "P_K04"], require=["A_CLING"]),
        _go("O05c", "我去追发车表上那一行日期。", "名字对上了。车票上的城市，在 8 月 17 日那一行里亮过。春日在成绩单上写下“缺考”。古泉转身去安抚她，安抚的时候挡着我的口袋，不让车票被第二个人看见。", "S05W", clues=["K04"], handouts=["H05"], flags=["A_ABSENT", "P_K04", "P_CITY"], require=["A_EXAM"]),
        _go("O05d", "我留在她身边，不追那一行。", "她写了“通过”。阿虚在旁边吐了口气。表上的字恢复以后，我没有第二眼。朝比奈把读数留在口袋里，茶和冰棍递到我手里。", "S05W", clues=["K04"], handouts=["H05"], flags=["A_PASSED", "P_K04"], require=["A_EXAM"]),
    ], variants=[
        _variant("朝比奈把读数写在纸巾上，趁春日不注意塞进我手里。", require=["A_SNEAK"]),
        _variant("朝比奈把纸巾递给阿虚，人躲到他身后。", require=["A_HIDE"]),
        _variant("朝比奈把茶和那张读数一起递到我手里。", require=["A_CARE"]),
        _variant("朝比奈把茶给我，读数留在口袋里。", require=["A_TEA"]),
    ]),
    _scene("S04K", "坡顶", _t(prose.S04K, prose.EXTRAS["S04K"]), [
        _go("O06a", "我继续背对着他们。", "风把后半句送全了。古泉说，零点八秒里的形状不是房间，是一把空椅子，和墙边那把还没打开的折叠椅重合。阿虚“啊”了一声，很短。春日在坡那头开始报时。", "S04K2", clues=["K05"], flags=["A_CHAIR", "P_HEARD_CHAIR", "P_K05"]),
        _go("O06b", "我回头看了他们一眼。", "后半句被他咽回去。他看见我的耳朵还在风里。春日在坡道那头喊：“考生回头，扣分！”阿虚别开脸，假装在看坡下的路。", "S04K2", clues=["K05"], flags=["A_LOOKED", "P_K05"]),
    ], _picture(
        (YELLOW, "      ■ ■ ■"),
        (DARK_YELLOW, "  ■ ■ ■ ■ ■ ■ ■"),
        (DARK_RED, "■ ■ ■ ■ ■ ■ ■ ■ ■"),
        (DARK_GRAY, "■   ■ ■   ■   ■ ■"),
    ), variants=[
        _variant("古泉的人站在春日那边。笑还在。", require=["A_SIDE"]),
        _variant("他对我笑了一下，只谈风大不大。", require=["A_SMILE"]),
        _variant("他已经不对我笑了。", require=["A_COLD"]),
    ]),
    _scene("S04K2", "那一秒", _t(prose.S04K2, prose.EXTRAS["S04K2"]), [
        _go("O06c", "我朝那一秒迈了一步。", "脚下那一声门响更近了。古泉按住我的肩膀，力道不大：“别告诉团长。”他没有道歉。手机在他掌心里发热。", "S05W", flags=["A_BLOCK"], require=["A_COLD"]),
        _go("O06d", "我站着没动。", "他看了一眼自己的手机，收了起来。下山的路上他不说话。蝉在坡下重新叫满。", "S05W", flags=["A_POCKET"], require=["A_COLD"]),
        _go("O06e", "我朝那一秒迈了一步。", "他立刻说：“对不起。”笑停了。他站到我侧面，挡住春日看过来的角度，直到那一秒过去。", "S05W", flags=["A_SORRY"], exclude=["A_COLD"]),
        _go("O06f", "我站着没动。", "他没有当时道歉。下山仍只谈天气。谈天气的句子一次比一次短。", "S05W", flags=["A_LATER"], exclude=["A_COLD"]),
    ]),
    _scene("S05W", "校门口", _t(longer.S05W, more.S05W), [
        _go("O5y1", "我把凉掉的两圈茶渍指给长门。", "她看了两圈，不碰杯子。“外圈更早。”她说。只说这一句。春日的果汁还没买回来。门缝够用。", "S06RY", flags=["P_STAIN"], require=["A_WITH_Y"]),
        _go("O5y2", "我问白茬的图钉孔，是不是今天下午才有的。", "阿虚说他早上经过的时候没注意。古泉说白茬放不久。不久和“一直都在”是两套话。长门没有把图钉写进纸里。她说没有时间。", "S06RY", flags=["P_PIN_ASK"], require=["A_WITH_Y"]),
        _go("O5m1", "我把凉掉的两圈茶渍指给长门。", "“外圈更早。”她说。朝比奈的纸巾还在口袋里鼓着。两件事都比果汁早。春日还在走廊里。", "S06RM", flags=["P_STAIN"], require=["A_WITH_M"]),
        _go("O5m2", "我问白茬的图钉孔是谁留下的。", "没有人认。阿虚把“没人认”重复了一遍，像这本身就是一条线索。门垫上的灰还没干透。", "S06RM", flags=["P_PIN_ASK"], require=["A_WITH_M"]),
        _go("O5k1", "我把凉掉的两圈茶渍指给长门。", "她点了一下外圈。“更早。”坡上的风已经不在这间屋子里。杯子上的时间还在。", "S06RK", flags=["P_STAIN"], require=["A_WITH_K"]),
        _go("O5k2", "我问白茬的图钉孔算不算今天的新东西。", "古泉说：“新的东西最容易被讲成旧的。尤其是没有人看见它变新的时候。”春日的声音在走廊里折回来。我们把这句话停在这里。", "S06RK", flags=["P_PIN_ASK"], require=["A_WITH_K"]),
    ]),
    _scene("S06RY", "另外两关", _t(prose.S06RY, prose.REPORT_M, prose.EXTRAS["REPORT_M"], prose.REPORT_K, prose.EXTRAS["REPORT_K"]), [
        _go("O6rya", "我把车票抽出来，问朝比奈：亮过的是不是这一列。", "她看了很久，点一次头。字形相同。她仍然读不出。她把纸巾上“站名”那两个残字对折进去，塞回口袋。古泉看着门缝，没有让这句再响一点。", "S06L", clues=["K04", "K05"], handouts=["H05"], flags=["P_CITY", "P_K04", "P_K05"]),
        _go("O6ryb", "我等门缝里的脚步走远，问古泉：没说完的形状是什么。", "他等到春日的声音转到走廊尽头。“空椅子。”他说，“和墙边那把折叠椅重合。当时它没有打开。人还没有坐。”长门把这句补进纸里，补在门缝重新变响以前。", "S06L", clues=["K04", "K05"], handouts=["H05"], flags=["P_HEARD_CHAIR", "P_K04", "P_K05"]),
    ]),
    _scene("S06RM", "另外两关", _t(prose.S06RM, prose.REPORT_Y, prose.EXTRAS["REPORT_Y"], prose.REPORT_K, prose.EXTRAS["REPORT_K"]), [
        _go("O6rma", "我问长门：十五点零二分还书的时候，柜门热不热。", "“十五点零二分，门是柜子，不热。”她说，“热从十五点十七分开始。还书的动作没有手。卡上只有时间。”阿虚把 15:02 和 15:17 分开写。中间他留了一行空。", "S06L", clues=["K01", "K03", "K05"], flags=["P_CARD", "P_K05"]),
        _go("O6rmb", "我等门缝合拢一点，问古泉那半句形状。", "“空椅子。”他说完就停。停在折叠椅这个词前面。是我把折叠椅接上去的。他点头，只点一次。长门写下轮廓，没有写下“等一个人坐”。", "S06L", clues=["K01", "K03", "K05"], flags=["P_HEARD_CHAIR", "P_K05"]),
    ]),
    _scene("S06RK", "另外两关", _t(prose.S06RK, prose.REPORT_Y, prose.EXTRAS["REPORT_Y"], prose.REPORT_M, prose.EXTRAS["REPORT_M"]), [
        _go("O6rka", "我把车票和朝比奈读不出的那一列放在一起。", "她用指节量字形，不读音。量完她说：“相同。”相同两个字她写在纸巾背面，写得很小。古泉用果汁杯把这行挡住。", "S06L", clues=["K01", "K03", "K04"], handouts=["H05"], flags=["P_CITY", "P_K04"]),
        _go("O6rkb", "我问长门：字典页边上那四个字，是哪一天写的。", "“八月二十日。认识我们。不是今天的墨。”她把借书卡的角转过来，归还时刻是今天 15:02。15:02 没有第六个人。字比人早。", "S06L", clues=["K01", "K03", "K04"], handouts=["H05"], flags=["P_MARGIN", "P_K04"]),
    ]),
    _scene("S06L", "抄在背面", _t(prose.EXTRAS["S06"], longer.S06L, more.S06L), [
        _go("O6la", "我把 15:02 和 15:17 分成两行，中间留空。", "长门的指节没有敲。空行留着。阿虚看着那一行空，说空着比写“未知”干净。春日的脚步在走廊尽头拐弯。我们把纸翻回正面。", "S07", flags=["P_GAP_EARLY"]),
        _go("O6lb", "我问长门：这些时间里，哪一个她不肯写原因。", "“全部。”她说，“原因一写，就会变成我的原因。”她在最后添了“原因，空”。笔帽扣上的时候，春日的声音正好回来。", "S07", flags=["P_NO_REASON"]),
    ]),
    _scene("S07", "只剩下一项", _t(prose.S07, prose.EXTRAS["S07"]), [
        _go("O07a", "我把手机、车票和那一页摆在一起，一样一样对。", "会发光的薄板。看不懂的票。已经认识他们的人。三样都在。15:16 的照片插在这个队列前面，像一件清单上没写、却先到了的东西。春日说这叫准备充分。她的手还抓着我的袖子。", "S07P", clues=["K06", "K13"], handouts=["H01", "H02"], flags=["P_COMPARED_LIST", "P_K13"], require=["A_CLING"]),
        _go("O07b", "我把手机、车票和那一页摆在一起，一样一样对。", "三样都对上了。春日说：“考生，准备充分。”阿虚说：“对不上才正常。”他的手指还停在 15:16 那张照片的刮痕上。", "S07P", clues=["K06", "K13"], handouts=["H01", "H02"], flags=["P_COMPARED_LIST", "P_K13"], require=["A_EXAM"]),
        _go("O07c", "我问春日：八月二十日那天，你为什么会写这一页？", "她想了想：“那天特别无聊。笔还没水。我就想，要是有个异世界人来就好了。最好已经认识我们。明天来最好，最后一天来也行。”她说完去翻零食。古泉的手机短短地震了一下。", "S07P", clues=["K06", "K13"], handouts=["H01", "H02"], flags=["P_ASKED_HARUHI", "P_K13"]),
    ], variants=[
        _variant("白板的车站那格写着“缺考”。", require=["A_ABSENT"]),
        _variant("白板的车站那格先写了“缺考”，又被她划掉。", require=["A_PULLED"]),
        _variant("白板的车站那格写着“通过”。", require=["A_PASSED"]),
        _variant("她把我拽回队以后，袖子就没松开过。", require=["A_FORMATION"]),
    ]),
    _scene("S07P", "两张照片", _t(longer.S07P, more.S07P, more3.S07P), [
        _go("O7p1", "我把 15:16 的刮痕高度，和我在柜门里侧看见的那道亮对一下。", "对得上。都在眼睛下面一点。阿虚让我比划给他看。比划完他看着自己的手，说他下午拉开柜门的时候，亮茬已经在了。他当时以为是拖把磕的。拖把是干的，磕不出新亮。", "S08", flags=["P_SCRATCH"]),
        _go("O7p2", "我问朝比奈：十五点十六分，你的装置在不在身上。", "“在口袋里。没响。”她说，“没响就不是有人从别的时间伸进来。照片是直接出现的。直接出现这句话，我可以负责。再往前我不能负责。”她看了一眼春日的零食袋，把后面的话咽回去。", "S08", flags=["P_NO_BEEP"]),
    ]),
    _scene("S08", "一句还没人说过的话", _t(prose.S08, prose.EXTRAS["S08"]), [
        _choice("O08a", "我说：“我是自己推门进来的。”", "长门点头：“记下了。20:10。之前的序列里，没有人说过这句话。”录音的红点跳了一下，像把这句咬住。", "S08W", clues=["K01", "K03", "K04", "K05"], handouts=["H03"], flags=["A_DOOR"], set_text=("PHRASE", "我是自己推门进来的。")),
        _choice("O08b", "我说：“下一个夏天，我也想跟你们一起过。”", "朝比奈抬起头看我。阿虚张了张嘴，没有吐槽。长门点头：“记下了。20:10。”红点继续亮。", "S08W", clues=["K01", "K03", "K04", "K05"], handouts=["H03"], flags=["A_SEP"], set_text=("PHRASE", "下一个夏天，我也想跟你们一起过。")),
        _choice("O08c", "我说：“暑假还没过完。”", "长门把这句话记下。20:10。屋里安静了两秒。风扇转到头，又转回来。", "S08W", clues=["K01", "K03", "K04", "K05"], handouts=["H03"], flags=["A_LOOP"], set_text=("PHRASE", "暑假还没过完。")),
    ], variants=[
        _variant("古泉把下午咽回去的半句补上：“空椅子。和那把折叠椅重合。当时没有打开。”", require=["A_LOOKED"]),
        _variant("阿虚问“不止一次”是什么意思。问完他才让我说那句话。", require=["A_ASK"]),
        _variant("阿虚站在窗边，不跟我并排。录音的手机放在桌子正中，离他比离我更远。", require=["A_FAR"]),
    ]),
    _scene("S08W", "等她回来", _t(prose.S08W, prose.EXTRAS["S08W"]), [
        _go("O8wa", "我拉开左手边那只抽屉。", "空的。拉手的缺口磕着指腹，磕的位置和我记忆里一样，记忆却说这里应该有一条旧臂章。抽屉底上只有一根红线，一根回形针。红线比灰尘新一点。我把抽屉推上。红线留在掌心里。我没有给任何人看。", "S08L", flags=["P_DRAWER"]),
        _go("O8wb", "我问古泉：手机上第三行为什么是空的。", "他终于把屏幕转了十五度。第一行 0.8 秒。第二行 3.2 秒。第三行没有数字，只有一条横线。“还没发生。”他说，“发生了我会写。现在写，就像替团长预约。”他把屏幕扣上。", "S08L", flags=["P_SECONDS"]),
        _go("O8wc", "我对着录音说：清单和我身上的东西是同一张单子。这算结论吗？", "长门摇头。“20:22。对照物还没有变化。臂章不在桌上。记忆还没有跟记录打架。”她说，“现在定，会把还没发生的行写成已经发生。等。”阿虚把这句也录了进去。录完他看我，像在说：你倒是敢提前交卷。", "S08L", flags=["P_EARLY"]),
    ]),
    _scene("S08L", "六条", _t(longer.S08L, more.S08L), [
        _go("O8la", "我把阿虚列的六条按时间重排，不让顺序骗人。", "第六条被我划到 18:40。第五条旁边我补了零点八秒。他看着我划，没有拦。“纸比我嘴硬。”他说，“你现在就比我硬。先别硬到结论上去。”", "S08M", flags=["P_TIMELINE"]),
        _go("O8lb", "我把手按住，不让它再弯向那只抽屉。", "按住了。缺口还在视线里。阿虚说他数过，这是第三次。我没有拉开。没有拉开也是一件可以记下的事。长门没有记。她只记拉开过的、空着的、热过的。", "S08M", flags=["P_HAND"]),
    ]),
    _scene("S08M", "塑料袋的声音", _t(longer.S08M, more.S08M, more3.S08M), [
        _go("O8ma", "我让杯子和干痕错开的那两厘米留着。", "长门说两厘米也是事实。朝比奈的手离开杯耳。错开的干痕独自留在桌上，像一个不再需要杯子证明的圈。门外的笔帽敲了三下。", "S09", flags=["P_TWOCENT"]),
        _go("O8mb", "我问长门：二十点二十二分的空行，要空到什么时候。", "“空到有东西可以写，或者空到零点。”她说，“现在没有东西。不要用句子去填。”笔还放在空行旁边。笔没有滚进去。门被肩膀顶开。", "S09", flags=["P_ASK_BLANK"]),
    ]),
    _scene("S09", "多出来的那一行", _t(prose.S09, prose.EXTRAS["S09"]), [
        _go("O09a", "我把照片和笔记本一处一处对照。", "折角、墨点、咖啡渍都一样。只有那一行，18:40 的照片里没有。句号比正文更圆。圆的那个点盖不住。", "S09L", clues=["K07"], handouts=["H01_REVISED"], flags=["P_COMPARED_PHOTO"]),
        _go("O09b", "我去摸柜门。", "门板是温的，不再烫。锁芯那一块仍比旁边热。热退得很慢，慢得像有一只手按过以后忘了拿开。缝没有开。拖把的影子从门缝底下露出来，干的。", "S09L", clues=["K07"], handouts=["H01_REVISED"], flags=["A_LOOK_DOOR"], require=["A_DOOR"]),
        _go("O09c", "我看阿虚的手机。", "屏幕上有一个九月一日 7:10 的闹钟，备注是空的。他没设过。几秒以后，日期自己空掉，闹钟还在，响的对象消失了。他把屏幕扣在桌上，不让春日看见。", "S09L", clues=["K07"], handouts=["H01_REVISED"], flags=["A_LOOK_ALARM"], require=["A_SEP"]),
        _go("O09d", "我去看日历。", "31 日前面的勾少了一格。少的是 20 号那道浅的。红的那些还在。浅的先走。长门看着那一格，没有指给我。纸白出来的地方，铅笔的压痕还在。", "S09L", clues=["K07"], handouts=["H01_REVISED"], flags=["A_LOOK_CAL"], require=["A_LOOP"]),
    ], variants=[
        _variant("柜门是温的。阿虚记得以前某一次八月，我从这只柜子里走出来。他没看我。", require=["A_DOOR", "A_FAR"]),
        _variant("柜门是温的。阿虚记得我从柜子里走出来。他说的时候看着我。", require=["A_DOOR"], exclude=["A_FAR"]),
        _variant("阿虚把闹钟屏幕转向我：“你也看见了？”", require=["A_SEP", "A_WORRY"]),
        _variant("阿虚把屏幕转向我：“这是你写进去的？”", require=["A_SEP", "A_ASK"]),
        _variant("阿虚把手机收进口袋。长门说：九月一日，7:10，备注空。", require=["A_SEP", "A_FAR"]),
        _variant("夜市的方向有人试音。长门说这场夜市以往不存在。", require=["A_SEP", "A_GUARD"]),
        _variant("日历上的勾从 31 日往前少了一格。少的是浅的那格。长门把它指给我。", require=["A_LOOP", "A_CAN_TELL"]),
        _variant("勾少了一格。浅的那道先不见。长门看着日历，没有指。", require=["A_LOOP"], exclude=["A_CAN_TELL"]),
    ]),
    _scene("S09L", "句号盖不住", _t(longer.S09L, more.S09L), [
        _go("O9la", "我记住“臂章”这两个字，不问。", "春日改口叫它惊喜。改口改得很快。朝比奈的手在死结上停过两秒。古泉报给长门的那个 7，埋在风扇噪音里。我只保住了整数。", "S09W", flags=["P_HEARD_BAND"]),
        _go("O9lb", "我问古泉：第三次比前两次长多少。", "他等风扇转到最响。“7.1 秒。”他说，“无神人。再问小数点以外的，等有桌子。”长门把这行折到背面。背面已经有划掉的水渍。现在有两层。", "S09W", flags=["P_SEVEN"], handouts=["H06"]),
    ]),
    _scene("S09W", "昨天", _t(prose.S09W, prose.EXTRAS["S09W"]), [
        _go("O9wa", "我问老板：昨天站在这里的人，长什么样。", "他看我的袖子，袖子是空的。“跟你差不多高。胳膊上有一块红。我当时以为是晒的。”他说完就去挂灯，不再解释昨天这个摊子在不在。阿虚的嘴张着，没有把反驳说出来。", "S10", flags=["P_STALL"]),
        _go("O9wb", "我不问。我看棚脚翻出来的土，干了没有。", "断面是潮的，潮上面有一层刚干的灰。长门用鞋尖点开灰：“不超过今天傍晚。”没有脚印。老板的“昨天”停在空气里，没有落到土上。", "S10", flags=["P_MUD"]),
    ]),
    _scene("S10", "捞金鱼", _t(prose.S10, prose.EXTRAS["S10"]), [
        _go("O10a", "我过去捞。", "她拉我进人群。纸网一沾水就软。我一张也没保住。老板说：“昨天你也没捞到，别费网。”阿虚在灯绳尽头把后半句留着。春日笑得直不起腰。", "S10L", flags=["A_WENT"]),
        _go("O10b", "我留在阿虚旁边。", "他把既视感说完，又补了一句他不愿意补的：“还有一句。她把什么东西套到你胳膊上，说不许弄丢。可你现在胳膊上什么都没有。”春日从摊子那边走回来，抓住我的袖子。", "S10L", clues=["K08"], flags=["A_SKIP_FISH", "P_K08", "P_LOSE_EARLY"], require=["A_CLING"]),
        _go("O10c", "我留在阿虚旁边。", "他把既视感说完，又补上那句还没发生的“不许弄丢”。说完他自己皱眉。春日在成绩单背面写：夜市缺考。字写在我抄过时间的那一面的角落，没有盖住 15:17。", "S10L", clues=["K08"], flags=["A_SKIP_FISH", "A_ABSENT", "P_K08", "P_LOSE_EARLY"], require=["A_EXAM"]),
    ], _picture(
        (RED, "■     ■     ■     ■"),
        (YELLOW, "  ■ ■   ■ ■   ■ ■"),
        (DARK_CYAN, "■ ■ ■ ■ ■ ■ ■ ■ ■ ■"),
    ), variants=[
        _variant("她的手还抓着我的袖子。红灯把袖口照成另一种红。", require=["A_CLING"]),
        _variant("她把马克笔夹在成绩单上。夹的位置避开了背面的时间。", require=["A_EXAM"]),
    ]),
    _scene("S10L", "半价", longer.S10L, [
        _go("O10d", "我看着老板把那张系着红线的网塞回去。", "塞回去的网柄只露出一截红。红和灯绳不是一种红。灯绳是新的塑料。这一截像布拆下来的线。他改抽了白线的那张，递给春日。春日没看见这次改抽。", "S11", clues=["K08"], flags=["P_RED_NET", "P_K08"]),
        _go("O10e", "我问阿虚：便条上另一半，坡上再说的是哪一半。", "“抽屉。”他说，“长门不让我在人多的地方说完。你的手指弯过。我数过。别在这里弯第三次。这里红灯太多，什么都像已经旧了。”", "S11", clues=["K08"], flags=["P_NOTE_HALF", "P_K08"]),
    ]),
    _scene("S11", "写着我的臂章", _t(prose.S11, prose.EXTRAS["S11"]), [
        _go("O11a", "我问长门：我记得的别的事，也会是这样来的吗？", "长门说：“你的记忆里，我分辨不出哪些早于今天下午。它们看起来都一样。”红线弹出来，又被风按回去。", "S11M", clues=["K09"], flags=["P_ASKED_MY_MEMORY", "P_K09"], exclude=["A_LOOP"]),
        _go("O11b", "我把臂章戴正。", "布是新的，马克笔的味道还没散。线是软的。春日回头喊我们走快点。喊声里没有第二次“不许弄丢”。一次已经够用。", "S11M", clues=["K09"], flags=["P_KEPT_ARMBAND", "P_K09"], exclude=["A_LOOP"]),
        _go("O11c", "我问长门：我记得的别的事，也会是这样来的吗？", "长门说：“分辨不出。勾少了的那一格，我没有指给你。浅的那道先走。”", "S11M", clues=["K09"], flags=["P_ASKED_MY_MEMORY", "P_K09"], require=["A_LOOP"], exclude=["A_CAN_TELL"]),
        _go("O11d", "我把臂章戴正。", "布是新的。日历上少掉的浅勾，她仍不指。压痕还在纸里。", "S11M", clues=["K09"], flags=["P_KEPT_ARMBAND", "P_K09"], require=["A_LOOP"], exclude=["A_CAN_TELL"]),
        _go("O11e", "我把少掉的那一格指给春日。", "她停下。看了很久。浅的那格空着，红的那些还在。她说：“怎么感觉，暑假还没过够。”说完她又笑，把这句话当成一句感叹，继续往前走。", "S11M", clues=["K09"], flags=["A_TOLD", "P_K09"], require=["A_LOOP", "A_CAN_TELL"]),
        _go("O11f", "我只把少掉的那一格告诉长门。", "长门点头。春日已经走到前面十步，没听见。十步是今晚她自己拉开的距离。", "S11M", clues=["K09"], flags=["A_KEPT", "P_K09"], require=["A_LOOP", "A_CAN_TELL"]),
    ], variants=[
        _variant("阿虚在坡上才把夜市里没说完的那句补上。补上的时候，臂章已经在我胳膊上了。", require=["A_WENT"]),
        _variant("他在夜市说过“不许弄丢”。这句话现在从春日嘴里又来了一次。两次的声音不一样。字一样。", require=["P_LOSE_EARLY"]),
    ]),
    _scene("S11M", "便条", _t(longer.S11M, more.S11M, more3.S11M), [
        _go("O11m1", "我把便条上的“年龄”两个字又看一遍，不问。", "布是今天的。线的格子她提前留了。格子留好的时候，她还没看见这根线。阿虚说这叫她知道要有一格，不叫她知道线会来。风把晚报的日期按在我鞋面上。", "S11W", flags=["P_AGE"]),
        _go("O11m2", "我问长门：红线的年龄，你现在能记吗？", "“能记看到的。”她说，“看到的是：线比布软，颜色更深。软和深不是年份。年份等抽屉。坡上对数字，会对错。”她不再看我的袖子。", "S11W", flags=["P_ASK_THREAD"]),
    ]),
    _scene("S11W", "空抽屉", _t(prose.S11W, prose.EXTRAS["S11W"]), [
        _go("O11w1", "我把臂章上的红线和 20:31 的“空”放在一起看。", "新布。旧记忆。空抽屉。三句话指着同一只拉手。朝比奈的装置不响。不响把“抽屉穿越”从桌上拿掉。剩下的那一种，她不肯命名。", "S12", clues=["K12"], flags=["P_LINED", "P_K12"]),
        _go("O11w2", "我问阿虚：你记得的那次八月，我胳膊上有没有这条。", "他想了很久。“有一块红。我说不清是布还是灯。现在看来是布。可那次八月如果没有你，这块红是我后来补上的，还是那次八月本来就在等这块红，我分不清。”他不再看臂章。", "S12", clues=["K12"], flags=["P_ASK_BAND", "P_K12"]),
    ], variants=[
        _variant("我掌心里那根红线还在。抽屉里已经没有第二根。臂章缝上的这一根，颜色相同，软硬相同。", require=["P_DRAWER"]),
        _variant("我没有拉开过。长门拉开过，或者她只看过。纸上写的是空。空没有红线。", require=[], exclude=["P_DRAWER"]),
    ]),
    _scene("S12", "按时间排开", _t(prose.S12, prose.EXTRAS["S12"]), [
        _go("O12p1", "我从干痕开始排。杯子放在最左边。", "两圈干痕对着 15:10。手机放在它右边。纸巾的 15:17 从缝里露出来。阿虚的白纸仍是空白。他等我排完，不帮我排。", "S12L", flags=["P_ORDER_CUP"]),
        _go("O12p2", "我从柜里的那张照片开始排。", "15:16 在最左边。没有我。18:40 在后面，页边还是干净的。再后面才是多出来的句子，和胳膊上的新布。顺序一排开，中间的空就变得很窄，窄得只够一个人从柜子里走出来。", "S12L", flags=["P_ORDER_PHOTO"]),
    ]),
    _scene("S12L", "各自能证明的", longer.S12L, [
        _go("O12l1", "我问长门：桌上这些箭头，你为什么不画。", "“画了就会变成我的箭头。”她说，“我的箭头会盖住你的。零点那一行还空着。空着的时候，箭头不该先落地。”笔帽仍对着我。", "S12R", flags=["P_BLANK"]),
        _go("O12l2", "我问阿虚：纸比嘴硬。三条路你现在写不写。", "“不写。”他说，“你的箭头还没落地。我现在写，写出来的会像建议。建议是私货。私货我今晚不夹。”笔放在纸外。纸还是白的。", "S12R", flags=["P_PAPER_WAIT"]),
    ]),
    _scene("S12R", "按顺序念", _t(longer.S12R, more.S12R, more3.S12R), [
        _go("O12r1", "我指出 15:10 和 15:17 中间，纸上没有人。", "长门把那两行再念了一遍。中间是刮痕、照片、没有拍摄者。她不添句子。阿虚说：“空着就空着。空着也是你刚才指的那个东西。”", "S12C", flags=["P_GAP"]),
        _go("O12r2", "我指出 18:40 的照片没有跟着页边一起改。", "长门点头。“照片停着。记录停着。笔记本和两个人的记忆没有停。”她说的两个人，一个是阿虚，一个是我。她没有把这句写成原因。", "S12C", flags=["P_GAP_PHOTO"]),
    ]),
    _scene("S12C", "箭头", """
箭头还是没有人画。

桌上的东西按时间排着。四个人看我。笔帽对着我。空白的纸在阿虚手边，笔在纸外。

楼上的风小了。春日的脚步仍在找一个可以放烟花的位置。
""", [
        _choice("O12a", "我是从另一个世界来的。我记得那个世界，那才是我原来待的地方。", "阿虚问：“那你的入口在哪儿？”长门的记录里没有。朝比奈的装置里也没有。15:16 的照片从柜子里面往外拍，镜头前没有人。古泉说，从另一个世界来的人，随身的东西不该正好是团长十一天前写下的清单。我摸到臂章的红线。我记得它的方式，和我记得“原来那个世界”的方式，是同一种清楚。", "S12C", flags=["R_ISEKAI"], exclude=["R_ISEKAI"]),
        _choice("O12b", "我是思念体或者别的什么造出来的观测装置，只是自己不知道。", "长门摇头：“没有线路。”古泉说，下午三点十七分那个闭锁空间，和他见过的那些是同一种东西。团长的东西。时长在变长。变长的不是一台被人放下的仪器。", "S12C", flags=["R_TERMINAL"], exclude=["R_TERMINAL"]),
        _choice("O12c", "这只是普通的时间改写：有人回到过去写下那一行，又改了记忆。", "朝比奈说，今天没有任何人移动过时间，包括她自己。秒针倒走过，人没有被搬走。照片和长门的记录都停在原处。变了的是笔记本、阿虚记得的那一次八月，还有我记得的那条臂章。方向都朝着“我本来就在”。", "S12C", flags=["R_TIME"], exclude=["R_TIME"]),
        _choice("O12e", "第六只杯子是热的。他们在等我。所以我本来就在这个八月里，只是下午才被想起来。", "阿虚问：那 15:05 你在哪儿。长门的纸上，15:10 水渍已经干了，第六人仍是无。春日认定茶是她倒的。朝比奈的茶壶那时是满的。等的动作有。等的人没有。满壶和干痕把“本来就在”挡在 15:17 以前。", "S12C", flags=["R_WAITED"], exclude=["R_WAITED"], require_clues=["K11"]),
        _choice("O12f", "臂章的记忆是真的。错的是今天下午这些记录。", "18:40 的照片不改口。20:31 的抽屉是空的。布是新的，马克笔的味道还在袖子上。长门的记录和那张照片停着。动过的是我记得的那些年，还有阿虚记得的椅子。停着的那两样，比动过的那两样更难叫做错。", "S12C", flags=["R_ALWAYS"], exclude=["R_ALWAYS"], require_clues=["K12"]),
        _choice("O12g", "十五点十六分的照片是我藏在柜子里拍的。我比记录更早到。", "照片里没有第六个人。长门说 15:16 门还是柜子，记录里没有人在门内。柜子里如果有我，镜头前应该有一只手，纸上应该有一行。两样都没有。照片是多出来的。多出来的方式，和后来页边上那一行一样。", "S12C", flags=["R_PHOTO"], exclude=["R_PHOTO"], require_clues=["K13"]),
        _choice("O12d", "春日在八月二十日想要一个异世界人。今天下午，这个世界照着那一页做出了一个——连同“我从另一个世界来”的记忆一起。", "话说出口以后，屋里很安静。没有人说我错了。阿虚看向长门。长门没有移开视线。笔帽仍对着我。空着的那一行留给零点，不留给反驳。", "S13", require_clues=["K01", "K03", "K04", "K05", "K06", "K07", "K08", "K09"], flags=["P_INFERRED_ORIGIN"]),
    ]),
    _scene("S13", "零点之前", _t(prose.S13, prose.EXTRAS["S13"]), [
        _go("O13a", "我问：如果你们回去，我会怎么样？", "古泉说，这个八月是为了我才分出来的。五个人一走，它就没有继续下去的理由，会在零点前后合上，我也在里面。长门补了另外两种可能。阿虚听完，把笔拿起来，仍先不写。", "S13M", clues=["K10"], flags=["P_ASKED_RETURN"]),
        _go("O13b", "我问：如果你们不回去，会怎么样？", "长门说，零点一过，这个八月就会变成真正的九月，他们五个再也回不去。原来的世界里，他们从八月三十一日起消失。朝比奈小声补了第三种。阿虚把笔拿起来，仍先不写。", "S13M", clues=["K10"], flags=["P_ASKED_STAY"]),
    ], variants=[
        _variant("古泉说：“下午那一步，我已经道过歉。”", require=["A_SORRY"]),
        _variant("古泉说：“下午我该当时就说对不起。”", require=["A_LATER"]),
        _variant("古泉说：“别告诉团长。这句话我还是得再说一遍。”", require=["A_BLOCK"]),
        _variant("古泉看了一眼已经收起的手机，没有再道歉。", require=["A_POCKET"]),
        _variant("古泉说：“傍晚我就看见时长在增加，没把数字提前给你。因为里面有一件事很难开口。”", require=[], exclude=["A_SORRY", "A_LATER", "A_BLOCK", "A_POCKET"]),
    ]),
    _scene("S13M", "三条", _t(longer.S13M, more.S13M, more3.S13M), [
        _go("O13m1", "我看着他把第一笔描深，不替他选词。", "浅的那一笔被他描深以后，就不再像 20 号的勾。他要这两件事分开。三条写完，纸推到我手边。他的手松开。", "S14", handouts=["H04"], flags=["P_WATCHED_WRITE"]),
        _go("O13m2", "我问朝比奈：窗口开过以后，拖把还在不在。", "“我不敢保证。”她说，“我保证的是五个人能过去。拖把是家具。你不是。”她把装置从门上拿下来，没有按。纸在这个时候被推到我手边。", "S14", handouts=["H04"], flags=["P_ASK_MOP"]),
    ]),
    _scene("S14", "回到铁皮柜前", _t(prose.S14, prose.EXTRAS["S14"]), [
        _go("O14p1", "我先看那张纸，不看门。", "三条都在。字是深的。深的字不再装成浅勾。春日还在讲风。风从楼上传下来，是凉的。", "S14L", flags=["P_READ_PAPER"]),
        _go("O14p2", "我先看柜门，不看纸。", "插销是开着的。门锁凉了。潮气还在门轴上。下午这里是热的。朝比奈站在插销旁边，口袋里的方形随着呼吸动。", "S14L", flags=["P_READ_DOOR"]),
    ], _picture(
        (DARK_GRAY, "■ ■ ■ ■ ■"),
        (DARK_GRAY, "■       ■   ■"),
        (DARK_GRAY, "■     ■ ■   ■"),
        (YELLOW, "■       ■   ■"),
        (DARK_GRAY, "■ ■ ■ ■ ■"),
    ), variants=[
        _variant("折叠椅在楼上。空间里那把空着的轮廓，不在这五把椅子里。", require=["P_HEARD_CHAIR"]),
        _variant("折叠椅在楼上。他下午没说完的那把，现在仍没有人坐。", require=["A_CHAIR"], exclude=["P_HEARD_CHAIR"]),
        _variant("他在春日离开以后补过空椅子。那把椅子现在不在这间屋里。", require=["A_LOOKED"], exclude=["P_HEARD_CHAIR", "A_CHAIR"]),
    ]),
    _scene("S14L", "还等什么", _t(longer.S14L, more.S14L, more3.S14L), [
        _choice("O14a", "我请朝比奈打开柜门，送他们回去。", "朝比奈看了我很久，点了点头。阿虚把那张纸展开，翻到第一条，放在我手边。春日的说明讲到一半，没有人接。", "S15", require_clues=["K10"], flags=["P_RETURN_PENDING"]),
        _choice("O14b", "我不开门。我们一起留在这里，等九月。", "朝比奈把手从口袋里拿了出来。装置的方形消失了。阿虚把那张纸翻到第二条，放在我手边。", "S16", require_clues=["K10"], flags=["P_STAY_PENDING"]),
        _choice("O14c", "我哪条都不选。我跟春日一起上天台，等零点。", "我接过那两根仙女棒。阿虚看着我，没有拦。长门跟在我们后面上楼，走得很慢。纸留在桌上。三条都在。没有一条被翻开。", outcome="E03", require_clues=["K10"]),
    ]),
    _scene("S15", "确认送返", _t(prose.S15, prose.EXTRAS["S15"]), [
        _choice("O15a", "我确认：送他们回去。这个八月合上，我也在里面。", "我点了头。朝比奈拧开柜门。门后不是拖把和水桶，是一片很亮的八月。", outcome="E01", require_clues=["K10"], require_flags=["P_RETURN_PENDING"]),
        _choice("O15b", "我还要再想一想。", "朝比奈把手从把手上拿开：“还有时间。”阿虚看了一眼挂钟，没说还剩多少。", "S14", require_flags=["P_RETURN_PENDING"], exclude_flags=["P_RETURN_HESITATED"], flags=["P_RETURN_HESITATED"]),
    ], variants=[
        _variant("15:16 的那张照片还在相册里。拍的时候，柜门是从里面看见的。", require=["P_K13"]),
        _variant("车票上的站名我还读得出。这间屋子里没有第二个人读得出。", require=["P_CITY"]),
    ]),
    _scene("S16", "确认留下", _t(prose.S16, prose.EXTRAS["S16"]), [
        _choice("O16a", "我确认：我们留下，一起过九月。", "我把那张纸折好，收进口袋。朝比奈轻轻吐出一口气，走到柜门前，替它扣上了插销。", outcome="E02", require_clues=["K10"], require_flags=["P_STAY_PENDING"]),
        _choice("O16b", "我还要再想一想。", "长门说：“我等。”她说完就站着不动，连书都没有翻。", "S14", require_flags=["P_STAY_PENDING"], exclude_flags=["P_STAY_HESITATED"], flags=["P_STAY_HESITATED"]),
    ]),
]

OUTCOMES = [
    {"id": "E01", "title": "送他们回八月", "delete_files": True, "text": prose.E01.strip(), "variants": [
        _variant("朝比奈鞠躬，眼睛看着地面。", require=["A_HIDE"]),
        _variant("朝比奈鞠躬，眼睛看着我。", require=[], exclude=["A_HIDE"]),
        _variant("阿虚先进去，没有回头。", require=["A_FAR"]),
        _variant("阿虚在门口停了一下，才进去。", require=["A_GUARD"]),
        _variant("阿虚问：“那句『不止一次』，我还会记得吗。”说完他进去了。", require=["A_ASK"]),
        _variant("阿虚问：“你是随口说的？”他等我摇头，才进去。", require=["A_WORRY"]),
        _variant("古泉没有笑。“谢谢你。”", require=["A_SORRY"]),
        _variant("古泉到了柜门前才说：“下午那一步，我该当时就道歉。”", require=["A_LATER"]),
        _variant("古泉说：“别告诉团长。”他留在春日旁边，最后才走进去。", require=["A_BLOCK"]),
        _variant("古泉看了一眼手机，收起来，没有跟我告别。", require=["A_POCKET"]),
        _variant("古泉站在春日那边，没有单独跟我说话。", require=["A_SIDE"], exclude=["A_SORRY", "A_LATER"]),
        _variant("古泉对我点了一下头。", require=["A_SMILE"], exclude=["A_SORRY", "A_LATER"]),
        _variant("古泉留在春日旁边。笑不在。", require=["A_COLD"], exclude=["A_BLOCK", "A_POCKET"]),
        _variant("春日把我的袖子放开，把臂章扶正：“九月不许迟到。”", require=["A_CLING"]),
        _variant("春日说：“缺考的人，九月补考。”", require=["A_EXAM", "A_ABSENT"]),
        _variant("春日说：“考生，九月也要到。”", require=["A_EXAM"], exclude=["A_ABSENT"]),
        _variant("长门把夹着时间的书放进我手里。", require=["A_SHOW"]),
        _variant("长门把夹着时间的书放进我手里。", require=["A_POINTED"], exclude=["A_SHOW"]),
        _variant("长门把书放在桌上，没有递到我手上。", require=["A_NSHOW"], exclude=["A_POINTED"]),
        _variant("桌上那只杯子还在。外圈的干痕比内圈更白。", require=["P_CUP_RING"]),
        _variant("朝比奈进门前看了一眼满壶。壶不在了。杯子还在。", require=["P_CUP_ASK"]),
        _variant("我掌心那根红线没有带进八月。它留在这只手里。", require=["P_DRAWER"]),
        _variant("我最后看了一眼这间屋子。桌上五只扣着的杯子，和一只口朝上的。", require=["P_BASELINE_EYES"]),
        _variant("我拿出手机。屏幕上是 00:00，然后一格一格暗了下去。15:16 那张照片暗在最后。", require=["P_BASELINE_SCREEN"]),
    ]},
    {"id": "E02", "title": "九月一日", "delete_files": False, "text": prose.E02.strip(), "variants": [
        _variant("零点前，春日拉着我上天台。", require=["A_CLING"]),
        _variant("夜市那次她走回来抓过我的袖子。零点她又抓了一次。", require=["A_CLING", "A_SKIP_FISH"]),
        _variant("她仍叫我考生。", require=["A_EXAM"], exclude=["A_ABSENT"]),
        _variant("她先问：“还缺不缺考？”然后才把计划贴上柜门。", require=["A_ABSENT"]),
        _variant("阿虚把夜市里没说完的既视感，留到九月一日的放学才说完。", require=["A_WENT"]),
        _variant("药局的水泥下面有没有潮气，没有人再揭。老板说的昨天，九月里没有第二个人提起。", require=["P_STALL"]),
        _variant("我抬头看了看天台上的人。六个，一个不少。", require=["P_BASELINE_EYES"]),
        _variant("后来我的手机有了信号。屏幕上的日期是 2009 年 9 月 1 日。相册里那张 15:16 还在，年份对不上任何一天。", require=["P_BASELINE_SCREEN"]),
        _variant("抽屉我九月又拉开过一次。空的。拉手的缺口还在。", require=["P_DRAWER"]),
    ]},
    {"id": "E03", "title": "又一个八月十七日", "delete_files": False, "text": prose.E03.strip(), "variants": [
        _variant("长门的书是开着的。页边有一个比上次更深的点。", require=["A_SHOW"]),
        _variant("长门的书是开着的。", require=["A_POINTED"], exclude=["A_SHOW"]),
        _variant("长门的书合着。", require=["A_NSHOW"], exclude=["A_POINTED"]),
        _variant("“今天一定会来”之前，她先看了一眼空日历。这句话她在天台上已经说过一次。", require=["A_TOLD"]),
        _variant("我看清了屋里的每一个人。和上一次一样，五个人，五种反应。多出来的只有那只已经倒好的杯子。", require=["P_BASELINE_EYES"]),
        _variant("我低头看手机：2026 年 8 月 31 日，15:17。它还不知道过去了多久。", require=["P_BASELINE_SCREEN"]),
    ]},
]


def _index(items, label):
    found = {}
    for item in items:
        item_id = item.get("id", "")
        if not item_id or item_id in found:
            raise RuntimeError(f"{label} id 为空或重复：{item_id}")
        found[item_id] = item
    return found


def validate():
    scenes = _index(SCENES, "场景")
    clues = _index(CLUES, "线索")
    handouts = _index(HANDOUTS, "手稿")
    outcomes = _index(OUTCOMES, "结局")
    if START_SCENE not in scenes:
        raise RuntimeError(f"起始场景不存在：{START_SCENE}")
    seen = set()
    for scene in SCENES:
        if not scene["choices"]:
            raise RuntimeError(f"场景 {scene['id']} 没有选项。")
        for choice in scene["choices"]:
            if choice["id"] in seen:
                raise RuntimeError(f"选项 id 重复：{choice['id']}")
            seen.add(choice["id"])
            if choice["next"] is not None and choice["next"] not in scenes:
                raise RuntimeError(f"选项 {choice['id']} 的场景不存在。")
            if choice["outcome"] is not None and choice["outcome"] not in outcomes:
                raise RuntimeError(f"选项 {choice['id']} 的结局不存在。")
            for clue_id in choice["require_clues"] + choice["clues"]:
                if clue_id not in clues:
                    raise RuntimeError(f"选项 {choice['id']} 的线索不存在：{clue_id}")
            for handout_id in choice["handouts"]:
                if handout_id not in handouts:
                    raise RuntimeError(f"选项 {choice['id']} 的手稿不存在：{handout_id}")
    for outcome in OUTCOMES:
        if outcome["delete_files"] and outcome["id"] != "E01":
            raise RuntimeError("只有送返结局 E01 可以请求清理程序文件。")
    return scenes, clues, handouts, outcomes

