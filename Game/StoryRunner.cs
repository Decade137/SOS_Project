using System.Text;
using System.Text.RegularExpressions;
using System.Threading;

namespace SOS_Project;

internal sealed class StoryRunner
{
    internal const int SendBackCleanupResult = 2;
    private const int TextDelayMilliseconds = 20;
    private const ConsoleColor FrameColor = ConsoleColor.Red;

    private static readonly Regex Placeholder = new(@"\{\{([A-Z0-9_]+)\}\}");
    private readonly record struct MenuOption(string Key, string Text, bool Enabled = true);
    private sealed class FrameLine
    {
        internal string Text { get; set; } = string.Empty;
        internal ConsoleColor Color { get; }

        internal FrameLine(ConsoleColor color)
        {
            Color = color;
        }
    }

    private readonly Story story;
    private readonly SaveStore saves;
    private readonly Dictionary<string, Scene> scenes;
    private readonly Dictionary<string, Clue> clues;
    private readonly Dictionary<string, Handout> handouts;
    private readonly Dictionary<string, Outcome> outcomes;
    private readonly List<FrameLine> frameLines = [];
    private bool fixedFrameOpen;
    private string fixedFrameSection = string.Empty;
    private string fixedFrameTitle = string.Empty;
    private int fixedFrameHeight;
    private int fixedContentTop;
    private int fixedContentHeight;
    private int fixedOptionTop;
    private int fixedOptionHeight;

    internal StoryRunner(Story story, SaveStore saves)
    {
        this.story = story;
        this.saves = saves;
        scenes = Index(story.Scenes, scene => scene.Id, "场景");
        clues = Index(story.Clues, clue => clue.Id, "线索");
        handouts = Index(story.Handouts, handout => handout.Id, "手稿");
        outcomes = Index(story.Outcomes ?? [], outcome => outcome.Id, "结局");
        ValidateStory();
    }

    internal int Run()
    {
        var state = ChooseState(out var isNewGame);
        if (state is null)
        {
            return 0;
        }

        if (isNewGame)
        {
            ShowPage("序章", "夏末的门", framed: true);
            Print(story.Hook, state, framed: true);
            WriteBoxBottom();
            saves.Save(state);
            WaitForEnter();
        }

        var cleanupConfirmedThisRun = false;
        while (true)
        {
            if (state.CompletedOutcomeId is not null)
            {
                var outcome = outcomes[state.CompletedOutcomeId];
                ShowPage("结局", outcome.Title, framed: true);
                Print(outcome.Text, state, framed: true);
                PrintVariants(outcome.Variants, state, framed: true);
                WriteBoxBottom();
                WaitForEnter("Enter 结束");
                return outcome.DeleteOwnFilesAfterExit && cleanupConfirmedThisRun
                    ? SendBackCleanupResult
                    : 0;
            }

            var scene = scenes[state.CurrentSceneId];
            ShowScene(scene, state);

            while (true)
            {
                var available = scene.Choices.Where(choice => Available(choice, state)).ToArray();
                if (available.Length == 0)
                {
                    throw new InvalidOperationException($"场景 {scene.Id} 没有可选项。");
                }

                var menu = new MenuOption[available.Length + 2];
                for (var index = 0; index < available.Length; index++)
                {
                    menu[index] = new((index + 1).ToString(), available[index].Text);
                }
                menu[^2] = new("0", "重读已发现的线索与手稿");
                menu[^1] = new("Q", "保存并退出");

                var input = ChooseOption(menu, available.Length, scene.Title);
                if (input is null || input == "Q")
                {
                    return 0;
                }

                if (input == "0")
                {
                    ShowJournal(state);
                    WaitForEnter();
                    ShowScene(scene, state, animate: false);
                    continue;
                }

                var choice = available[int.Parse(input) - 1];
                if (choice.NextOutcomeId == "E01")
                {
                    if (scene.Id != "S15" || choice.Id != "O15a" ||
                        !state.Flags.Contains("P_RETURN_PENDING") || !state.FoundClues.Contains("K10"))
                    {
                        throw new InvalidOperationException("送返结局缺少两次确认。");
                    }
                    cleanupConfirmedThisRun = true;
                }

                Apply(choice, state);
                if (state.CompletedOutcomeId != "E01")
                {
                    saves.Save(state);
                }
                WaitForEnter();
                break;
            }
        }
    }

