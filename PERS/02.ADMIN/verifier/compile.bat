@ECHO OFF

cl.exe /W0 /D_USRDLL /D_WINDLL verifier.cpp /MT /link /DLL /OUT:vrf.dll