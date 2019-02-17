#!/bin/python3

# Instruction Decoder & Loader
# PPASM -> PPAPI

import sys  # only for sys.exit()
import ppapi as api

# Stretch Goal Ops:
#     putc src
#     getc dst
#     jmp jmp
#     jeq/jne/jlt/jgt/jle/jge jmp,dst,src
#     eq/ne/lt/gt/le/ge dst,src
#     dump

# PPCPU Page Index
pages = {
    "mem1" : 0,
    "mem2" : 1,
    "reg"  : 2,
    "asm"  : 3,
    "succ" : 4,
    "pred" : 5,
    "add"  : 6,
    "sub"  : 7,
}


class PPEXE(object):

    def __init__():
        self.ppt = None
        pass

    def load_instructions():
        ''' Read in ppasm instructions from pptx slide '''
        pass

    def execute_instructions():
        ''' Execute commands until end of ppasm instruction list '''
        pass

    def mov(dst,src):
        val = api.reg_read(self.ppt, dst)
        api.reg_write(self.ppt, dst, val)

    def add(dst,src):
        a = api.reg_read(self.ppt, dst)
        b = api.reg_read(self.ppt, src)

        a = format(a, 'b')
        b = format(b, 'b')

        pass

    def sub(dst,src):
        a = api.reg_read(self.ppt, dst)
        b = api.reg_read(self.ppt, src)


        pass

    def load(dst,src):
        val = api.reg_read(self.ppt, src)  # todo: src could be mem. write isreg()
        api.reg_write(self.ppt, dst, val)

    def store(src,dst):
        val = api.reg_read(self.ppt, src)  # todo: src could be mem. write isreg()
        api.reg_write(self.ppt, dst, val)

    def exit():
        sys.exit()
}

if __name__ == "__main__":
    pass
