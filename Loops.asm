; Loops.asm
; Author: RedTeam Nation

; Used to tell the linker where the entry point of the application is
global _start



: This is a function in ASM
; Since ASM will run code when compiled it important for functions to be above the entry point
: If they are not and the application does not exit on its own it will start running code in the functions
HelloWorld:

	; This is the epilog
	; Keeps track of the Current Stack Pointer that the calling application was using
	; We do this do that nothing is lost when the function continues

	; This will push the contents of ebp onto the stack
	push ebp

	; Move the Current stack pointer to ebp
	mov ebp, esp


	; Now we will simply print a string
	mov eax, 0x4
	mov ecx, string
	mov edx, stringL
	int 0x80

	; Now we wnat to reverse the epilog to correct the stack pointer
	; This can be done with the leave command as done below or with the following
	; mov esp ,ebp
	; pop ebp
	leave

	; Ret will return fro the function to the calling application so code execution does not push into other sections of memory
	ret


_start:
	; We will mov  0x5 into ecx as this will be used for counting
	mov ecx, 0x5


; This will begin to be executed once the above command finishes
PrintMethod:

	; Before we call a function we want to save all of the registers and flags onto the stack so we can be in the same state after its complete

	; This will push all of the registers content to the stack
	pushad

	; This will push all of the CPU Flags to the stack
	pushfd

	; We call a function with the call command
	; Call will take the value of EIP AKA the next instruction and push it onto the stack
	; When the function uses ret it will pop this back off the stack so it can continue where it left off
	call HelloWorld

	; Now we will restore all registers and flags
	; Note that this is in opposite order this is because the stack is FIFO

	; Pop the flags off the stack and reset them to what they were
	popfd

	; Pop the registers contents off the stack and rebuild the registers
	popad


	; Now that we reset the stack we will want to loop through the code
	; We will use the loop command to do this. It will run this code until ecx is set to 0x0
	; Every time it calls loop it will issue a dec on ecx
	; Once ecx is set to 0x0 the ZF or Zero flag will be set telling the loop to quit
	loop PrintMethod


	; Exit the application

	mov eax, 0x1
	mov ebx, 0x0
	int 0x80




	string: db "RedTeam Nation", 0x0a
	stringL equ $-string

