@ECHO OFF

cl.exe /W0 /D_USRDLL /D_WINDLL winspool.cpp /MT /link /DLL /OUT:winspool.drv