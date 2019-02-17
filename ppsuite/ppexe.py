#!/bin/python3

# Instruction Decoder & Loader
# PPASM -> PPAPI

import sys  # only for sys.exit()
import win32com.client
from ppapi import PPAPI
import time
import win32gui
from windowmngr import WindowMgr

# Stretch Goal Ops:
#     putc src
#     getc dst
#     jmp jmp
#     jeq/jne/jlt/jgt/jle/jge jmp,dst,src
#     eq/ne/lt/gt/le/ge dst,src
#     dump

class PPEXE(object):

    _ovr_bit = "OVR"  # over/underflow register for add/sub
    _isz_bit = "ISZ"  # isZero flag

    def __init__(self,ppt,filepath):
        self.api = PPAPI(ppt)

        # Load ppasm into ppcpu
        self.api.init_inst_cache()
        self.api.load_ppasm(filepath)

    def is_int(self, val):
        ''' Checks if a value in a string can be converted to int '''
        try:
            int(val)
            return True
        except ValueError:
            return False

    def mov(self,dst,src):
        if self.is_int(src):
            val = int(src)
        else:
            val = self.api.reg_read(src)

        # TODO- make sure val is clean
        self.api.reg_write(dst, val)

    def add(self,dst,src):
        if self.is_int(src):
            sstr = src
        else:
            sstr = self.api.reg_read(src)

        dstr = self.api.reg_read(dst)
        # convert int to binary string
        dstr = format(int(dstr), '08b')
        sstr = format(int(sstr), '08b')

        # initialize overflow flag to 0
        self.api.reg_write(self._ovr_bit, 0)
        self.api.reg_write(dst, 0)

        for i in range(1,9):    # todo: sad conditional
            a = dstr[-i]
            b = sstr[-i]
            ovr = self.api.reg_read(self._ovr_bit)

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
            self.api.reg_write(self._ovr_bit, ovr)
            d = self.api.reg_read(dst)
            self.api.reg_write(dst, int(res + bin(d)[2:].zfill(i - 1), 2))

        return

    def sub(self,dst,src):
        if self.is_int(src):
            sstr = src
        else:
            sstr = self.api.reg_read(src)

        dstr = self.api.reg_read(dst)
        print("Subtracting {} from {}".format(sstr, dstr))
        # convert int to binary string
        dstr = format(int(dstr), '08b')
        sstr = format(int(sstr), '08b')
        print("subtracting {} from {}".format(sstr, dstr))

        # initialize overflow flag to 0
        self.api.reg_write(self._ovr_bit, 0)
        self.api.reg_write(dst, 0)

        for i in range(1,9):    # todo: sad conditional
            a = dstr[-i]
            b = sstr[-i]
            ovr = self.api.reg_read(self._ovr_bit)

            # Write Tape to SUBTM
            tape_input = format(ovr,'b') + a + b + '2' + '_' + '2'
            self.api.tape_write_raw(self.api.SUB, tape_input)
            print("tape input: {}".format(tape_input))
            # Execute Tape
            self.api.execute()

            # Read Tape
            out = self.api.tape_read_raw()
            ovr = out[4]  # flipped from add for sub
            res = out[3]
            print("tape output: res {} ovr {}".format(res, ovr))

            # Write back overflow bit and dst bit
            self.api.reg_write(self._ovr_bit, ovr)
            d = self.api.reg_read(dst)
            print("d is {}".format(d))
            print("Writing: {}".format(res + format(d, 'b')))
            self.api.reg_write(dst, int(res + bin(d)[2:].zfill(i - 1), 2))

        # set isz_bit
        if self.api.reg_read(dst) == 0: # cond handled by wiring
            self.api.reg_write(self._isz_bit, 1)
        else:
            self.api.reg_write(self._isz_bit, 0)

    def load(self,dst,src):
        if self.is_int(src):  # cond handled by wiring
            src_val = int(src)
        else:
            src_val = self.api.reg_read(src)

        val = self.api.mem_read(src_val)
        self.api.reg_write(dst, val)

    def store(self,src,dst):
        if self.is_int(dst):  # cond handled by wiring
            dst_val = int(dst)
        else:
            dst_val = self.api.reg_read(dst)

        val = self.api.reg_read(src)
        self.api.mem_write(dst_val, val)

    def eq(self, dst, src):
        self.sub(dst, src)
        cond = self.api.reg_read(self._isz_bit)
        self.mov(self._isz_bit, cond)

    def ne(self, dst, src):
        self.sub(dst, src)
        cond = not self.api.reg_read(self._isz_bit)
        self.mov(self._isz_bit, cond)

    def lt(self, dst, src):
        self.sub(dst, src)
        cond = not self.api.reg_read(self._isz_bit) and \
               self.api.reg_read(self._ovr_bit)
        self.mov(self._isz_bit, cond)

    def gt(self, dst, src):
        self.sub(dst, src)
        cond = not self.api.reg_read(self._isz_bit) and \
               not self.api.reg_read(self._ovr_bit)
        self.mov(self._isz_bit, cond)

    def le(self, dst, src):
        self.sub(dst, src)
        cond = self.api.reg_read(self._isz_bit) or \
               self.api.reg_read(self._ovr_bit)
        self.mov(self._isz_bit, cond)

    def ge(self, dst, src):
        self.sub(dst, src)
        cond = self.api.reg_read(self._isz_bit) or \
               not self.api.reg_read(self._ovr_bit)
        self.mov(self._isz_bit, cond)

    def jmp(self, jmp):
        self.api.update_instr_ptr(jmp)

    def jeq(self, jmp, dst, src):
        self.eq(dst, src)

        if self.api.reg_read(self._isz_bit):
            self.jmp(jmp)

    def jne(self, jmp, dst, src):
        self.ne(dst, src)

        if self.api.reg_read(self._isz_bit):
            self.jmp(jmp)

    def jlt(self, jmp, dst, src):
        self.lt(dst, src)

        if self.api.reg_read(self._isz_bit):
            self.jmp(jmp)

    def jgt(self, jmp, dst, src):
        self.gt(dst, src)

        if self.api.reg_read(self._isz_bit):
            self.jmp(jmp)

    def jle(self, jmp, dst, src):
        self.le(dst, src)

        if self.api.reg_read(self._isz_bit):
            self.jmp(jmp)

    def jge(self, jmp, dst, src):
        self.ge(dst, src)

        if self.api.reg_read(self._isz_bit):
            self.jmp(jmp)


    def execute(self):
        ''' Execute commands until end of ppasm instruction list '''

        while (1):      # todo: sad loop :(
            instr = self.api.get_next_instr()
            args = instr.split(' ')

            print("Processing: {}".format(instr))

            # Dispatch Table
            if args[0] == 'mov':
                self.mov(args[1][:-1], args[2][:-1])
            elif args[0] == 'add':
                self.add(args[1][:-1], args[2][:-1])
            elif args[0] == 'sub':
                self.sub(args[1][:-1], args[2][:-1])
            elif args[0] == 'load':
                self.load(args[1][:-1], args[2][:-1])
            elif args[0] == 'store':
                self.store(args[1][:-1], args[2][:-1])
            elif args[0] == 'eq':
                self.eq(args[1][:-1], args[2][:-1])
            elif args[0] == 'ne':
                self.ne(args[1][:-1], args[2][:-1])
            elif args[0] == 'lt':
                self.lt(args[1][:-1], args[2][:-1])
            elif args[0] == 'gt':
                self.gt(args[1][:-1], args[2][:-1])
            elif args[0] == 'le':
                self.le(args[1][:-1], args[2][:-1])
            elif args[0] == 'ge':
                self.ge(args[1][:-1], args[2][:-1])
            elif args[0] == 'jmp':
                self.jmp(args[1][:-1])
            elif args[0] == 'jeq':
                self.jeq(args[1][:-1], args[2][:-1], args[3][:-1])
            elif args[0] == 'jne':
                self.jne(args[1][:-1], args[2][:-1], args[3][:-1])
            elif args[0] == 'jlt':
                self.jlt(args[1][:-1], args[2][:-1], args[3][:-1])
            elif args[0] == 'jgt':
                self.jgt(args[1][:-1], args[2][:-1], args[3][:-1])
            elif args[0] == 'jle':
                self.jle(args[1][:-1], args[2][:-1], args[3][:-1])
            elif args[0] == 'jge':
                self.jge(args[1][:-1], args[2][:-1], args[3][:-1])
            elif args[0] == 'exit':
                break

        # todo: read from stdout buffer
        return

if __name__ == "__main__":
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Application.Visible = True
    time.sleep(8)
    ppt = Application.ActivePresentation

    w = WindowMgr()
    w.find_window_wildcard(".*PPCPU.*")
    w.set_foreground()

    ppt.SlideShowSettings.Run().View.AcceleratorsEnabled = False

    if len(sys.argv) != 2:
        print("USAGE: $ python3 ppexe.py [.ppasm file]")
        sys.exit(1)

    fp = sys.argv[1]

    ppexe = PPEXE(ppt,fp)
    ppexe.execute()
