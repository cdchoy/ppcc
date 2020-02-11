import subprocess
import time
import win32com.client  # todo rm. pres is initialized in ppexe

class PPAPI:
    def __init__(self, pres):

        if pres == None:
            self.regs = []
            self.mem_0 = []
            self.mem_1 = []
            self.instr = []
            self.tape = ['_', '_', '_', '_', '_', '_', '_', '_']
            self.virtual = True
            self.tape_loc = -1

        else:
            self.pres = pres
            self.virtual = False
            self.tape_loc = -1 # unused (virtual only)

        self.MEM_0 = 1
        self.MEM_1 = 2
        self.REG = 3
        self.INSTR_CACHE = 4

        self.NUM_TURING_SLIDES = 4 #Chane this
        self.SUCC = 5
        self.PRED = 6
        self.ADD = 7
        self.SUB = 8

        self.reg_table = {
            "A": 0,
            "B": 1,
            "C": 2, 
            "D": 3,
            "SP": 4,
            "BP": 5,
            "OVR": 6,
            "ISZ": 7,
            "TMP": 8
        }

        if self.virtual or self.pres.Slides.Count == self.NUM_TURING_SLIDES:
            self.init_mem()
            self.init_register()
            # self.init_inst_cache()

    def is_int(self, val):
        ''' Checks if a value in a string can be converted to int '''
        try:
            int(val)
            return True
        except ValueError:
            return False

    # Pulls up a slide
    def show_slide(self, slide, wait=.5):
        self.pres.SlideShowWindow.View.GoToSlide(slide)
        time.sleep(wait)
        return self.pres.Slides(slide)

    #init instr cache page
    def init_inst_cache(self):

        if self.virtual:
            self.instr.append("1")

        else:
            self.pres.Slides.Add(self.INSTR_CACHE, 12)
            self.show_slide(self.INSTR_CACHE)
            slide = self.pres.Slides(self.INSTR_CACHE)

            slide.Shapes.AddTextbox(Orientation=0x1,
                                    Left=100,
                                    Top=20,
                                    Width=300,
                                    Height=30)
            slide.Shapes(1).TextFrame.TextRange.Text = "1"

    #loads program from ppasm file
    def load_ppasm(self, file_path):
        if not self.virtual:
            slide = self.show_slide(self.INSTR_CACHE)
    
        line = 2

        with open(file_path, 'r') as f:
            for asm_line in f:
                txt = asm_line.split('\t')[2]

                if self.virtual:
                    self.instr.append(txt)

                else:
                    slide.Shapes.AddTextbox(Orientation=0x1,
                                            Left=100,
                                            Top=20 * line,
                                            Width=300,
                                            Height=30)
                    slide.Shapes(line).TextFrame.TextRange.Text = txt

                line += 1

    #returns next instr
    def get_next_instr(self):
        if self.virtual:
            ip_num = int(self.instr[0])
            self.instr[0] = str(ip_num + 1)

            return self.instr[ip_num]

        else:
            self.show_slide(self.INSTR_CACHE)

            instr_cache_slide = self.pres.Slides(self.INSTR_CACHE)
            ip_num = int(instr_cache_slide.Shapes(1).TextFrame.TextRange.Text)
            instr_cache_slide.Shapes(1).TextFrame.TextRange.Text = str(ip_num + 1)

            return instr_cache_slide.Shapes(ip_num + 1).TextFrame.TextRange.Text

    #updates instruction counter
    def update_instr_ptr(self, new_num):
        if self.virtual:
            self.instr[0] = str(int(new_num) + 1)

        else:
            slide = self.show_slide(self.INSTR_CACHE)
            slide.Shapes(1).TextFrame.TextRange.Text = str(int(new_num) + 1)

    # Initializes the register page
    def init_register(self):

        if not self.virtual:
            self.pres.Slides.Add(self.REG, 12)
            slide = self.show_slide(self.REG)

        for reg_num in range(1, 10):
            if (reg_num == (self.reg_table['SP'] + 1)):
                txt =  "X{}: 11111111".format(reg_num - 1)
            else:
                txt =  "X{}: 00000000".format(reg_num - 1)
            
            if self.virtual:
                self.regs.append(txt)

            else:
                slide.Shapes.AddTextbox(Orientation=0x1,
                                        Left=100,
                                        Top=50 * reg_num,
                                        Width=300,
                                        Height=30)

                textframe = slide.Shapes(reg_num).TextFrame
                textframe.TextRange.Text = txt

    # Writes a string to a register
    def reg_write_raw(self, reg_name, val):
        reg_num = self.reg_table[reg_name]

        txt = "X{}: {}".format(reg_num,val)

        if self.virtual:
            self.regs[reg_num] = txt

        else:
            slide = self.show_slide(self.REG)
            textframe = slide.Shapes(reg_num + 1).TextFrame

            textframe.TextRange.Text = txt

    # Converts a value to binary string, then writes to a register
    def reg_write(self, reg_name, val):
        raw = format(val, '08b')
        self.reg_write_raw(reg_name, raw)

    # Reads a string from a register
    def reg_read_raw(self, reg_name):
        reg_num = self.reg_table[reg_name]

        if self.virtual:
            txt = self.regs[reg_num]

        else:
            slide = self.show_slide(self.REG)
            textframe = slide.Shapes(reg_num + 1).TextFrame

            txt = textframe.TextRange.Text

        strip_len = len(str(reg_num)) + 3
        val = txt[strip_len:]

        return val

    # Reads a binary string from a register, 
    # then converts it to an int
    def reg_read(self, reg_name):
        raw = self.reg_read_raw(reg_name)
        val = int(raw, 2)

        return val

    # Initializes the memory page
    def init_mem(self):

        if not self.virtual:
            self.pres.Slides.Add(self.MEM_0, 12)
            self.pres.Slides.Add(self.MEM_1, 12)
            slide_0 = self.show_slide(self.MEM_0)
            slide_1 = self.pres.Slides(self.MEM_1)

        for reg_num in range(1, 129):
            x = 15 + ((reg_num - 1) % 16) * 42
            y = 40 + 57 * ((reg_num - 1) // 16)

            txt_0 = "{}: {}".format(hex(reg_num - 1), hex(0))
            txt_1 = "{}: {}".format(hex(reg_num - 1), hex(0))

            if self.virtual:
                self.mem_0.append(txt_0)
                self.mem_1.append(txt_1)

            else:
                slide_0.Shapes.AddTextbox(Orientation=0x1,
                                        Left=x,
                                        Top=y,
                                        Width=45,
                                        Height=18)

                slide_1.Shapes.AddTextbox(Orientation=0x1,
                                        Left=x,
                                        Top=y,
                                        Width=45,
                                        Height=18)

                textframe_0 = slide_0.Shapes(reg_num).TextFrame
                textframe_0.TextRange.Font.Size = 10
                textframe_0.TextRange.Text = txt_0
                textframe_1 = slide_1.Shapes(reg_num).TextFrame
                textframe_1.TextRange.Font.Size = 10
                textframe_1.TextRange.Text = txt_1

    # Writes a string to memory
    def mem_write_raw(self, mem_loc, val):
        mem_loc_real = mem_loc
        slide_num = self.MEM_0

        if mem_loc > 127:
            mem_loc_real = mem_loc - 128
            slide_num = self.MEM_1

        txt = "{}: {}".format(hex(mem_loc), val)

        if self.virtual:
            if slide_num == self.MEM_0:
                self.mem_0[mem_loc_real] = txt
            else:
                self.mem_1[mem_loc_real] = txt

            print("Wrote {}".format(txt))

        else:
            slide = self.show_slide(slide_num)
            textframe = slide.Shapes(mem_loc_real + 1).TextFrame

            textframe.TextRange.Text = txt

    # Converts a value to hex string, then writes to memory
    def mem_write(self, mem_loc, val):
        raw = hex(val)
        self.mem_write_raw(mem_loc, raw)

    # Reads a string from memory
    def mem_read_raw(self, mem_loc):
        mem_loc_real = mem_loc
        slide_num = self.MEM_0
        
        if mem_loc > 127:
            mem_loc_real = mem_loc - 128
            slide_num = self.MEM_1

        if self.virtual:
            if slide_num == self.MEM_0:
                txt = self.mem_0[mem_loc_real]
            else:
                txt = self.mem_1[mem_loc_real]

        else:
            slide = self.show_slide(slide_num)
            textframe = slide.Shapes(mem_loc_real + 1).TextFrame
            txt = textframe.TextRange.Text

        strip_len = len(hex(mem_loc)) + 2
        val = txt[strip_len:]

        return val

    # Reads a binary string from a register, 
    # then converts it to an int
    def mem_read(self, mem_loc):
        raw = self.mem_read_raw(mem_loc)
        no_hex_prefix = raw[2:]
        val = int(no_hex_prefix, 16)

        return val

    def tape_write_raw(self, tape_loc, val):
        lst = list(val)

        if self.virtual:
            for idx, char in enumerate(lst):
                self.tape[idx] = char

            self.tape_loc = tape_loc

        else:
            self.show_slide(tape_loc)
            args = ["C:/Program Files/AutoHotkey/AutoHotkeyU64.exe",
                    "hotkey/tape_write.ahk"]
            args += lst

            ahk = subprocess.Popen(args, stdout=subprocess.PIPE)
            ahk.wait()

    # Reads a tape and returns its raw output
    def tape_read_raw(self):
        if self.virtual:
            out = ''.join(self.tape)

        else:
            ahk = subprocess.Popen(["C:/Program Files/AutoHotkey/AutoHotkeyU64.exe",
                                    "hotkey/tape_read.ahk"], stdout=subprocess.PIPE)
            ahk.wait()
            out = ahk.stdout.read().decode()

        return out

    def execute(self):

        if self.virtual:
            if self.tape_loc == self.ADD:
                res = int(self.tape[0]) + int(self.tape[1]) + int(self.tape[2])

                if res > 1:
                    self.tape[3] = '1'
                    self.tape[4] = str(res - 2)[0]
                else:
                    self.tape[3] = '0'
                    self.tape[4] = str(res)[0]

            elif self.tape_loc == self.SUB:
                res = int(self.tape[1]) - int(self.tape[0]) - int(self.tape[2])

                if res < 0:
                    self.tape[4] = '1'
                    self.tape[3] = str(res + 2)[0]
                else:
                    self.tape[4] = '0'
                    self.tape[3] = str(res)[0]

        else:
            ahk_start = subprocess.Popen(["C:/Program Files/AutoHotkey/AutoHotkeyU64.exe",
                                        "hotkey/toggle_exec.ahk"])
            ahk_start.wait()

            ahk_run = subprocess.Popen(["C:/Program Files/AutoHotkey/AutoHotkeyU64.exe",
                                        "hotkey/cpu_cycle.ahk"])
            ahk_run.wait()

            ahk_teardown = subprocess.Popen(["C:/Program Files/AutoHotkey/AutoHotkeyU64.exe",
                                            "hotkey/toggle_exec.ahk", "1"])
            ahk_teardown.wait()

    # Need to find the delete function for slides
    def teardown(self):
        self.pres.Slides.Delete(1) # MEM_0
        self.pres.Slides.Delete(1) # MEM_1
        self.pres.Slides.Delete(1) # REG


if __name__ == "__main__":
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Application.Visible = True
    pres = Application.ActivePresentation

    api = PPAPI(pres)
    # api.load_ppasm("./ppasm/test.ppasm")

    api.mem_write(5, 11001111)
    val = api.mem_read(5)
    api.tape_write_raw(4, str(val))
    api.execute()
    res = api.tape_read_raw()
    # api.teardown()
