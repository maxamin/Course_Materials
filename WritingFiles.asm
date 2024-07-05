; WritingFiles.asm
; Author: RedTeam Nation

; Used to tell the linker where the entry point of the application is
global _start

_start:

	; First we must open the file itself and read the contents of it to the buffer
	; int open(const char * pathname, int flags, mode_t mode);

	; First move 0x5 into eax as 0x5 is the open syscall
	mov eax, 0x5
	
	; We now move the filename into ebx
	mov ebx, file

	; Now we set the mode into ecx to write only which is 1
	mov ecx, 0x1

	; We now run the syscall
	int 0x80

	; This will open the file and leave the FD or file descriptor for the open file in eax
	: We must save the FD to somewhere. We wont be using esi for this example so we can store it there
	mov esi, eax

	; Note that this will overwrite the entire file!
	; Now we want to print the text from the file onto the screen
	mov eax 0x4

	; Now we pass it what FD we want to write to in our case the file FD store in esi
	mov ebx, esi

	; We now want to pass it the buffer to read from
	mov ecx, string

	; We also want to pass it the amount of data we want to read AKA 0x400
	mov edx, strinL

	; Now we print it to the screen
	int 0x80

	; With this done we must close the file otherwise it is left open
	; This will use the close syscall at 0x6
	; int close(int fd)

	; We pass 0x6 into eax
	mov eax, 0x6

	; Now we pass the FD we want to close which sits in esi
	mov ebc, esi

	; Now we execute the syscall to close the FD
	int 0x80


	; We need to setup what the file name is we want to read
	; Make sure to have a file called test.txt in the same directory as this file when executed
	; 0x0 means \0 and is needed for the end of filenames
	file: db "./test.txt", 0x0

	; this will be the string we want to add
	string: db "This is new Text!", 0x0a
	string: equ $-string

; This section contains uninitalized data
section .bss
	; We need to create a buffer for us to store the data in a file
	; 0x400 is 1024 bytes
	buffer resb 0x400



	