using System.Text;

namespace SOS_Project;

internal static class Program
{
    private static int Main()
    {
        Console.OutputEncoding = Encoding.UTF8;

        try
        {
            return new StoryRunner(ZeroFloor.Create(), new SaveStore()).Run();
        }
        catch (InvalidOperationException error)
        {
            Console.Error.WriteLine($"剧情数据错误：{error.Message}");
            return 1;
        }
        catch (IOException error)
        {
            Console.Error.WriteLine($"无法读写存档：{error.Message}");
            return 1;
        }
        catch (UnauthorizedAccessException error)
        {
            Console.Error.WriteLine($"没有权限读写存档：{error.Message}");
            return 1;
        }
    }
}
