import argparse
import subprocess
import os

"""
Reads the lone command line argument and returns it as a str
"""
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    return args.file_path

def compile_program(file_path):
    subprocess.call(["./elvm/8cc/8cc", file_path, "-S"])

def convert_elir_to_ppasm(file_name):
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
    line_num = 0;

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
                nf.write(str(line_num))
                nf.write("\t")
                nf.write(' '.join(line_elems).rstrip('\n'))
                nf.write('\n')
                line_num += 1
    # os.remove(compiled_file)

def main():
    if (os.getcwd().split('/')[-1] != 'ppasm'):
        print('Must execute this program in the ppasm folder')

    file_path = parse_args()
    file_name = file_path.split('/')[-1]
    compile_program(file_path)
    convert_elir_to_ppasm(file_name)


if __name__ == '__main__':
    main()