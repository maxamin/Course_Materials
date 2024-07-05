@ECHO OFF

cl.exe /W0 /D_USRDLL /D_WINDLL appcert.cpp appcert.def /MT /link /DLL /OUT:appcert.dll