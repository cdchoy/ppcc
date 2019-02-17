#!/bin/python3

# Instruction Decoder & Loader
# PPASM -> PPAPI

import sys  # only for sys.exit()
from ppapi import PPAPI

# Stretch Goal Ops:
#     putc src
#     getc dst
#     jmp jmp
#     jeq/jne/jlt/jgt/jle/jge jmp,dst,src
#     eq/ne/lt/gt/le/ge dst,src
#     dump

class PPEXE(object):

    def __init__():
        self.api = PPAPI()

    def load_instructions():
        ''' Read in ppasm instructions from pptx slide '''
        pass

    def execute_instructions():
        ''' Execute commands until end of ppasm instruction list '''
        pass

    def mov(dst,src):
        val = self.api.reg_read(self.ppt, dst)
        self.api.reg_write(self.ppt, dst, val)

    def add(dst,src):
        dstr = self.api.reg_read(self.ppt, dst)
        sstr = self.api.reg_read(self.ppt, src)
        # convert int to binary string
        dstr = format(dstr, '08b')
        sstr = format(sstr, '08b')

        # write overflow flag to 0

        for i in range(1,9):    # todo: sad conditional
            a = dstr[-i]
            b = sstr[-i]
            ovr = 0 # todo: read from overflow flag

            # Write Tape

            # Execute Tape in addTM

            # Read Tape
            out = "00011"
            ovr = out[3]  # write to ovr flag
            res = out[4] + res

            # Write res to dst reg
            dstr = list(dstr)
            dstr[-i] = res
            "".join(dstr)


        # Write dstr to reg
        return

    def sub(dst,src):
        a = self.api.reg_read(self.ppt, dst)
        b = self.api.reg_read(self.ppt, src)


        pass

    def load(dst,src):
        val = self.api.reg_read(self.ppt, src)  # todo: src could be mem. write isreg()
        self.api.reg_write(self.ppt, dst, val)

    def store(src,dst):
        val = self.api.reg_read(self.ppt, src)  # todo: src could be mem. write isreg()
        self.api.reg_write(self.ppt, dst, val)

    def exit():
        sys.exit()

if __name__ == "__main__":
    p = PPEXE()
