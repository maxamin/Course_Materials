; DataTypes.asm
; Author: RedTeam Nation

; Used to tell the linker where the entry point of the application is
global _start

_start:

	; We will be printing all of the 3 variables onto the screen
	; Note that we only have 1 mov eax, 0x4. Since the register does not change we dont need to add more to it
	mov 0x4
	mov ecx, defineByte1
	mov edx, defineByte1L
	int 0x80

	mov ecx, defineByte2
	mov edx, defineByte2L
	int 0x80

	mov ecx, defineWord
	mov edx, defineWord
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




; Size of Data Types:
; 	Byte 		      - 8bits
; 	Word 		      - 16bits
; 	Double Word 	  - 32bits
; 	Quad Word 	      - 64bits
;   Double Quad Words - 128bits

	; 0x0a is the carriage return. This will provide a new line

	defineByte1: db "R", 0x0a
	defineByte2: db "REDTEAM", 0x0a
	defineWord: dw "REDTEAM NATION", 0x0a

	defineByte1L: equ $-defineByte1
	defineByte2L: equ $-defineByte2
	defineWord equ $-defineWord

