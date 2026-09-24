# 结构

英文 `Docs/STRUCTURE.md` 为准。本文件只复述同一批事实。

## 根目录

- `AGENTS.md`：本仓库的常驻政策。
- `README.md`：指向政策与设计约定的短说明。
- `Docs/AI_PROJECT_HANDOFF_RULES.md`：可移植的交接规范。不是本游戏的设计。
- `Docs/MEMORY.md`：仍成立的事实和决定。
- `Docs/PROCESS.md`：工作方式和会话记录。
- `Docs/STRUCTURE.md`：本目录图。
- `Docs/TODO.md`：待办。
- `Docs/GAME_DESIGN.md`：控制台循环、类似 COC 的模块约定、凉宫春日故事边界。
- `Docs/LOGS/`：长会话笔记。目前只有 `.gitkeep`。
- `.git/`：仓库元数据。不要手改。

中文镜像是同一路径加上 `.zh-CN.md`。没有 `AGENTS.zh-CN.md`。

## 功能 → 文件

- 交接政策：`AGENTS.md`，`Docs/AI_PROJECT_HANDOFF_RULES.md`
- 产品约定：`Docs/GAME_DESIGN.md`，`Docs/GAME_DESIGN.zh-CN.md`
- 仍成立的决定：`Docs/MEMORY.md`，`Docs/MEMORY.zh-CN.md`
- 下一步：`Docs/TODO.md`，`Docs/TODO.zh-CN.md`
- 运行时决定：C# 控制台，写在 `Docs/GAME_DESIGN.md`。还没有源代码目录。

`Scenarios/` 还不存在。真正开始写剧本之前不要建这个目录。用户要求实现之前，不要添加 C# 工程。

## 文档索引

- `Docs/MEMORY.md`、`Docs/PROCESS.md`、`Docs/STRUCTURE.md`、`Docs/TODO.md`
- `Docs/GAME_DESIGN.md`
- `Docs/LOGS/`
- `Docs/Reports/` 未创建。只有在产生证据文件时才添加。
