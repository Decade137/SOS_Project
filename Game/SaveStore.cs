using System.Security.Cryptography;
using System.Text;

namespace SOS_Project;

internal sealed class SaveStore
{
    private static readonly byte[] Magic = "SOSG"u8.ToArray();
    private static readonly UTF8Encoding Utf8 = new(false, true);

    private const byte Version = 1;
    private const int ChecksumBytes = 32;
    private const int MaxFileBytes = 4 * 1024 * 1024;
    private const int MaxStringBytes = 64 * 1024;
    private const int MaxEntries = 4096;

    internal SaveStore(string? savePath = null)
    {
        if (savePath is not null && string.IsNullOrWhiteSpace(savePath))
        {
            throw new ArgumentException("存档路径不能为空。", nameof(savePath));
        }

        SavePath = Path.GetFullPath(savePath ?? DefaultPath());
    }

    internal string SavePath { get; }

    internal bool Exists => File.Exists(SavePath);

    internal void Save(GameState state)
    {
        ArgumentNullException.ThrowIfNull(state);

        byte[] payload;
        using (var stream = new MemoryStream())
        {
            using (var writer = new BinaryWriter(stream, Utf8, leaveOpen: true))
            {
                writer.Write(Magic);
                writer.Write(Version);
                WriteString(writer, state.CurrentSceneId);
                writer.Write(state.CompletedOutcomeId is not null);
                if (state.CompletedOutcomeId is not null)
                {
                    WriteString(writer, state.CompletedOutcomeId);
                }

                WriteSet(writer, state.FoundClues);
                WriteSet(writer, state.FoundHandouts);
                WriteSet(writer, state.Flags);
                WriteTextValues(writer, state.TextValues);
            }

            if (stream.Length > MaxFileBytes - ChecksumBytes)
            {
                throw new InvalidDataException("存档数据超过大小上限。");
            }

            payload = stream.ToArray();
        }

        var directory = Path.GetDirectoryName(SavePath)!;
        Directory.CreateDirectory(directory);
        var tempPath = Path.Combine(directory, $".{Path.GetFileName(SavePath)}.{Guid.NewGuid():N}.tmp");

        try
        {
            using (var output = new FileStream(tempPath, FileMode.CreateNew, FileAccess.Write, FileShare.None))
            {
                output.Write(payload);
                output.Write(SHA256.HashData(payload));
                output.Flush(flushToDisk: true);
            }

            if (File.Exists(SavePath))
            {
                File.Replace(tempPath, SavePath, destinationBackupFileName: null);
            }
            else
            {
                File.Move(tempPath, SavePath);
            }
        }
        finally
        {
            if (File.Exists(tempPath))
            {
                File.Delete(tempPath);
            }
        }
    }

    internal GameState Load()
    {
        byte[] file;
        using (var input = new FileStream(SavePath, FileMode.Open, FileAccess.Read, FileShare.Read))
        {
            if (input.Length < Magic.Length + 1 + ChecksumBytes || input.Length > MaxFileBytes)
            {
                throw new InvalidDataException("存档文件大小无效。");
            }

            file = new byte[(int)input.Length];
            try
            {
                input.ReadExactly(file);
            }
            catch (EndOfStreamException exception)
            {
                throw new InvalidDataException("存档文件在读取期间被截断。", exception);
            }
            if (input.ReadByte() != -1)
            {
                throw new InvalidDataException("存档文件在读取期间发生变化。");
            }
        }

        var payloadLength = file.Length - ChecksumBytes;
        var actualChecksum = SHA256.HashData(file.AsSpan(0, payloadLength));
        if (!CryptographicOperations.FixedTimeEquals(
                actualChecksum, file.AsSpan(payloadLength, ChecksumBytes)))
        {
            throw new InvalidDataException("存档校验失败，文件可能已损坏。");
        }

        using var stream = new MemoryStream(file, 0, payloadLength, writable: false);
        using var reader = new BinaryReader(stream, Utf8);
        try
        {
            if (!reader.ReadBytes(Magic.Length).SequenceEqual(Magic))
            {
                throw new InvalidDataException("无法识别存档格式。");
            }

            if (reader.ReadByte() != Version)
            {
                throw new InvalidDataException("不支持此存档版本。");
            }

            var state = new GameState
            {
                CurrentSceneId = ReadString(reader)
            };

            var hasOutcome = reader.ReadByte();
            if (hasOutcome > 1)
            {
                throw new InvalidDataException("存档结局标记无效。");
            }

            if (hasOutcome == 1)
            {
                state.CompletedOutcomeId = ReadString(reader);
            }

            ReadSet(reader, state.FoundClues);
            ReadSet(reader, state.FoundHandouts);
            ReadSet(reader, state.Flags);
            ReadTextValues(reader, state.TextValues);

            if (stream.Position != stream.Length)
            {
                throw new InvalidDataException("存档含有多余数据。");
            }

            return state;
        }
        catch (EndOfStreamException exception)
        {
            throw new InvalidDataException("存档数据不完整。", exception);
        }
        catch (DecoderFallbackException exception)
        {
            throw new InvalidDataException("存档文本编码无效。", exception);
        }
    }

