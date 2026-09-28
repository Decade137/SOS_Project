# 结构

英文 `Docs/STRUCTURE.md` 为准。本文件只复述同一批事实。

## 根目录

- `AGENTS.md`：本仓库的常驻政策。
- `README.md`：指向政策与设计约定的短说明。
- `.gitignore`：忽略生成的 `Game/bin/`、`Game/obj/` 和根目录 `SOS_Project.exe` 产物。
- `SOS_Project.exe`：复制到仓库根目录的 Windows x64 自包含单文件发布版。
- `Docs/AI_PROJECT_HANDOFF_RULES.md`：可移植的交接规范。不是本游戏的设计。
- `Docs/MEMORY.md`：仍成立的事实和决定。
- `Docs/PROCESS.md`：工作方式和会话记录。
- `Docs/STRUCTURE.md`：本目录图。
- `Docs/TODO.md`：待办。
- `Docs/GAME_DESIGN.md`：控制台循环、类似 COC 的模块约定、凉宫春日故事边界。
- `Game/SOS_Project.csproj`：面向 `net10.0` 的控制台工程，把可玩的剧情数据编译进程序。
- `Game/Program.cs`：控制台入口。
- `Game/Story.cs`：场景、选项、线索、手稿和结局。
- `Game/GameState.cs`：当前场景、已发现材料、旗标、文本选择和已完成结局。
- `Game/SaveStore.cs`：带完整性校验的单一版本化本地存档。
- `Game/StoryRunner.cs`：独立的首页／场景／行动／档案／结局页面、内容在其中滚动刷新的固定大小 Unicode 边框、只有出现选项时才显示且位置固定的选项框、限宽正文和对白提示、圆点标记且选中项全文变色的 W/S 与 Enter 菜单、状态效果、即时重读与可选彩色画面。
- `Game/OwnFileCleanup.cs`：送返结局中限定范围的本作存档和已发布 exe 清理。
- `Scenarios/00-zero-floor.md`：已写的中文第一人称第 0 号剧本，含八阶段故事圆环与完整模块章节。
- `Scenarios/ZeroFloor.Play.cs`：编译用首个完整剧本的玩家剧情数据，涵盖开场至 S16、K01—K10、H01—H04、E01/E02。
- `Docs/LOGS/`：长会话笔记。目前只有 `.gitkeep`。
- `.git/`：仓库元数据。不要手改。

中文镜像是同一路径加上 `.zh-CN.md`。没有 `AGENTS.zh-CN.md`。

## 功能 → 文件

- 交接政策：`AGENTS.md`，`Docs/AI_PROJECT_HANDOFF_RULES.md`
- 产品约定：`Docs/GAME_DESIGN.md`，`Docs/GAME_DESIGN.zh-CN.md`
- 第一份剧本的决定：`Docs/MEMORY.md`、`Docs/GAME_DESIGN.md` 及其中文镜像。
- 第 0 号剧本正文与主持人笔记：`Scenarios/00-zero-floor.md`（中文源文件；尚无英文译本）。
- 第 0 号剧本可游玩的剧情数据：`Scenarios/ZeroFloor.Play.cs`（由 Markdown 整理而来；玩家输出不含主持人笔记）。
- 控制台程序：`Game/Program.cs`、`Game/Story.cs`、`Game/GameState.cs`、`Game/SaveStore.cs`、`Game/StoryRunner.cs`、`Game/OwnFileCleanup.cs`、`Game/SOS_Project.csproj`。
- 控制台界面、开始页与菜单输入：`Game/StoryRunner.cs`；交互约定：`Docs/GAME_DESIGN.md` 和 `Docs/GAME_DESIGN.zh-CN.md`。
- 构建产物规则：`.gitignore` 忽略生成的 `Game/bin/`、`Game/obj/` 和根目录 `SOS_Project.exe` 文件。
- 仍成立的决定：`Docs/MEMORY.md`，`Docs/MEMORY.zh-CN.md`
- 下一步：`Docs/TODO.md`，`Docs/TODO.zh-CN.md`
- 运行时决定：.NET 10 的 C# 控制台与 Windows x64 自包含单文件 exe，写在 `Docs/GAME_DESIGN.md`。源码位于 `Game/`；本地发布文件位于 `Game/bin/Release/net10.0/win-x64/publish/SOS_Project.exe`，仓库根目录另有一份 `SOS_Project.exe`。

`Scenarios/` 包含第 0 号完整剧本和编译用剧情数据。第 0 号剧本默认玩家熟悉 SOS 团及其相关故事，玩家输出通过细节、档案、时间轨迹和角色反应体现这份熟悉，不直接解释其来源。C# 工程位于 `Game/`。新的开始界面与分页排版已通过 Release 构建及 Windows x64 单文件发布。双结局与临时发布副本的 E01 自删在更早版本上验证过；新界面尚未试玩。

剧本 Markdown 与编译用剧情数据已同步修改当前文案，包括团员介绍前的外貌与动作描写；发布目录及仓库根目录的 exe 都包含这些文案，以及圆点标记、选中项全文变色与溢出处理的菜单。

## 文档索引

- `Docs/MEMORY.md`、`Docs/PROCESS.md`、`Docs/STRUCTURE.md`、`Docs/TODO.md`
- `Docs/GAME_DESIGN.md`
- `Docs/LOGS/`
- `Docs/Reports/` 未创建。只有在产生证据文件时才添加。
