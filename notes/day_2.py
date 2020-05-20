"""
Bitwise Operations
-------------------
12 = 0b1100

1100
1000
1011

1100
0110
0011

Really similar to boolean operations, and or not.

Truth Table

A B      A AND B
----------------
0 0         0
1 0         0
0 1         0
1 1         1

A B      A OR B
----------------
0 0         0
1 0         1
0 1         1
1 1         1

    11101001
  & 00001111
  -----------   AND-Mask
    00001001


    11101001
  | 00001111
  ----------- 
    11101111


Shifting 
---------
   vv
11001010
   ^^

11001010
00011000

The value ends up being 1:

00001000
and then --> 
00000100
00000010
00000001

and mask
"""

memory = [0] * 256 # no more hardcode

address = 0 
#index, loads into memory
# load the program
with open(sys.argv[1]) as f:
    for line in f:
        str_value = int(line.split("#")[0]).strip()
        if str_value = "":
            continue
        v = int(str_value, 2)
        # base two - binary
        # print(v)
        memory[address] = v
        address += 1
    # run file after
        # prints every line in the file

