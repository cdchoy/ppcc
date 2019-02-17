#!/bin/python3

# Instruction Decoder & Loader
# PPASM -> PPAPI

import sys  # only for sys.exit()
import win32com.client
from ppsuite import PPAPI

# Stretch Goal Ops:
#     putc src
#     getc dst
#     jmp jmp
#     jeq/jne/jlt/jgt/jle/jge jmp,dst,src
#     eq/ne/lt/gt/le/ge dst,src
#     dump

class PPEXE(object):

    _ovr_reg = 6  # overflor register for add/sub

    def __init__(self,ppt,filepath):
        self.api = PPAPI(ppt)

    def is_int(self, val):
        ''' Checks if a value in a string can be converted to int '''
        try: 
            int(val)
            return True
        except ValueError:
            return False

    def load_instructions(self):
        ''' Read in ppasm instructions from pptx slide '''
        pass

    def execute_instructions(self):
        ''' Execute commands until end of ppasm instruction list '''
        # Load instructions into PPCPU
        self.api.init_inst_cache()
        # self.api.load_ppasm(filepath)

    def mov(self,dst,src):
        if self.is_int(src):
            val = int(src)
        else:
            val = self.api.reg_read(src)

        self.api.reg_write(dst, val)

    def add(self,dst,src):
        if self.is_int(src):
            src_val = int(src)
        else:
            src_val = self.api.reg_read(src)

        dstr = self.api.reg_read(dst)
        sstr = self.api.reg_read(src_val)
        # convert int to binary string
        dstr = format(dstr, '08b')
        sstr = format(sstr, '08b')

        # initialize overflow flag to 0
        self.api.reg_write(self.api._ovr_reg, 0)

        for i in range(1,9):    # todo: sad conditional
            a = dstr[-i]
            b = sstr[-i]
            ovr = self.api.reg_read(self._ovr_reg)

            # Write Tape to ADDTM
            tape_input = format(ovr,'b') + a + b + '2' + '_'
            self.api.tape_write_raw(self.api.ADD, tape_input)

            # Execute Tape
            self.api.execute()

            # Read Tape
            out = self.api.tape_read_raw()
            ovr = out[3]
            res = out[4]

            # Write back overflow bit and dst bit
            self.api.reg_write(self._ovr_reg, ovr)
            d = self.api.reg_read(dst)
            self.api.reg_write(dst, int(res + format(d, '08b'), 2))

        return

    def sub(self,dst,src):
        if self.is_int(src):
            src_val = int(src)
        else:
            src_val = self.api.reg_read(src)

        dstr = self.api.reg_read(dst)
        sstr = self.api.reg_read(src_val)
        # convert int to binary string
        dstr = format(dstr, '08b')
        sstr = format(sstr, '08b')

        # initialize overflow flag to 0
        self.api.reg_write(self.api._ovr_reg, 0)

        for i in range(1,9):    # todo: sad conditional
            a = dstr[-i]
            b = sstr[-i]
            ovr = self.api.reg_read(self._ovr_reg)

            # Write Tape to SUBTM
            tape_input = format(ovr,'b') + a + b + '2' + '_' + '2'
            self.api.tape_write_raw(self.api.SUB, tape_input)

            # Execute Tape
            self.api.execute()

            # Read Tape
            out = self.api.tape_read_raw()
            ovr = out[4]  # flipped from add for sub
            res = out[3]

            # Write back overflow bit and dst bit
            self.api.reg_write(self._ovr_reg, ovr)
            d = self.api.reg_read(dst)
            self.api.reg_write(dst, int(res + format(d, '08b'), 2))

    def load(self,dst,src):
        if self.is_int(src):
            src_val = int(src)
        else:
            src_val = self.api.reg_read(src)

        val = self.api.mem_read(src_val)  # todo: src could be mem. write isreg()
        self.api.reg_write(dst, val)

    def store(self,src,dst):
        if self.is_int(src):
            dst_val = int(src)
        else:
            dst_val = self.api.reg_read(src)

        val = self.api.reg_read(src)  # todo: src could be mem. write isreg()
        self.api.mem_write(dst_val, val)

    def exit(self):
        sys.exit(0)

    def execute(self):
        ''' Execute commands until end of ppasm instruction list '''
        return

if __name__ == "__main__":
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Application.Visible = True
    ppt = Application.ActivePresentation

    if len(sys.argv != 3):
        print("USAGE: $ python3 ppexe.py [.ppasm file]")
        sys.exit(1)

    fp = sys.argv[2]

    ppexe = PPEXE(ppt,fp)
    ppexe.execute()
