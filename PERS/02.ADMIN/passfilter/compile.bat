@ECHO OFF

cl.exe /W0 /D_USRDLL /D_WINDLL passfilter.cpp passfilter.def /MT /link /DLL /OUT:passfilter.dll