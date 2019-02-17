import argparse
import subprocess
import os

"""
Reads the lone command line argument and returns it as a str
"""

class PPCC:

    def __init__(self):
        pass

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("file_path")
        args = parser.parse_args()
        return args.file_path

    def compile_program(self, file_path):
        subprocess.call(["../elvm/8cc/8cc", file_path, "-S"])

    def convert_elir_to_ppasm(self, file_name):
        line_num = 0
        branch_dir = {}
        file_root = file_name.split('.')[0]
        compiled_file = file_root + '.s'
        new_file = file_root + '.ppasm'

        #Build branch dir
        with open(compiled_file, 'rw') as f:
            for line in f:
                line_elems = line.split(' ')
                if line_elems[0].startswith('\t#') or line_elems[0].startswith('\t.') or (':' in line_elems[0]):
                    if ':' in line_elems[0]:
                        branch_dir[line_elems[0][0:-2].lstrip('\t')] = line_num
                    continue
                line_num += 1
        line_num = 0

        with open(compiled_file, 'rw') as f:
            with open(new_file, 'w+') as nf:
                for line in f:
                    line_elems = line.split(' ')
                    #skip pseudo ops and comments
                    if line_elems[0].startswith('\t#') or line_elems[0].startswith('\t.') or (':' in line_elems[0]):
                        continue
                    # If this is a jump instruction, figure out the target line
                    if 'j' in line_elems[0]:
                        target = line_elems[1]
                        line_elems[1] = str(branch_dir[target[:-1]])
                    # If the iinsturction tries to add a negative number, convert it to a sub
                    if 'add' in line_elems[0]:
                        arg1 = line_elems[1]
                        arg2 = line_elems[2].rstrip('\n')
                        if self.is_number(arg1) and int(arg1) < 0:
                            line_elems[1] = str(int(arg1) * -1)
                            line_elems[0] = '\tsub'
                        if self.is_number(arg2) and int(arg2) < 0:
                            line_elems[2] = str(int(arg2) * -1)
                            line_elems[0] = '\tsub'
                    if 'sub' in line_elems[0]:
                        arg1 = line_elems[1]
                        arg2 = line_elems[2].rstrip('\n')
                        if self.is_number(arg2) and int(arg2) < 0:
                            line_elems[2] = str(int(arg2) * -1)
                            line_elems[0] = '\tadd'

                    nf.write(str(line_num))
                    nf.write("\t")
                    nf.write(' '.join(line_elems).rstrip('\n'))
                    nf.write('\n')
                    line_num += 1
        # os.remove(compiled_file)

    def compile(self):
        if (os.getcwd().split('/')[-1] != 'ppsuite'):
            print('Must execute this program in the ppasm folder')

        file_path = self.parse_args()
        file_name = file_path.split('/')[-1]
        self.compile_program(file_path)
        self.convert_elir_to_ppasm(file_name)


if __name__ == '__main__':

    asm = PPCC()
    asm.compile()