    private GameState? ChooseState(out bool isNewGame)
    {
        isNewGame = false;
        var hasSave = saves.Exists;
        var corrupted = false;
        string? saveError = null;
        while (true)
        {
            ShowPage("开始", "一个夏末的故事");
            var indent = Indent();
            Console.WriteLine(saveError is not null
                ? $"{indent}{saveError} 新游戏会覆盖现有文件。"
                : hasSave
                    ? $"{indent}已发现存档。新游戏会覆盖现有进度。"
                    : $"{indent}请选择旅程的起点。");
            Console.WriteLine($"{indent}阅读时任意键可补完文字。");
            var menu = new[]
            {
                new MenuOption("1", "新游戏"),
                new MenuOption("2", hasSave && !corrupted ? "读存档" : "读存档  ·  暂不可用", hasSave && !corrupted),
                new MenuOption("3", "退出")
            };
            var input = ChooseOption(menu);
            if (input is null or "3")
            {
                return null;
            }

            if (input == "1")
            {
                isNewGame = true;
                return NewState();
            }

            if (input == "2")
            {
                try
                {
                    var state = saves.Load();
                    ValidateState(state);
                    return state;
                }
                catch (InvalidDataException error)
                {
                    corrupted = true;
                    saveError = error.Message;
                }
            }
        }
    }

    private string? ChooseOption(MenuOption[] options, int primaryCount = int.MaxValue,
        string? sceneTitle = null)
    {
        if (fixedFrameOpen && SupportsFixedLayout())
        {
            return ChooseFixedOption(options, primaryCount);
        }

        var indent = Indent();
        if (Console.IsInputRedirected || Console.IsOutputRedirected)
        {
            Console.WriteLine();
            WriteBoxTop("玩家选项");
            WriteBoxLine("");
            for (var index = 0; index < options.Length; index++)
            {
                if (index == primaryCount)
                {
                    WriteBoxLine("");
                    WriteBoxLine("  ·  其他");
                }
                var option = options[index];
                foreach (var line in BuildChoiceLines(option))
                {
                    WriteBoxLine(line, option.Enabled ? ConsoleColor.Gray : ConsoleColor.DarkGray);
                }
            }
            WriteBoxLine("");
            WriteBoxLine("  输入选项文字后按 Enter 确认");
            WriteBoxBottom();
            while (true)
            {
                Console.Write($"{indent}输入选项文字 > ");
                var input = Console.ReadLine()?.Trim();
                if (input is null)
                {
                    return null;
                }
                var match = Array.FindIndex(options, option =>
                    option.Enabled && (string.Equals(option.Key, input, StringComparison.OrdinalIgnoreCase) ||
                        string.Equals(option.Text, input, StringComparison.Ordinal)));
                if (match >= 0)
                {
                    return options[match].Key;
                }
                Console.WriteLine($"{indent}请输入可选的选项文字。");
            }
        }

        while (Console.KeyAvailable)
        {
            Console.ReadKey(intercept: true);
        }
        var selected = Array.FindIndex(options, option => option.Enabled);
        var positions = new int[options.Length];
        var rendered = new string[options.Length][];
        var originalColor = Console.ForegroundColor;
        for (var index = 0; index < options.Length; index++)
        {
            rendered[index] = BuildChoiceLines(options[index]);
        }
        var menuHeight = 7 + rendered.Sum(lines => lines.Length) +
            (primaryCount < options.Length ? 2 : 0);
        if (menuHeight >= Console.WindowTop + Console.WindowHeight - Console.CursorTop)
        {
            if (menuHeight + 5 >= Console.WindowHeight)
            {
                return ChooseCompactOption(options, sceneTitle);
            }
            ShowPage("选择", sceneTitle ?? "接下来");
        }

        Console.WriteLine();
        WriteBoxTop("玩家选项");
        WriteBoxLine("");
        for (var index = 0; index < options.Length; index++)
        {
            if (index == primaryCount)
            {
                WriteBoxLine("");
                WriteBoxLine("  ·  其他");
            }
            positions[index] = Console.CursorTop;
            var option = options[index];
            Console.ForegroundColor = !option.Enabled ? ConsoleColor.DarkGray
                : index == selected ? ConsoleColor.Cyan : ConsoleColor.Gray;
            foreach (var line in rendered[index])
            {
                WriteBoxLine(line, !option.Enabled ? ConsoleColor.DarkGray
                    : index == selected ? ConsoleColor.Cyan : ConsoleColor.Gray);
            }
            Console.ForegroundColor = originalColor;
        }
        WriteBoxLine("");
        WriteBoxLine("  W/S 或 ↑↓ 选择   ·   Enter 确认");
        WriteBoxBottom();
        var bottom = Console.CursorTop;

        void Recolor(int index, ConsoleColor color)
        {
            for (var lineIndex = 0; lineIndex < rendered[index].Length; lineIndex++)
            {
                Console.SetCursorPosition(0, positions[index] + lineIndex);
                WriteBoxLine(rendered[index][lineIndex], color);
            }
        }

        while (true)
        {
            var key = Console.ReadKey(intercept: true).Key;
            if (key == ConsoleKey.Enter)
            {
                return options[selected].Key;
            }

            var direction = key switch
            {
                ConsoleKey.W or ConsoleKey.UpArrow => -1,
                ConsoleKey.S or ConsoleKey.DownArrow => 1,
                _ => 0
            };
            if (direction == 0)
            {
                continue;
            }
            var next = selected;
            do
            {
                next = (next + direction + options.Length) % options.Length;
            }
            while (!options[next].Enabled);
            if (next == selected)
            {
                continue;
            }
            Recolor(selected, ConsoleColor.Gray);
            Recolor(next, ConsoleColor.Cyan);
            Console.SetCursorPosition(0, bottom);
            selected = next;
        }
    }

