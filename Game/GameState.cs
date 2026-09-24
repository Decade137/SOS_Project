namespace SOS_Project;

internal sealed class GameState
{
    public string CurrentSceneId { get; set; } = "";

    public string? CompletedOutcomeId { get; set; }

    public HashSet<string> FoundClues { get; } = new(StringComparer.Ordinal);

    public HashSet<string> FoundHandouts { get; } = new(StringComparer.Ordinal);

    public HashSet<string> Flags { get; } = new(StringComparer.Ordinal);

    public Dictionary<string, string> TextValues { get; } = new(StringComparer.Ordinal);
}
