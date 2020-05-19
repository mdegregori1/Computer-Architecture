"""
Number Bases
------------
different "languages" for numbers

Decimal Base 10
Binary  Base 2
Hex     Base 16
Octal   Base 8
        Base 64

What does base x mean? Represents the number of digits that a numbering system has. 

specify that its binary with 0b, 0x hex

00
01
02
03
04
05
06
07
08
09
10

1234
one 1000
two 100
three 10
four 1

Binary Counting:

8, 4, 2, 1

    0 
    1
   10
   11
  100
  101
  110
  111
 1000

Value of
1101
1 + 4 + 8 = 13

Binary to Hex
-------------
4 binary digits =  1 hex digit 

Byte = 8 bits

Byte example = 11011011
conversion into hex -> base 16
1101 0011

13+3
d 3

0b11010011 = 0xd3

list can be your memory.


 


"""

# Write a program that runs programs

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3 # store a value in a register (in the LS8 called LDI)
PRINT_REG = 4 #corresponds to PRN in the LS8

#RAM -> random access memory -> list makes a lot of sense here
memory = [
    PRINT_BEEJ,
    SAVE_REG,   # SAVE R0, 37 store 37 in RO
    0, # R0 operand ("argument")
    37,# 37 operand 
    PRINT_BEEJ,
    PRINT_REG,
    0, #R0

    HALT
]
# a byte (?) -> 8 bits
register = [0] * 8 # like variables, R0-R7

# adds flexibility instead of for loop
pc = 0
# what index in memory is it?
running = True

while running:
    inst = memory[pc]
    if inst == PRINT_BEEJ:
        print("Beej!")
        pc += 1
    elif inst = SAVE_REG:
        reg_num = memory[pc + 1]
        value = memory [pc + 2]
        register[reg_num] = value
        pc += 3
    elif inst = PRINT_REG:
        reg_num = memory[pc + 1]
        value = register[reg_num]
        print(value)
        pc += 2
    elif inst == HALT:
        running = False
    else:
        print("Unknown Instruction")
        running = False 


# i dont understand the point of the register


