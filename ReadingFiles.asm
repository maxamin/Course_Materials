; ReadingFiles.asm
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

	; Now we set the mode into ecx to read only which is 0
	mov ecx, 0x0

	; We now run the syscall
	int 0x80

	; This will open the file and leave the FD or file descriptor for the open file in eax
	: We must save the FD to somewhere. We wont be using esi for this example so we can store it there
	mov esi, eax


	; Now with the file open we need to read from the file
	; We can do this with the read syscall
	; ssize_t read(int fd, void *buffer, size_t count)

	; First we pass 0x3 into eax as that is the read syscall
	mov eax, 0x3

	; Now we pass it the file descriptor we want to read from whcih is in esi
	mov ebx, esi

	; Now we pass it the place we want the text to be store AKA our buffer
	mov  ecx, buffer

	; Now how large is the buffer that we passed? AKA 0x400
	mov edx, 0x400

	; Now we launch the read
	; After this runs the buffer will contain out text from the file
	int 0x80

	; Now we want to print the text from the buffer onto the screen
	mov eax 0x4

	; Now we pass it what FD we want to write to in our case STDOUT
	mov ebx, 0x1

	; We now want to pass it the buffer to read from
	mov ecx, buffer

	; We also want to pass it the amount of data we want to read AKA 0x400
	mov edx, 0x400

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

; This section contains uninitalized data
section .bss
	; We need to create a buffer for us to store the data in a file
	; 0x400 is 1024 bytes
	buffer resb 0x400



	