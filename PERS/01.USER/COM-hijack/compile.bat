@ECHO OFF

cl.exe /W0 /D_USRDLL /D_WINDLL WorkFoldersShell.cpp WorkFoldersShell.def /MT /link /DLL /OUT:WrkFoldersShell.dll