    private string ChooseCompactOption(MenuOption[] options, string? sceneTitle)
    {
        var selected = Array.FindIndex(options, option => option.Enabled);
        while (true)
        {
            Console.Clear();
            var indent = Indent();
            Console.WriteLine($"{indent}◇  {sceneTitle ?? "选择"}  ·  {selected + 1}/{options.Length}");
            Console.WriteLine();
            WriteBoxTop("玩家选项");
            WriteBoxLine("");
            foreach (var line in BuildChoiceLines(options[selected]))
            {
                WriteBoxLine(line, ConsoleColor.Cyan);
            }
            WriteBoxLine("");
            WriteBoxLine("  W/S 或 ↑↓ 选择   ·   Enter 确认");
            WriteBoxBottom();

            var key = Console.ReadKey(intercept: true).Key;
            if (key == ConsoleKey.Enter)
            {
                return options[selected].Key;
            }
            var direction = key switch
            {
                ConsoleKey.W or ConsoleKey.UpArrow => -1,
                ConsoleKey.S or ConsoleKey.DownArrow => 1,
                _ => 0
            };
            if (direction == 0)
            {
                continue;
            }
            do
            {
                selected = (selected + direction + options.Length) % options.Length;
            }
            while (!options[selected].Enabled);
        }
    }

    private string? ChooseFixedOption(MenuOption[] options, int primaryCount)
    {
        while (Console.KeyAvailable)
        {
            Console.ReadKey(intercept: true);
        }

        var selected = Array.FindIndex(options, option => option.Enabled);
        RenderFixedOptions(options, primaryCount, selected);
        while (true)
        {
            var key = Console.ReadKey(intercept: true).Key;
            if (key == ConsoleKey.Enter)
            {
                return options[selected].Key;
            }

            var direction = key switch
            {
                ConsoleKey.W or ConsoleKey.UpArrow => -1,
                ConsoleKey.S or ConsoleKey.DownArrow => 1,
                _ => 0
            };
            if (direction == 0)
            {
                continue;
            }

            var next = selected;
            do
            {
                next = (next + direction + options.Length) % options.Length;
            }
            while (!options[next].Enabled);
            if (next == selected)
            {
                continue;
            }

            selected = next;
            RenderFixedOptions(options, primaryCount, selected);
        }
    }

    private static string[] BuildChoiceLines(MenuOption option)
    {
        var indent = Indent();
        return Wrap($"·  {option.Text}", $"{indent}  ", $"{indent}     ", BoxRightColumn())
            .Select(line => line[indent.Length..])
            .ToArray();
    }

