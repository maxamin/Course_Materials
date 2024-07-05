; Logic.asm
; Author: RedTeam Nation

; Used to tell the linker where the entry point of the application is
global _start


; SetupFunction will set ecx to 0x5 and jump to another label
SetupFunction:
	
	; Set ecx to 0x5 as our counter
	mov ecx, 0x5

	; Jump to FinalMethod for the if statement
	jmp FinalMethod



_start:

	; We will jump directly to our setup funtion
	jmp SetupFunction


; This is our print method that we can easily use to print text to the screen
Print:

	; We first setup our epilog
	push ebp
	mov ebp, esp

	; Now we will print our text to the screen
	mov eax, 0x4
	mov ecx, string
	mov edx, stringL
	int 0x80

	; We will use the leave function
	leave

	; Now we will return
	ret

FinalMethod:

	; First we want to make sure every time we preserve the alue of our counter in ecx so we push it to the stack
	puch ecx

	; Now we push our registers and flags onto the stack
	pushfd
	pushad

	; Now we call our print function
	call Print

	; We restore the registers and stack
	popfd
	popad

	; We then manually restore out ecx register
	pop ecx

	; Next we decrese it by 1
	dec ecx

	; Now we use a conditional jump to check if the ZF or Zero flag is set
	; If its not set it will jump to the label if it is it will continue to the exit
	jnz FinalMethod



	; This will create a variable called string with the text RedTeam Nation! inside of it
	string: db "RedTeam Nation!"

	; This is a short way in NASM to generate the strings length at compile time instead of hard coding it
	stringLength equ $-string


	