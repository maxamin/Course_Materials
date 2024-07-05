; Arithmetic.asm
; Author: RedTeam Nation

; Used to tell the linker where the entry point of the application is
global _start

_start:

	; We will now work with Additon

	; They way this works is when you perform the add the final result is located in the register you gave in the add command
	; command: add register_to_add_to, value_to_add
	
	; First we move the value of 0x55 into al or EAX's lower bits section
	mov al, 0x55

	; Next we want to add 0x10 to get a result of 0x65
	add al, 0x10

	; Now if we look at the eax register we see that the al section of the register is now set to 0x65

	; If we want to add two number that are going to be greater that 32 bits we must set the carry flag to let the CPU know it will overflow the 32 bits
	; We can set this flag with the command 'stc' which will set the carry flag
	; We can see the flags in GDB with 'info registers eflags'
	; Other commands with this flag
	; clc : clears the carry flag AKA not set
	; cmc : compliments the carry flag. Will set it if its not and unset it if it is

	; We will set a full value of 32 bits into eax
	mov eax, 0xffffffff

	; Now we will set the carry flag
	stc

	; We now need to use a special type of add called adc or add with carry otherwise we will get an overflow error
	adc eax, 0x10

	; Now we should get a value of 0xffffff11 in eax

	; -------------------------------------------------------------------
	; Now we will work with subtraction

	; We now set eax to 0 to reset our additon
	mov eax, 0x0

	; Now we move 0x20 into al
	mov al, 0x20

	; Next we want to subtract 0x5
	sub al, 0x5

	; We now see in al or EAX we get a result of 0x1b

	; The carry flag works with subtraction as well

	; We use the value 0x1b from our previous result and set the carry flag
	stc

	; Now we subtract 0x10 with the carry flag using sbb
	sbb eax, 0x10

	; We get our result of 0xa in eax

	; -------------------------------------------------------------------
	; We will now look at increasing and decreasing a value in a register

	; We will first set the value of 0x0 into eax
	mov eax, 0x0

	; Next we will want to increase by 1 eax
	inc eax

	; This will leave us with a value of 0x1 in eax

	; Now we will decrease this by 1
	dec eax

	; Now we have a value of 0x0 again in eax
	; Its important to understand that inc and dec only operate by 1 at a time



	; -------------------------------------------------------------------
	; We will now look at Multiplication
	; When multiplying #'s in ASM take the following chart into consideration.

	;	AL * 8bits = AX register
	;	AX * 16bits = DX & AX register
	;	EAX * 32bits = EDX & EAX registers

	; When the multiplication is greater than the original register it will set the carry flag(CF) & overflow flag(OF) to 1.

	; If we multiplied AL(8bits) * AH(16bits) the answer(depending on #'s in the registers) would set the carry & overflow flag an
	; push results to the AX register

	; First we set eax and ebx to 0
	mov eax, 0x0
	mov ebx, eax

	; Next we set al to be 0x10
	mov al, 0x10

	; We now set 0x5 into bl
	mov bl ,0x5

	; When we issue the mul bl for multiplation it will multiply bl or whatever you pass it why what it is al
	mul bl

	; This will result with a value of 0x50
	; The result will always end up in eax unless there is an overflow
	; If there is an overflow the Carry and Overflow Flag will be set

	; -------------------------------------------------------------------
	; We will now look at Division
	; When dividing #'s in ASM take the following chart into consideration.
	; Since this is devision no need to worry about the carry flag or overflow flag

	;	AX / 8bits = Answer in AL remainder in AH
	;	DX & AX / 16bits = Answer in AX remainder in DX
	;	EDX & EAX / 32bits = Answer in EAX remainder in EDX

	; First we set eax, edx and ecx to 0
	mov eax, 0x0
	mov edx, eax
	mov ecx, eax

	; Next we set al to be 0x10
	mov ax, 0x1000

	; We now set 0x5 into dx
	mov cx, 0x5

	; When we issue the div cx for division it will divide cx or whatever you pass it why what it is ax
	div cx

	; The value of this will be 0x333 in eax and the remainder of 0x1 in edx

	; This will print the text to the screen
	; We now want to exit the application using the exit syscall
	; void exit(int status)

	; Moving the Syscall number 1 into eax to use exit
	mov eax, 0x1

	; We now pass what exit code we want in our case 0
	mov ebc, 0x0

	; Now we can use 0x80 AKA the interupt to execte the syscall in eax
	int 0x80



	