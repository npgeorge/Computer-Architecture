"""CPU functionality."""

import sys
import time
import traceback

HLT = 0b00000001
LDI = 0b00000010
PRN = 0b00000111

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.sp = 0xf4
    
    def ram_read(self, address):
        return self.ram[address]
    
    def ram_write(self, val, address):
        self.ram[address] += val

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # read memory address stored in PC
        # store that result in IR
        # can just be a local variable in run
        ir = self.ram[self.pc] # instruction register

        self.pc += 1

        inst = ir & 0b1111

        #using ram_read()
        #ex.)
        # ram_read(3)

        opera_cnt = ir >> 6

        op_pos = self.pc
        opera = (self.ram_read(op_pos + i) for i in range(opera_cnt))

        op_a = self.ram_read(self.pc + 1)

        op_b = self.ram_read(self.pc + 2)

        # then, depending on op_a & op_b
        # perform action needed per the instruction

        # use and if else cascade here...

        # implement HLT
        # HLT is = 1

        running = True

        while running:
            if inst == HLT:
                running = False
            else:
                def ldi():
                    a = next(opera)
                    b = next(opera)
                    self.reg[a] = b
                def prn():
                    print(self.reg[next(opera)], end="")
                    sys.stdout.flush()
                
                self.pc += 4