    private void RenderFixedOptions(MenuOption[] options, int primaryCount, int selected)
    {
        var lines = new List<(string Text, ConsoleColor Color)>();
        lines.Add((string.Empty, ConsoleColor.Gray));
        for (var index = 0; index < options.Length; index++)
        {
            if (index == primaryCount)
            {
                lines.Add((string.Empty, ConsoleColor.Gray));
                lines.Add(("  ·  其他", ConsoleColor.Gray));
            }

            var option = options[index];
            var color = !option.Enabled ? ConsoleColor.DarkGray
                : index == selected ? ConsoleColor.Cyan : ConsoleColor.Gray;
            lines.AddRange(BuildChoiceLines(option).Select(line => (line, color)));
        }

        lines.Add((string.Empty, ConsoleColor.Gray));
        lines.Add(("  W/S 或 ↑↓ 选择   ·   Enter 确认", ConsoleColor.Gray));

        var availableRows = Math.Max(1, fixedOptionHeight - 3);
        if (lines.Count > availableRows)
        {
            var option = options[selected];
            var selectedLines = BuildChoiceLines(option)
                .Select(line => (line, ConsoleColor.Cyan))
                .ToList();
            lines =
            [
                (string.Empty, ConsoleColor.Gray),
                .. selectedLines,
                (string.Empty, ConsoleColor.Gray),
                ($"  {selected + 1}/{options.Length}    W/S 或 ↑↓ 选择   ·   Enter 确认", ConsoleColor.Gray)
            ];
        }

        WriteBoxBorderAt(fixedOptionTop, '╔', '═', '╗');
        WriteBoxLineAt(fixedOptionTop + 1, "  玩家选项");
        for (var row = 0; row < availableRows; row++)
        {
            var line = row < lines.Count ? lines[row] : (string.Empty, ConsoleColor.Gray);
            WriteBoxLineAt(fixedOptionTop + 2 + row, line.Item1, line.Item2);
        }
        WriteBoxBorderAt(fixedOptionTop + fixedOptionHeight - 1, '╚', '═', '╝');
        Console.SetCursorPosition(0, Math.Min(Console.WindowHeight - 1, fixedOptionTop + fixedOptionHeight));
    }

    private GameState NewState() => new() { CurrentSceneId = story.StartSceneId };

