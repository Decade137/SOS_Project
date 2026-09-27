using System.Text;
using System.Text.RegularExpressions;
using System.Threading;

namespace SOS_Project;

internal sealed class StoryRunner
{
    internal const int SendBackCleanupResult = 2;
    private const int TextDelayMilliseconds = 20;

    private static readonly Regex Placeholder = new(@"\{\{([A-Z0-9_]+)\}\}");

    private readonly Story story;
    private readonly SaveStore saves;
    private readonly Dictionary<string, Scene> scenes;
    private readonly Dictionary<string, Clue> clues;
    private readonly Dictionary<string, Handout> handouts;
    private readonly Dictionary<string, Outcome> outcomes;

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
        Console.WriteLine(story.Title);
        if (!Console.IsInputRedirected && !Console.IsOutputRedirected)
        {
            Console.WriteLine("文字显示时按任意键可立即补完。");
        }
        Console.WriteLine();

        var state = ChooseState(out var isNewGame);
        if (state is null)
        {
            return 0;
        }

        if (isNewGame)
        {
            Print(story.Hook, state);
            saves.Save(state);
        }

        var cleanupConfirmedThisRun = false;
        while (true)
        {
            if (state.CompletedOutcomeId is not null)
            {
                var outcome = outcomes[state.CompletedOutcomeId];
                Console.WriteLine();
                Console.WriteLine($"【{outcome.Title}】");
                Print(outcome.Text, state);
                PrintVariants(outcome.Variants, state);
                return outcome.DeleteOwnFilesAfterExit && cleanupConfirmedThisRun
                    ? SendBackCleanupResult
                    : 0;
            }

            var scene = scenes[state.CurrentSceneId];
            Console.WriteLine();
            Console.WriteLine($"【{scene.Title}】");
            Print(scene.Text, state);
            PrintVariants(scene.Variants, state);
            PrintPicture(scene.Picture);

            while (true)
            {
                var available = scene.Choices.Where(choice => Available(choice, state)).ToArray();
                if (available.Length == 0)
                {
                    throw new InvalidOperationException($"场景 {scene.Id} 没有可选项。");
                }

                var menu = new (string Key, string Text)[available.Length + 2];
                for (var index = 0; index < available.Length; index++)
                {
                    menu[index] = ((index + 1).ToString(), available[index].Text);
                }
                menu[^2] = ("0", "重读已发现的线索与手稿");
                menu[^1] = ("Q", "保存并退出");

                var input = ChooseOption(menu);
                if (input is null || input == "Q")
                {
                    return 0;
                }

                if (input == "0")
                {
                    ShowJournal(state);
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
                break;
            }
        }
    }

    private GameState? ChooseState(out bool isNewGame)
    {
        isNewGame = false;
        if (!saves.Exists)
        {
            isNewGame = true;
            return NewState();
        }

        var corrupted = false;
        while (true)
        {
            Console.WriteLine(corrupted
                ? "存档已损坏。选择新游戏会覆盖该存档。"
                : "发现本作存档。新游戏会覆盖现有进度。");
            var menu = corrupted
                ? new (string Key, string Text)[] { ("1", "新游戏"), ("2", "退出") }
                : new (string Key, string Text)[] { ("1", "继续游戏"), ("2", "新游戏"), ("3", "退出") };
            var input = ChooseOption(menu);
            if (input is null || input == (corrupted ? "2" : "3"))
            {
                return null;
            }

            if (input == (corrupted ? "1" : "2"))
            {
                isNewGame = true;
                return NewState();
            }

            if (!corrupted && input == "1")
            {
                try
                {
                    var state = saves.Load();
                    ValidateState(state);
                    return state;
                }
                catch (InvalidDataException error)
                {
                    Console.WriteLine(error.Message);
                    corrupted = true;
                }
            }
        }
    }

