# 待办

英文 `Docs/TODO.md` 为准。本文件只复述同一批事实。

状态：`Not started`（未开始），`Blocked by product choice`（等产品决定），`Ready for design`（可以设计），`Ready for implementation`（可以实现），`Implemented; validation pending`（已写完，核对未完成），`Complete`（完成）。

## P0

### DOC-001 交接文档与设计约定
- Status: Complete
- Dependencies: 无
- Current files: `AGENTS.md`、`Docs/MEMORY.md`、`Docs/PROCESS.md`、`Docs/STRUCTURE.md`、`Docs/TODO.md`、`Docs/GAME_DESIGN.md`、中文镜像、`Docs/AI_PROJECT_HANDOFF_RULES.md`
- Work: 保持英文文档与中文镜像事实一致。
- Done when: 新会话不靠猜测就能读到产品目标、模块结构和未决问题（中英文交接审阅已验证）。

### DES-002 挡住第一份剧本的选择
- Status: Complete
- Dependencies: DOC-001
- Current files: `Docs/GAME_DESIGN.md` 的未决问题，`Docs/MEMORY.md`
- Work: 第一份模块选用空间路线谜、跨年代人际故事和外星 AI 观测谜。正文是虚构无名城市中的中文第一人称故事，按八阶段故事圆环推进。属性名称、数值和检定结算方式留给以后模块；本模块只用直接选项。
- Done when: 选定的故事方向和第一人称语言写入 `Docs/MEMORY.md` 与 `Docs/GAME_DESIGN.md`，并与完整剧本复核（已达到）。

## P1

### DES-003 第 0 号完整剧本
- Status: Complete
- Dependencies: DES-002
- Current files: `Scenarios/00-zero-floor.md`
- Work: 一份中文第一人称 Markdown 模块，有完整故事圆环、原创正文、双结局、线索解锁推理，以及直接选项。
- Done when: 约定章节、揭示条件、线索门槛及每拍选项齐全，已做编辑复核并试玩双结局（已达到）。

### ENG-001 C# 控制台运行时
- Status: Complete
- Dependencies: 用户已要求开始实现。运行时是 .NET 10 上的 C# 控制台。发布目标是 Windows x64 自包含单文件 exe。
- Current files: `Game/SOS_Project.csproj`、`Game/Program.cs`、`Game/Story.cs`、`Game/GameState.cs`、`Game/SaveStore.cs`、`Game/StoryRunner.cs`、`Game/OwnFileCleanup.cs`。
- Work: 源码按编号选项推进，处理线索及旗标门槛和效果，可重读已发现材料，偶尔输出彩色 `■` 画面，从单一存档继续，并处理双结局与送返结局的限定范围清理。玩家输出不含主持人笔记。
- Done when: 静态审阅确认源码符合设计约定，且获授权的 .NET 10 构建与双结局试玩验证控制台行为（已达到）。未运行自动测试套件。不添加 Unity。

### ENG-002 接入第 0 号剧本后续内容
- Status: Complete
- Dependencies: ENG-001、DES-003；接入后续内容时处理它们的核对结果。
- Current files: `Scenarios/00-zero-floor.md`、`Scenarios/ZeroFloor.Play.cs`、`Game/Story.cs`、`Game/StoryRunner.cs`。
- Work: 接入 S06—S16、其余线索和手稿、线索解锁推理与两条结局路径，不让玩家看到主持人笔记。本模块保持直接选项，按剧情进度追加手稿，避免提前剧透。
- Done when: 静态流程审阅确认双结局按文档条件及反馈可达，且获授权的程序试玩证实两条路线（已达到）。

### REL-001 Windows 单文件发布
- Status: Complete
- Dependencies: ENG-001、ENG-002，且已获得用户明确构建与发布许可。
- Current files: `Game/SOS_Project.csproj`、`README.md`、本地被忽略的产物 `Game/bin/Release/net10.0/win-x64/publish/SOS_Project.exe`。
- Work: 已构建并试玩两条路线，发布 Windows x64 自包含单文件 exe，并用临时副本验证 E01 自删。
- Done when: 已在目标平台观察 exe 和双结局的实际行为，本地发布文件可交付（已达到）。
