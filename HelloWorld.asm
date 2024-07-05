; HelloWorld.asm
; Author: RedTeam Nation

; Used to tell the linker where the entry point of the application is
global _start

_start:

	; This application will use the write syscall to write to a file descriptor 
	; By default this will used 0x1 or Standard Output FD

	; The write syscall number is the digit 4 so these is what we place into eax
	; ssize_t write(int fd, const void *buf, size_t count);
	mov eax, 0x4

	; This line can be ignored as it is the FD used to write too.
	; You can change this to 0x2 or 0x3
	mov ebx, 0x1

	; We now move the next param into the ecx register
	; This will contain the message we want to write AKA the buffer
	mov ecx, string

	; We need the buffers length AKA the count that will be passed in the buffer param
	mov edx, stringLength

	; Now we can use 0x80 AKA the interupt to execte the syscall in eax
	int 0x80


	; This will print the text to the screen
	; We now want to exit the application using the exit syscall
	; void exit(int status)

	; Moving the Syscall number 1 into eax to use exit
	mov eax, 0x1

	; We now pass what exit code we want in our case 0
	mov ebc, 0x0

	; Now we can use 0x80 AKA the interupt to execte the syscall in eax
	int 0x80



	; This will create a variable called string with the text RedTeam Nation! inside of it
	string: db "RedTeam Nation!"

	; This is a short way in NASM to generate the strings length at compile time instead of hard coding it
	stringLength equ $-string


	