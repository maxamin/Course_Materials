@ECHO OFF

cl.exe /W0 /D_USRDLL /D_WINDLL nethelp.cpp /MT /link /DLL /OUT:nethelp.dll