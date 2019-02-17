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
    file_root = file_name.split('.')[0]
    compiled_file = file_root + '.s'
    new_file = file_root + '.ppasm'
    with open(compiled_file, 'rw') as f:
        with open(new_file, 'rw') as nf:
            for line in compiled_file:
                line_elems = line.split(' ')
                if line_elems[0].startswith('#') or line_elems[0].startswith('.'):
                    continue
                nf.write(line)
                if line_elems[0] == 'add':
                    target = line_elems[1]

def main():
    if (os.getcwd().split('/')[-1] != 'ppasm'):
        print('Must execute this program in the ppasm folder')

    file_path = parse_args()
    file_name = file_path.split('/')[-1]
    compile_program(file_path)
    #convert_elir_to_ppasm(file_name)

if __name__ == '__main__':
    main()