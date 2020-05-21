# 01 = 🇮binary # base 2
# 0123456789 = # base 10
# 0123456789abcde = # base 15

"""
Stack = LIFO
Operations with a stack -> push and pop

R0: 12
R1: 4A
R2: 32
R3: 00
R4: 00
R5: 00
R6: 00
R7: F4  (this is the sp) -> F3 after push R0 -> F2 -> F1 -> F2 -> F3 

register on left, values on right

PUSH R0
PUSH R1
PUSH R2
POP R1
POP R2
POP R1 <--- pop on empty stack?


Need to: Keep track of the top of the stack:
1. how do i keep track of the top of the stack?
    Use a register, stack pointer (SP)
2. we need a place to store data
    Memory ->  Let's use main memory


------


Memory 

FF: 00
FE: 00
FD: 00
FC: 00
F3: 12  (from 00 to 12, because RO (12), was pushed )
F2: 32 xxx
F1: 4A <--- SP 

.
.
.
255
"""

"""
Stack is basically stack pointer

"""
# value at R7, basically (in stack)
SP = 7
# points to item in memory (RAM)
#random init

registers[SP] = 0xf4

elif instruction == "PUSH": #e.g register 3
    # decrement the sp
    register[SP] -= 1
    # copy the value from the given register into memory at address sp
    # get register number
    reg_num = memory[pc + 1]
    # get value of register 
    val = registers[reg_num]
    # store val in memory
    memory[registers[SP]] = val
    pc += 2

# Program that I want to write 

3# SAVE_REG R2, 37 -> 3 is just val of save_reg
2
37
6 #PUSH R2-> push val is 6 according to prev code
2
2 #HALT  val is 2

# VAL AT REGISTER 7 is index into memory