    private static string? ChooseOption((string Key, string Text)[] options)
    {
        Console.WriteLine();
        if (Console.IsInputRedirected || Console.IsOutputRedirected)
        {
            foreach (var option in options)
            {
                Console.WriteLine($"{option.Key}. {option.Text}");
            }
            while (true)
            {
                Console.Write("请选择：");
                var input = Console.ReadLine()?.Trim();
                if (input is null)
                {
                    return null;
                }
                var match = Array.FindIndex(options, option =>
                    string.Equals(option.Key, input, StringComparison.OrdinalIgnoreCase));
                if (match >= 0)
                {
                    return options[match].Key;
                }
                Console.WriteLine("请输入列表中的编号。");
            }
        }

        while (Console.KeyAvailable)
        {
            Console.ReadKey(intercept: true);
        }
        foreach (var option in options)
        {
            Console.WriteLine($"{option.Key}. {option.Text}");
        }
        Console.WriteLine("W/S 上下选择，Enter 确认。");
        const string prompt = "选中 > ";
        Console.Write($"{prompt}----");
        var selected = -1;
        while (true)
        {
            var key = Console.ReadKey(intercept: true).Key;
            if (key == ConsoleKey.Enter)
            {
                if (selected >= 0)
                {
                    Console.WriteLine();
                    return options[selected].Key;
                }
                continue;
            }

            var next = key switch
            {
                ConsoleKey.W or ConsoleKey.UpArrow => selected < 0 ? options.Length - 1 : Math.Max(0, selected - 1),
                ConsoleKey.S or ConsoleKey.DownArrow => selected < 0 ? 0 : Math.Min(options.Length - 1, selected + 1),
                _ => selected
            };
            if (next == selected)
            {
                continue;
            }
            selected = next;
            Console.Write($"\r{prompt}{options[selected].Key.PadRight(4)}");
        }
    }

    private GameState NewState() => new() { CurrentSceneId = story.StartSceneId };

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

        Console.WriteLine();
        Print(choice.Feedback, state);
        PrintVariants(choice.FeedbackVariants, state);

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
        Console.WriteLine();
        if (state.FoundClues.Count == 0 && state.FoundHandouts.Count == 0)
        {
            Console.WriteLine("尚无可重读的材料。");
            return;
        }

        foreach (var clue in story.Clues.Where(clue => state.FoundClues.Contains(clue.Id)))
        {
            Console.WriteLine($"【线索：{clue.Title}】");
            Print(clue.Text, state, animate: false);
        }
        foreach (var handout in story.Handouts.Where(handout => state.FoundHandouts.Contains(handout.Id)))
        {
            Console.WriteLine($"【手稿：{handout.Title}】");
            Print(handout.Text, state, animate: false);
            PrintVariants(handout.Variants, state, animate: false);
        }
    }

    private static void PrintPicture(PictureLine[]? picture)
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
                Console.ForegroundColor = line.Color;
                Console.WriteLine(line.Text);
            }
        }
        finally
        {
            Console.ForegroundColor = originalColor;
        }
    }

    private void PrintVariants(TextVariant[]? variants, GameState state, bool animate = true)
    {
        foreach (var variant in variants ?? [])
        {
            if (Available(variant.RequiredFlagIds, variant.ExcludedFlagIds, state))
            {
                Print(variant.Text, state, animate);
            }
        }
    }

    private static bool Available(Choice choice, GameState state) =>
        (choice.RequiredClueIds ?? []).All(state.FoundClues.Contains) &&
        Available(choice.RequiredFlagIds, choice.ExcludedFlagIds, state);

    private static bool Available(string[]? requiredFlags, string[]? excludedFlags, GameState state) =>
        (requiredFlags ?? []).All(state.Flags.Contains) &&
        !(excludedFlags ?? []).Any(state.Flags.Contains);

    private static void Print(string value, GameState state, bool animate = true)
    {
        var rendered = Placeholder.Replace(value.Trim(), match =>
        {
            var key = match.Groups[1].Value;
            return state.TextValues.TryGetValue(key, out var replacement)
                ? replacement
                : throw new InvalidOperationException($"缺少剧情文本变量：{key}");
        });
        if (rendered.Length > 0)
        {
            if (!animate || Console.IsInputRedirected || Console.IsOutputRedirected)
            {
                Console.WriteLine(rendered);
            }
            else
            {
                var skip = false;
                foreach (var rune in rendered.EnumerateRunes())
                {
                    Console.Write(rune.ToString());
                    if (skip)
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
                Console.WriteLine();
            }
            Console.WriteLine();
        }
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
