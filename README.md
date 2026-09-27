# SOS_Project

Unofficial single-player C# console text game. The player picks numbered options, plays themself, and solves deduction puzzles. Scenario modules follow a Call of Cthulhu–style TRPG structure. The fiction is the world of The Melancholy of Haruhi Suzumiya.

非官方单人 C# 控制台文字游戏。玩家选择编号选项，扮演自己，进行推理解谜。剧本模块用类似 COC 跑团的结构。故事世界是《凉宫春日的忧郁》。

- Policy: [AGENTS.md](AGENTS.md)
- Design: [Docs/GAME_DESIGN.md](Docs/GAME_DESIGN.md) · [中文](Docs/GAME_DESIGN.zh-CN.md)
- Handoff: [Docs/MEMORY.md](Docs/MEMORY.md) · [Docs/TODO.md](Docs/TODO.md)

The source contains the complete first scenario, including both endings. With the .NET 10 SDK installed, run `dotnet run --project Game/SOS_Project.csproj`. Progress is saved in `%LOCALAPPDATA%/SOS_Project/save.bin`. To publish the Windows x64 self-contained single-file game, run `dotnet publish Game/SOS_Project.csproj -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:DebugType=None -p:DebugSymbols=false`. The current W/S and text presentation has passed a Release build and single-file publish; the exe is at `Game/bin/Release/net10.0/win-x64/publish/SOS_Project.exe`. Both endings were played on the earlier version, and E01 self-deletion was verified using a disposable published copy; the current interaction has not yet been played. Build outputs are ignored by Git.

源码已接入首个剧本全篇及双结局。安装 .NET 10 SDK 后，可运行 `dotnet run --project Game/SOS_Project.csproj`。进度存于 `%LOCALAPPDATA%/SOS_Project/save.bin`。发布 Windows x64 自包含单文件游戏可运行 `dotnet publish Game/SOS_Project.csproj -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:DebugType=None -p:DebugSymbols=false`。当前 W/S 选项与逐字演出已通过 Release 构建及单文件发布；exe 位于 `Game/bin/Release/net10.0/win-x64/publish/SOS_Project.exe`。双结局曾在旧版试玩，E01 自删曾用临时发布副本验证；当前交互尚未试玩。构建产物由 Git 忽略。
