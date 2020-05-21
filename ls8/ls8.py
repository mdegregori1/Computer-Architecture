
#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

program = sys.argv[1]

cpu = CPU()

# load sys.argv[1] (program) 
cpu.load(program)
cpu.run()