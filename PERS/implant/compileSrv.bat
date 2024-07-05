@ECHO OFF

cl.exe /nologo /Ox /MT /W0 /GS- /DNDEBUG /Tcimplantsrv.cpp /link /OUT:implantsrv.exe /MACHINE:x64