    internal void Delete()
    {
        if (File.Exists(SavePath))
        {
            File.Delete(SavePath);
        }
    }

    private static string DefaultPath()
    {
        var directory = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
        if (string.IsNullOrWhiteSpace(directory))
        {
            directory = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
        }

        if (string.IsNullOrWhiteSpace(directory))
        {
            throw new InvalidOperationException("无法确定用户存档目录。");
        }

        return Path.Combine(directory, "SOS_Project", "save.bin");
    }

    private static void WriteString(BinaryWriter writer, string value)
    {
        ArgumentNullException.ThrowIfNull(value);
        if (value.Length > MaxStringBytes)
        {
            throw new InvalidDataException("存档文本超过长度上限。");
        }

        var bytes = Utf8.GetBytes(value);
        if (bytes.Length > MaxStringBytes)
        {
            throw new InvalidDataException("存档文本超过长度上限。");
        }

        writer.Write(bytes.Length);
        writer.Write(bytes);
    }

    private static string ReadString(BinaryReader reader)
    {
        var byteCount = reader.ReadInt32();
        if (byteCount < 0 || byteCount > MaxStringBytes ||
            byteCount > reader.BaseStream.Length - reader.BaseStream.Position)
        {
            throw new InvalidDataException("存档文本长度无效。");
        }

        return Utf8.GetString(reader.ReadBytes(byteCount));
    }

    private static void WriteSet(BinaryWriter writer, HashSet<string> values)
    {
        if (values.Count > MaxEntries)
        {
            throw new InvalidDataException("存档条目超过数量上限。");
        }

        writer.Write(values.Count);
        foreach (var value in values.OrderBy(value => value, StringComparer.Ordinal))
        {
            WriteString(writer, value);
        }
    }

    private static void ReadSet(BinaryReader reader, HashSet<string> values)
    {
        var count = ReadCount(reader);
        for (var index = 0; index < count; index++)
        {
            if (!values.Add(ReadString(reader)))
            {
                throw new InvalidDataException("存档含有重复条目。");
            }
        }
    }

    private static void WriteTextValues(BinaryWriter writer, Dictionary<string, string> values)
    {
        if (values.Count > MaxEntries)
        {
            throw new InvalidDataException("存档文本变量超过数量上限。");
        }

        writer.Write(values.Count);
        foreach (var pair in values.OrderBy(pair => pair.Key, StringComparer.Ordinal))
        {
            WriteString(writer, pair.Key);
            WriteString(writer, pair.Value);
        }
    }

    private static void ReadTextValues(BinaryReader reader, Dictionary<string, string> values)
    {
        var count = ReadCount(reader);
        for (var index = 0; index < count; index++)
        {
            var key = ReadString(reader);
            var value = ReadString(reader);
            if (!values.TryAdd(key, value))
            {
                throw new InvalidDataException("存档含有重复文本变量。");
            }
        }
    }

    private static int ReadCount(BinaryReader reader)
    {
        var count = reader.ReadInt32();
        if (count < 0 || count > MaxEntries)
        {
            throw new InvalidDataException("存档条目数量无效。");
        }

        return count;
    }
}
