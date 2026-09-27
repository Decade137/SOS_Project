using System.Diagnostics;
using System.Security.Cryptography;
using System.Text;

namespace SOS_Project;

internal static class OwnFileCleanup
{
    internal static bool AfterSendBack(SaveStore saves)
    {
        saves.Delete();

        var executable = Environment.ProcessPath;
        if (!OperatingSystem.IsWindows() || executable is null ||
            !string.Equals(Path.GetFileName(executable), "SOS_Project.exe", StringComparison.OrdinalIgnoreCase) ||
            !string.Equals(executable, Path.Combine(AppContext.BaseDirectory, "SOS_Project.exe"), StringComparison.OrdinalIgnoreCase) ||
            File.Exists(Path.ChangeExtension(executable, ".dll")))
        {
            Console.WriteLine("本作存档已删除；当前不是已发布的 Windows 单文件程序，不删除运行文件。");
            return true;
        }

        var systemDirectory = Environment.GetFolderPath(Environment.SpecialFolder.System);
        var powershell = Path.Combine(systemDirectory, "WindowsPowerShell", "v1.0", "powershell.exe");
        if (!File.Exists(powershell))
        {
            Console.Error.WriteLine($"本作存档已删除，但无法安排删除程序。请手动删除：{executable}");
            return false;
        }

        string expectedHash;
        try
        {
            using var currentFile = File.OpenRead(executable);
            expectedHash = Convert.ToHexString(SHA256.HashData(currentFile));
        }
        catch (Exception error) when (error is IOException or UnauthorizedAccessException)
        {
            Console.Error.WriteLine($"本作存档已删除，但无法核对程序文件。请手动删除：{executable}");
            return false;
        }

        var quotedPath = executable.Replace("'", "''", StringComparison.Ordinal);
        var command = $"$gameExe = '{quotedPath}'; " +
            $"$expectedHash = '{expectedHash}'; " +
            "for ($attempt = 0; $attempt -lt 300; $attempt++) { " +
            "if (-not [System.IO.File]::Exists($gameExe)) { break }; " +
            "try { " +
            "$stream = [System.IO.File]::OpenRead($gameExe); " +
            "try { $hasher = [System.Security.Cryptography.SHA256]::Create(); " +
            "try { $actualHash = [System.BitConverter]::ToString($hasher.ComputeHash($stream)).Replace('-', '') } " +
            "finally { $hasher.Dispose() } } finally { $stream.Dispose() }; " +
            "if ($actualHash -ne $expectedHash) { break }; " +
            "[System.IO.File]::Delete($gameExe); " +
            "if (-not [System.IO.File]::Exists($gameExe)) { break } " +
            "} catch {} [System.Threading.Thread]::Sleep(200) }";

        var start = new ProcessStartInfo(powershell)
        {
            UseShellExecute = false,
            CreateNoWindow = true,
            WindowStyle = ProcessWindowStyle.Hidden
        };
        start.ArgumentList.Add("-NoProfile");
        start.ArgumentList.Add("-NonInteractive");
        start.ArgumentList.Add("-EncodedCommand");
        start.ArgumentList.Add(Convert.ToBase64String(Encoding.Unicode.GetBytes(command)));

        try
        {
            using var helper = Process.Start(start);
            if (helper is null)
            {
                throw new IOException("无法启动退出后删除程序的辅助进程。");
            }
        }
        catch (Exception error) when (error is System.ComponentModel.Win32Exception or IOException or UnauthorizedAccessException)
        {
            Console.Error.WriteLine($"本作存档已删除，但无法安排删除程序。请手动删除：{executable}");
            return false;
        }

        Console.WriteLine("本作存档已删除；已安排在程序退出后尝试删除本游戏 exe。");
        return true;
    }
}
