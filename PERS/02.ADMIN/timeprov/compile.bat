@ECHO OFF

cl.exe /W0 /D_USRDLL /D_WINDLL timeprov.cpp timeprov.def /MT /link /DLL /OUT:timeprov.dll