namespace SOS_Project;

internal sealed record Story(
    string Title,
    string Hook,
    string StartSceneId,
    Clue[] Clues,
    Handout[] Handouts,
    Scene[] Scenes,
    Outcome[]? Outcomes = null);

internal sealed record Clue(string Id, string Title, string Text);

internal sealed record Handout(string Id, string Title, string Text, TextVariant[]? Variants = null);

internal sealed record TextVariant(
    string Text,
    string[]? RequiredFlagIds = null,
    string[]? ExcludedFlagIds = null);

internal sealed record TextAssignment(string Key, string Value);

internal sealed record PictureLine(ConsoleColor Color, string Text);

internal sealed record Scene(
    string Id,
    string Title,
    string Text,
    Choice[] Choices,
    PictureLine[]? Picture = null,
    TextVariant[]? Variants = null);

internal sealed record Choice(
    string Id,
    string Text,
    string Feedback,
    string? NextSceneId,
    string[]? RevealedClueIds = null,
    string[]? GrantedHandoutIds = null,
    string[]? SetFlagIds = null,
    string[]? RequiredClueIds = null,
    string[]? RequiredFlagIds = null,
    string[]? ExcludedFlagIds = null,
    string? NextOutcomeId = null,
    TextAssignment? SetText = null,
    TextVariant[]? FeedbackVariants = null);

internal sealed record Outcome(
    string Id,
    string Title,
    string Text,
    bool DeleteOwnFilesAfterExit = false,
    TextVariant[]? Variants = null);
