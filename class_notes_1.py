"""
CPU
    Executing intstructions
    Gets them out of RAM
    Registers (Like variables)
        fixed names --> R0-R7
        fixed number of them -- 8 of them
        Fixed size -- 8 bits

Memory (RAM)
    A big array of bytes
    Each memory slot has an index, a value stored at that index
    That index into memory AKA:
        pointer
        location
        address
    That's all memories holds, numbers
"""

#ex.)

memory = [
    1, #PRINT_NICK

    3, #SAVE_REG, R2, 99, register to save in, the value save there, #like LDI
    2,  #    R2
    99, #       99
    
    4, # like PRN
    2,
    2, #HALT
]

#how does the CPU know the difference between the 2's?
# it's based on index, not value

# we need to make sure the CPU ends up at the beginning of instructions
# the CPU is dumb, and if it ends up in the middle, say at the other 2, it will halt the program

register = [0] * 8

# Program counter, index into memory of the current instruction
# AKA a pointer to the current instruction
pc = 0

running = True

#We're going to write a program that steps through the array

while running:
    inst = memory[pc] # instruction register
    
    if inst == 1: # print Nick
        print("Nick")
        pc += 1

    elif inst == 2: # HALT
        running = False

    elif inst == 3: # 
        reg_num = memory[pc + 1]
        value = memory[pc + 2]

        register[reg_num] = value

        pc += 3
    
    elif inst ==4:
        reg_num = memory[pc + 1]
        print(register[reg_num])

        pc += 2

    else:
        print(f"Unknown instruction {inst}")