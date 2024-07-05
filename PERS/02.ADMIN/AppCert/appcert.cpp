/*

 Red Team Operator course code template
 AppCert DLL template
 
 author: reenz0h (twitter: @sektor7net)
 credits: Stefan Kanthak <‍stefan‍.‍kanthak‍@‍nexgo‍.‍de‍>

*/
#include <windows.h>
#include <stdio.h>

#define STATUS_SUCCESS 0x00000000
typedef	enum	_REASON
{
	PROCESS_CREATION_QUERY   = 1,
	PROCESS_CREATION_ALLOWED = 2,
	PROCESS_CREATION_DENIED  = 3
} REASON;

extern "C" { __declspec(dllexport) NTSTATUS	NTAPI CreateProcessNotify(LPCWSTR, REASON); }

LPCWSTR	target = L"c:\\windows\\system32\\cmd.exe";


void Go(LPCWSTR lpApplicationName) {
	// put your code here
	// example:
	wchar_t msgbuf[1024];
	
	swprintf(msgbuf, 1024, L"[%s] caught!\n", lpApplicationName);
	OutputDebugStringW(msgbuf);
}

// CreateProcessNotify() is called whenever one of the below functions is called:
// CreateProcess()
// CreateProcessAsUser()
// CreateProcessWithLogon()
// CreateProcessWithToken()
NTSTATUS NTAPI CreateProcessNotify(LPCWSTR lpApplicationName, REASON enReason) {
	NTSTATUS	ntStatus = STATUS_SUCCESS;

	int r = -1;
	r = lstrcmpiW(target, lpApplicationName);

	if ( !r ) {
		Go(lpApplicationName);
	}

	return ntStatus;
}


BOOL WINAPI DllMain( HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved ) {

	switch ( fdwReason ) {
		case DLL_PROCESS_ATTACH:
						break;
		case DLL_THREAD_ATTACH:
						break;
		case DLL_THREAD_DETACH:
						break;
		case DLL_PROCESS_DETACH:
						break;
		}
	return TRUE;
}


