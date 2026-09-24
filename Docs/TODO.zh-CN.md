# 待办

英文 `Docs/TODO.md` 为准。本文件只复述同一批事实。

状态：`Not started`（未开始），`Blocked by product choice`（等产品决定），`Ready for design`（可以设计），`Ready for implementation`（可以实现），`Implemented; validation pending`（已写完，核对未完成）。

## P0

### DOC-001 交接文档与设计约定
- Status: Implemented; validation pending
- Dependencies: 无
- Current files: `AGENTS.md`、`Docs/MEMORY.md`、`Docs/PROCESS.md`、`Docs/STRUCTURE.md`、`Docs/TODO.md`、`Docs/GAME_DESIGN.md`、中文镜像、`Docs/AI_PROJECT_HANDOFF_RULES.md`
- Work: 保持英文文档与中文镜像事实一致。
- Done when: 新会话不靠猜测就能读到产品目标、模块结构和未决问题。

### DES-002 挡住第一份剧本的选择
- Status: Blocked by product choice
- Dependencies: DOC-001
- Current files: `Docs/GAME_DESIGN.md` 的未决问题，`Docs/MEMORY.md`
- Work: 第一件事件由用户决定。定下之后，记下该模块的语气说明。玩家看到的语言仍未定。已经决定：编号选项、玩家扮演自己、推理解谜、C# 控制台、偶尔用颜色画 `■`。
- Done when: 第一件事件和它的语气说明写进 `Docs/MEMORY.md` 的决定，并且 `Docs/GAME_DESIGN.md` 与之相符。只有在剧本语言也被明确推迟时，语言才可以继续留在未决里。

## P1

### DES-003 第 0 号剧本大纲
- Status: Not started
- Dependencies: DES-002
- Current files: 无。开始写的时候才在 `Scenarios/` 建文件。
- Work: 一份 Markdown 模块，填满设计约定里的每个标题。正文原创。不要引擎。
- Done when: 标题信息、主持人简报、时间线、开场、人物、地点、线索、场景、选项、结局、手稿都在。每条线索都有揭示条件。每个结论选项都写明所需线索 id。

### ENG-001 C# 控制台运行时
- Status: Not started
- Dependencies: 用户要求实现。运行时已经选定为 C# 控制台。
- Current files: 无。不要用空目录占位。
- Work: 当用户要求时，做一个 C# 控制台程序：打印一个场景的正文；仅当该场景有图时，用颜色打印 `■`；接受一次编号选择。
- Done when: 程序用已写好的文本完成这三件事。用户要求之前不开始。不添加 Unity。