    private void ShowPage(string section, string title, bool framed = false)
    {
        fixedFrameOpen = false;
        frameLines.Clear();
        if (!Console.IsOutputRedirected)
        {
            Console.Clear();
        }
        if (framed)
        {
            if (SupportsFixedLayout())
            {
                BeginFixedFrame(section, title);
                return;
            }

            WriteBoxBorder('╔', '═', '╗');
            WriteBoxLine($"  {story.Title}  /  {section}");
            WriteBoxLine(new string('─', BoxInnerWidth()));
            WriteBoxLine("");
            WriteBoxLine($"  ◆  {title}", ConsoleColor.Cyan);
            WriteBoxLine("");
            return;
        }
        var indent = Indent();
        Console.WriteLine($"{indent}{story.Title}  /  {section}");
        Console.WriteLine($"{indent}{new string('─', ReadingWidth() - 2)}");
        Console.WriteLine();
        var originalColor = Console.ForegroundColor;
        if (!Console.IsOutputRedirected)
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
        }
        Console.WriteLine($"{indent}◆  {title}");
        Console.ForegroundColor = originalColor;
        Console.WriteLine();
    }

    private void BeginFixedFrame(string section, string title)
    {
        fixedFrameOpen = true;
        fixedFrameSection = section;
        fixedFrameTitle = title;
        frameLines.Clear();

        var totalHeight = Console.WindowHeight;
        fixedOptionHeight = Math.Clamp(totalHeight / 3, 6, 12);
        fixedFrameHeight = totalHeight - fixedOptionHeight - 1;
        if (fixedFrameHeight < 12)
        {
            fixedFrameHeight = Math.Max(9, totalHeight - 7);
            fixedOptionHeight = Math.Max(5, totalHeight - fixedFrameHeight - 1);
        }

        fixedContentTop = 6;
        fixedContentHeight = Math.Max(1, fixedFrameHeight - fixedContentTop - 1);
        fixedOptionTop = fixedFrameHeight + 1;
        RenderFixedFrame();
    }

    private void RenderFixedFrame()
    {
        WriteBoxBorderAt(0, '╔', '═', '╗');
        WriteBoxLineAt(1, $"  {story.Title}  /  {fixedFrameSection}");
        WriteBoxLineAt(2, new string('─', BoxInnerWidth()));
        WriteBoxLineAt(3, string.Empty);
        WriteBoxLineAt(4, $"  ◆  {fixedFrameTitle}", ConsoleColor.Cyan);
        WriteBoxLineAt(5, string.Empty);

        var visibleStart = Math.Max(0, frameLines.Count - fixedContentHeight);
        for (var row = 0; row < fixedContentHeight; row++)
        {
            var lineIndex = visibleStart + row;
            var line = lineIndex < frameLines.Count
                ? frameLines[lineIndex]
                : new FrameLine(ConsoleColor.Gray);
            WriteBoxLineAt(fixedContentTop + row, line.Text, line.Color);
        }

        WriteBoxBorderAt(fixedFrameHeight - 1, '╚', '═', '╝');
        if (Console.WindowHeight > fixedOptionTop)
        {
            Console.SetCursorPosition(0, fixedOptionTop);
        }
    }

    private void AppendFixedFrameLine(string line, ConsoleColor color, bool reveal, ref bool skip)
    {
        var indent = Indent();
        var content = line.StartsWith(indent, StringComparison.Ordinal)
            ? line[indent.Length..]
            : line;
        content = FitVisual(content, BoxInnerWidth());

        var buffered = new FrameLine(color);
        frameLines.Add(buffered);
        if (frameLines.Count > fixedContentHeight)
        {
            frameLines.RemoveAt(0);
        }

        if (!reveal)
        {
            buffered.Text = content;
            RenderFixedFrame();
            return;
        }

        foreach (var rune in content.EnumerateRunes())
        {
            buffered.Text += rune.ToString();
            RenderFixedFrame();
            if (skip || Rune.IsWhiteSpace(rune))
            {
                continue;
            }
            if (Console.KeyAvailable)
            {
                Console.ReadKey(intercept: true);
                skip = true;
            }
            else
            {
                Thread.Sleep(TextDelayMilliseconds);
            }
        }
    }

    private static bool SupportsFixedLayout() =>
        !Console.IsInputRedirected && !Console.IsOutputRedirected && Console.WindowHeight >= 18;

    private void ShowScene(Scene scene, GameState state, bool animate = true)
    {
        ShowPage("剧情", scene.Title, framed: true);
        Print(scene.Text, state, animate, framed: true);
        PrintVariants(scene.Variants, state, animate, framed: true);
        PrintPicture(scene.Picture, framed: true);
        WriteBoxBottom();
    }

    private static void WaitForEnter(string prompt = "Enter 继续")
    {
        if (Console.IsInputRedirected || Console.IsOutputRedirected)
        {
            return;
        }
        while (Console.KeyAvailable)
        {
            Console.ReadKey(intercept: true);
        }
        Console.WriteLine($"{Indent()}·  {prompt}");
        while (Console.ReadKey(intercept: true).Key != ConsoleKey.Enter)
        {
        }
    }

    private void Apply(Choice choice, GameState state)
    {
        foreach (var clueId in choice.RevealedClueIds ?? [])
        {
            state.FoundClues.Add(clueId);
        }
        foreach (var handoutId in choice.GrantedHandoutIds ?? [])
        {
            state.FoundHandouts.Add(handoutId);
        }
        foreach (var flagId in choice.SetFlagIds ?? [])
        {
            state.Flags.Add(flagId);
        }
        if (choice.SetText is not null)
        {
            state.TextValues[choice.SetText.Key] = choice.SetText.Value;
        }

        ShowPage("行动", "我的选择", framed: true);
        Print(choice.Feedback, state, framed: true);
        PrintVariants(choice.FeedbackVariants, state, framed: true);
        WriteBoxBottom();

        if (choice.NextOutcomeId is not null)
        {
            state.CompletedOutcomeId = choice.NextOutcomeId;
        }
        else
        {
            state.CurrentSceneId = choice.NextSceneId!;
        }
    }

    private void ShowJournal(GameState state)
    {
        ShowPage("档案", "已发现的材料");
        if (state.FoundClues.Count == 0 && state.FoundHandouts.Count == 0)
        {
            Console.WriteLine($"{Indent()}尚无可重读的材料。");
            return;
        }

        foreach (var clue in story.Clues.Where(clue => state.FoundClues.Contains(clue.Id)))
        {
            Console.WriteLine($"{Indent()}◇  线索 · {clue.Title}");
            Print(clue.Text, state, animate: false);
        }
        foreach (var handout in story.Handouts.Where(handout => state.FoundHandouts.Contains(handout.Id)))
        {
            Console.WriteLine($"{Indent()}◇  手稿 · {handout.Title}");
            Print(handout.Text, state, animate: false);
            PrintVariants(handout.Variants, state, animate: false);
        }
    }

    private void PrintPicture(PictureLine[]? picture, bool framed = false)
    {
        if (picture is null)
        {
            return;
        }

        var originalColor = Console.ForegroundColor;
        try
        {
            foreach (var line in picture)
            {
                var prefix = framed ? $"{Indent()} " : Indent();
                foreach (var renderedLine in Wrap(line.Text, prefix, prefix,
                    framed ? BoxRightColumn() : null))
                {
                    if (framed)
                    {
                        var skip = false;
                        if (fixedFrameOpen)
                        {
                            AppendFixedFrameLine(renderedLine, line.Color, reveal: false, ref skip);
                        }
                        else
                        {
                            WriteFramedLine(renderedLine, line.Color, reveal: false, ref skip);
                        }
                    }
                    else
                    {
                        Console.ForegroundColor = line.Color;
                        Console.WriteLine(renderedLine);
                    }
                }
            }
        }
        finally
        {
            Console.ForegroundColor = originalColor;
        }
    }

    private void PrintVariants(TextVariant[]? variants, GameState state, bool animate = true,
        bool framed = false)
    {
        foreach (var variant in variants ?? [])
        {
            if (Available(variant.RequiredFlagIds, variant.ExcludedFlagIds, state))
            {
                Print(variant.Text, state, animate, framed);
            }
        }
    }

    private static bool Available(Choice choice, GameState state) =>
        (choice.RequiredClueIds ?? []).All(state.FoundClues.Contains) &&
        Available(choice.RequiredFlagIds, choice.ExcludedFlagIds, state);

    private static bool Available(string[]? requiredFlags, string[]? excludedFlags, GameState state) =>
        (requiredFlags ?? []).All(state.Flags.Contains) &&
        !(excludedFlags ?? []).Any(state.Flags.Contains);

    private void Print(string value, GameState state, bool animate = true, bool framed = false)
    {
        var rendered = Placeholder.Replace(value.Trim(), match =>
        {
            var key = match.Groups[1].Value;
            return state.TextValues.TryGetValue(key, out var replacement)
                ? replacement
                : throw new InvalidOperationException($"缺少剧情文本变量：{key}");
        });
        if (rendered.Length == 0)
        {
            return;
        }

        var reveal = animate && !Console.IsInputRedirected && !Console.IsOutputRedirected;
        var skip = false;
        foreach (var paragraph in rendered.Replace("\r\n", "\n").Split('\n'))
        {
            if (paragraph.Length == 0)
            {
                if (framed)
                {
                    if (fixedFrameOpen)
                    {
                        AppendFixedFrameLine(string.Empty, ConsoleColor.Gray, reveal: false, ref skip);
                    }
                    else
                    {
                        WriteBoxLine("");
                    }
                }
                else
                {
                    Console.WriteLine();
                }
                continue;
            }

            var dialogue = paragraph.StartsWith('“') || paragraph.Contains("：“", StringComparison.Ordinal);
            var prefix = framed
                ? $"{Indent()}{(dialogue ? "│ " : " ")}"
                : dialogue ? $"{Indent()}│ " : Indent();
            foreach (var line in Wrap(paragraph, prefix, prefix,
                framed ? BoxRightColumn() : null))
            {
                if (framed)
                {
                    var color = dialogue ? ConsoleColor.Cyan : ConsoleColor.Gray;
                    if (fixedFrameOpen)
                    {
                        AppendFixedFrameLine(line, color, reveal, ref skip);
                    }
                    else
                    {
                        WriteFramedLine(line, color, reveal, ref skip);
                    }
                    continue;
                }

                var originalColor = Console.ForegroundColor;
                if (!Console.IsOutputRedirected)
                {
                    Console.ForegroundColor = dialogue ? ConsoleColor.Cyan : ConsoleColor.Gray;
                }
                if (reveal)
                {
                    foreach (var rune in line.EnumerateRunes())
                    {
                        Console.Write(rune.ToString());
                        if (skip || Rune.IsWhiteSpace(rune))
                        {
                            continue;
                        }
                        if (Console.KeyAvailable)
                        {
                            Console.ReadKey(intercept: true);
                            skip = true;
                        }
                        else
                        {
                            Thread.Sleep(TextDelayMilliseconds);
                        }
                    }
                }
                else
                {
                    Console.Write(line);
                }
                Console.WriteLine();
                Console.ForegroundColor = originalColor;
            }
        }
        if (framed)
        {
            if (fixedFrameOpen)
            {
                AppendFixedFrameLine(string.Empty, ConsoleColor.Gray, reveal: false, ref skip);
            }
            else
            {
                WriteBoxLine("");
            }
        }
        else
        {
            Console.WriteLine();
        }
    }

    private static IEnumerable<string> Wrap(string value, string firstPrefix, string nextPrefix,
        int? rightEdge = null)
    {
        var width = rightEdge ?? (LeftMargin() + ReadingWidth());
        var line = new StringBuilder(firstPrefix);
        var used = VisualWidth(firstPrefix);
        foreach (var rune in value.EnumerateRunes())
        {
            var runeWidth = RuneWidth(rune);
            if (used + runeWidth > width && used > VisualWidth(firstPrefix))
            {
                yield return line.ToString();
                line.Clear();
                line.Append(nextPrefix);
                used = VisualWidth(nextPrefix);
            }
            line.Append(rune.ToString());
            used += runeWidth;
        }
        yield return line.ToString();
    }

    private static void WriteBoxTop(string label)
    {
        WriteBoxBorder('╔', '═', '╗');
        WriteBoxLine($"  {label}");
    }

    private void WriteBoxBottom()
    {
        if (fixedFrameOpen)
        {
            RenderFixedFrame();
            return;
        }

        WriteBoxBorder('╚', '═', '╝');
    }

    private static void WriteBoxBorder(char left, char fill, char right)
    {
        var originalColor = Console.ForegroundColor;
        try
        {
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = FrameColor;
            }
            Console.WriteLine($"{Indent()}{left}{new string(fill, BoxInnerWidth() + 2)}{right}");
        }
        finally
        {
            Console.ForegroundColor = originalColor;
        }
    }

    private static void WriteBoxBorderAt(int row, char left, char fill, char right)
    {
        var originalColor = Console.ForegroundColor;
        try
        {
            Console.SetCursorPosition(0, row);
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = FrameColor;
            }
            Console.Write($"{Indent()}{left}{new string(fill, BoxInnerWidth() + 2)}{right}");
        }
        finally
        {
            Console.ForegroundColor = originalColor;
        }
    }

    private static void WriteBoxLineAt(int row, string content, ConsoleColor contentColor = ConsoleColor.Gray)
    {
        var originalColor = Console.ForegroundColor;
        var clipped = FitVisual(content, BoxInnerWidth());
        try
        {
            Console.SetCursorPosition(0, row);
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = FrameColor;
            }
            Console.Write($"{Indent()}║ ");
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = contentColor;
            }
            Console.Write(clipped);
            Console.Write(new string(' ', BoxInnerWidth() - VisualWidth(clipped)));
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = FrameColor;
            }
            Console.Write(" ║");
        }
        finally
        {
            Console.ForegroundColor = originalColor;
        }
    }

    private static void WriteBoxLine(string content, ConsoleColor contentColor = ConsoleColor.Gray)
    {
        var originalColor = Console.ForegroundColor;
        var clipped = FitVisual(content, BoxInnerWidth());
        try
        {
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = FrameColor;
            }
            Console.Write($"{Indent()}║ ");
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = contentColor;
            }
            Console.Write(clipped);
            Console.Write(new string(' ', BoxInnerWidth() - VisualWidth(clipped)));
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = FrameColor;
            }
            Console.WriteLine(" ║");
        }
        finally
        {
            Console.ForegroundColor = originalColor;
        }
    }

    private static void WriteFramedLine(string line, ConsoleColor contentColor, bool reveal,
        ref bool skip)
    {
        var indent = Indent();
        var content = line.StartsWith(indent, StringComparison.Ordinal)
            ? line[indent.Length..]
            : line;
        content = FitVisual(content, BoxInnerWidth());
        var originalColor = Console.ForegroundColor;
        try
        {
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = FrameColor;
            }
            Console.Write($"{indent}║ ");
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = contentColor;
            }
            if (reveal)
            {
                foreach (var rune in content.EnumerateRunes())
                {
                    Console.Write(rune.ToString());
                    if (skip || Rune.IsWhiteSpace(rune))
                    {
                        continue;
                    }
                    if (Console.KeyAvailable)
                    {
                        Console.ReadKey(intercept: true);
                        skip = true;
                    }
                    else
                    {
                        Thread.Sleep(TextDelayMilliseconds);
                    }
                }
            }
            else
            {
                Console.Write(content);
            }
            Console.Write(new string(' ', BoxInnerWidth() - VisualWidth(content)));
            if (!Console.IsOutputRedirected)
            {
                Console.ForegroundColor = FrameColor;
            }
            Console.WriteLine(" ║");
        }
        finally
        {
            Console.ForegroundColor = originalColor;
        }
    }

    private static string FitVisual(string value, int maxWidth)
    {
        if (VisualWidth(value) <= maxWidth)
        {
            return value;
        }

        var builder = new StringBuilder();
        var used = 0;
        foreach (var rune in value.EnumerateRunes())
        {
            var runeWidth = RuneWidth(rune);
            if (used + runeWidth > maxWidth)
            {
                break;
            }
            builder.Append(rune.ToString());
            used += runeWidth;
        }
        return builder.ToString();
    }

    private static int BoxInnerWidth() => Math.Max(8, ReadingWidth() - 4);

    private static int BoxRightColumn() => LeftMargin() + BoxInnerWidth();

    private static int ReadingWidth() => Console.IsOutputRedirected
        ? 78
        : Math.Max(16, Math.Min(78, Console.WindowWidth - 4));

    private static int LeftMargin() => Console.IsOutputRedirected
        ? 2
        : Math.Max(2, (Console.WindowWidth - ReadingWidth()) / 2);

    private static string Indent() => new(' ', LeftMargin());

    private static int VisualWidth(string text)
    {
        var width = 0;
        foreach (var rune in text.EnumerateRunes())
        {
            width += RuneWidth(rune);
        }
        return width;
    }

    private static int RuneWidth(Rune rune)
    {
        var value = rune.Value;
        return value is >= 0x1100 and <= 0x115F or
            >= 0x2E80 and <= 0xA4CF or
            >= 0xAC00 and <= 0xD7A3 or
            >= 0xF900 and <= 0xFAFF or
            >= 0xFE10 and <= 0xFE6F or
            >= 0xFF01 and <= 0xFF60 or
            >= 0xFFE0 and <= 0xFFE6 ? 2 : 1;
    }

    private static Dictionary<string, T> Index<T>(IEnumerable<T> items, Func<T, string> idOf, string label)
    {
        var result = new Dictionary<string, T>(StringComparer.Ordinal);
        foreach (var item in items)
        {
            var id = idOf(item);
            if (string.IsNullOrWhiteSpace(id) || !result.TryAdd(id, item))
            {
                throw new InvalidOperationException($"{label} id 为空或重复：{id}");
            }
        }
        return result;
    }

    private void ValidateStory()
    {
        if (!scenes.ContainsKey(story.StartSceneId))
        {
            throw new InvalidOperationException($"起始场景不存在：{story.StartSceneId}");
        }

        foreach (var scene in story.Scenes)
        {
            if (scene.Choices.Length == 0)
            {
                throw new InvalidOperationException($"场景 {scene.Id} 没有选项。");
            }

            foreach (var choice in scene.Choices)
            {
                if ((choice.NextSceneId is null) == (choice.NextOutcomeId is null) ||
                    (choice.NextSceneId is not null && !scenes.ContainsKey(choice.NextSceneId)) ||
                    (choice.NextOutcomeId is not null && !outcomes.ContainsKey(choice.NextOutcomeId)) ||
                    (choice.RequiredClueIds ?? []).Any(id => !clues.ContainsKey(id)) ||
                    (choice.RevealedClueIds ?? []).Any(id => !clues.ContainsKey(id)) ||
                    (choice.GrantedHandoutIds ?? []).Any(id => !handouts.ContainsKey(id)))
                {
                    throw new InvalidOperationException($"选项 {choice.Id} 的剧情引用无效。");
                }
            }
        }

        if (outcomes.Values.Any(outcome => outcome.DeleteOwnFilesAfterExit && outcome.Id != "E01"))
        {
            throw new InvalidOperationException("只有送返结局 E01 可以请求清理程序文件。");
        }
    }

    private void ValidateState(GameState state)
    {
        if (!scenes.ContainsKey(state.CurrentSceneId) ||
            (state.CompletedOutcomeId is not null && !outcomes.ContainsKey(state.CompletedOutcomeId)) ||
            state.FoundClues.Any(id => !clues.ContainsKey(id)) ||
            state.FoundHandouts.Any(id => !handouts.ContainsKey(id)) ||
            (state.CurrentSceneId == "S15" && !state.Flags.Contains("P_RETURN_PENDING")) ||
            (state.CurrentSceneId == "S16" && !state.Flags.Contains("P_STAY_PENDING")))
        {
            throw new InvalidDataException("存档包含无法识别的剧情状态。");
        }

        var visibleText = new List<string> { scenes[state.CurrentSceneId].Text };
        visibleText.AddRange((scenes[state.CurrentSceneId].Variants ?? [])
            .Where(variant => Available(variant.RequiredFlagIds, variant.ExcludedFlagIds, state))
            .Select(variant => variant.Text));
        foreach (var handoutId in state.FoundHandouts)
        {
            var handout = handouts[handoutId];
            visibleText.Add(handout.Text);
            visibleText.AddRange((handout.Variants ?? [])
                .Where(variant => Available(variant.RequiredFlagIds, variant.ExcludedFlagIds, state))
                .Select(variant => variant.Text));
        }
        if (state.CompletedOutcomeId is not null)
        {
            var outcome = outcomes[state.CompletedOutcomeId];
            visibleText.Add(outcome.Text);
            visibleText.AddRange((outcome.Variants ?? [])
                .Where(variant => Available(variant.RequiredFlagIds, variant.ExcludedFlagIds, state))
                .Select(variant => variant.Text));
        }
        if (visibleText.Any(text => Placeholder.Matches(text).Cast<Match>()
            .Any(match => !state.TextValues.ContainsKey(match.Groups[1].Value))))
        {
            throw new InvalidDataException("存档缺少剧情文本变量。");
        }
    }
}
