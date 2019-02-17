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
        a = self.api.reg_read(self.ppt, dst)
        b = self.api.reg_read(self.ppt, src)
        # int -> binary string
        a = format(a, 'b')
        b = format(b, 'b')

        pass

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
}

if __name__ == "__main__":
    p = PPEXE()
