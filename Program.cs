using System;
using System.Runtime.InteropServices;

using DInvoke.DynamicInvoke;

namespace ConsoleApp1
{
    internal class Program
    {
        
        
        static void Main(string[] args)
        {
            var si = new Win32.STARTUPINFO();
            si.cb = Marshal.SizeOf(si);

            var pa = new Win32.SECURITY_ATTRIBUTES();
            pa.nLength = Marshal.SizeOf(pa);

            var ta = new Win32.SECURITY_ATTRIBUTES();
            ta.nLength = Marshal.SizeOf(ta);

            var pi = new Win32.PROCESS_INFORMATION();

            object[] parameters =
            {
                "C:\\Windows\\System32\\notepad.exe", null, pa, ta, false, (uint)0, IntPtr.Zero,
                "C:\\Windows\\System32", si, pi
            };

            var success = (bool)Generic.DynamicAPIInvoke("kernel32.dll", "CreateProcessW",
                typeof(Win32.CreateProcessW), ref parameters);

            if (success)
            {
                pi = (Win32.PROCESS_INFORMATION) parameters[9];
                Console.WriteLine("Process created with PID: {0}", pi.dwProcessId);
            }
            else
            {
                Console.WriteLine("Failed to create process. Error code: {0}.", Marshal.GetLastWin32Error());
            }
        }
    }
}