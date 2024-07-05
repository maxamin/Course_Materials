@ECHO OFF

cl.exe /W0 /D_USRDLL /D_WINDLL implantDLL.cpp /MT /link /DLL /OUT:implant.dll