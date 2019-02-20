import subprocess
import time
import win32com.client  # todo rm. pres is initialized in ppexe

class PPAPI:
    def __init__(self, pres):
        self.pres = pres

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

        if self.pres.Slides.Count == self.NUM_TURING_SLIDES:
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
    def show_slide(self, slide, time=.5):
        self.pres.SlideShowWindow.View.GoToSlide(slide)
        time.sleep(time)
        return self.pres.Slides(slide)

    #init instr cache page
    def init_inst_cache(self):
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
        slide = self.show_slide(self.INSTR_CACHE)
        shape_num = 2

        with open(file_path, 'r') as f:
            for asm_line in f:
                if slide.Shapes.Count < shape_num:
                    slide.Shapes.AddTextbox(Orientation=0x1,
                                                        Left=100,
                                                        Top=20 * shape_num,
                                                        Width=300,
                                                        Height=30)
                slide.Shapes(shape_num).TextFrame.TextRange.Text = asm_line.split('\t')[2]
                shape_num += 1

    #returns next instr
    def get_next_instr(self):
        self.show_slide(self.INSTR_CACHE)

        instr_cache_slide = self.pres.Slides(self.INSTR_CACHE)
        ip_num = int(instr_cache_slide.Shapes(1).TextFrame.TextRange.Text)
        instr_cache_slide.Shapes(1).TextFrame.TextRange.Text = str(ip_num + 1)

        return instr_cache_slide.Shapes(ip_num + 1).TextFrame.TextRange.Text

    #updates instruction counter
    def update_instr_ptr(self, new_num):
        slide = self.show_slide(self.INSTR_CACHE)
        slide.Shapes(1).TextFrame.TextRange.Text = str(int(new_num) + 1)

    # Initializes the register page
    def init_register(self):
        self.pres.Slides.Add(self.REG, 12)

        slide = self.show_slide(self.REG)

        for reg_num in range(1, 10):
            slide.Shapes.AddTextbox(Orientation=0x1,
                                    Left=100,
                                    Top=50 * reg_num,
                                    Width=300,
                                    Height=30)

            textframe = slide.Shapes(reg_num).TextFrame
            if (reg_num == (self.reg_table['SP'] + 1)):
                textframe.TextRange.Text = "X{}: 11111111".format(reg_num - 1)
            else:
                textframe.TextRange.Text = "X{}: 00000000".format(reg_num - 1)

    # Writes a string to a register
    def reg_write_raw(self, reg_name, val):
        reg_num = self.reg_table[reg_name]

        slide = self.show_slide(self.REG)
        textframe = slide.Shapes(reg_num + 1).TextFrame

        textframe.TextRange.Text = "X{}: {}".format(reg_num,val)

    # Converts a value to binary string, then writes to a register
    def reg_write(self, reg_name, val):
        bin_val = format(val, '08b')
        raw = bin_val[2:]
        self.reg_write_raw(reg_name, raw)

    # Reads a string from a register
    def reg_read_raw(self, reg_name):
        reg_num = self.reg_table[reg_name]

        slide = self.show_slide(self.REG)
        textframe = slide.Shapes(reg_num + 1).TextFrame

        strip_len = len(str(reg_num)) + 3
        val = textframe.TextRange.Text[strip_len:]

        return val

    # Reads a binary string from a register, 
    # then converts it to an int
    def reg_read(self, reg_name):
        raw = self.reg_read_raw(reg_name)
        val = int(raw, 2)

        return val

    # Initializes the memory page
    def init_mem(self):
        self.pres.Slides.Add(self.MEM_0, 12)
        self.pres.Slides.Add(self.MEM_1, 12)
        slide_0 = self.show_slide(self.MEM_0)
        slide_1 = self.pres.Slides(self.MEM_1)

        for reg_num in range(1, 129):
            x = 15 + ((reg_num - 1) % 16) * 42
            y = 40 + 57 * ((reg_num - 1) // 16)

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
            textframe_0.TextRange.Text = "{}: {}".format(hex(reg_num - 1), hex(0))
            textframe_1 = slide_1.Shapes(reg_num).TextFrame
            textframe_1.TextRange.Font.Size = 10
            textframe_1.TextRange.Text = "{}: {}".format(hex(reg_num - 1 + 128), hex(0))

    # Writes a string to memory
    def mem_write_raw(self, mem_loc, val):
        mem_loc_real = mem_loc
        slide_num = self.MEM_0

        if mem_loc > 127:
            mem_loc_real = mem_loc - 128
            slide_num = self.MEM_1

        slide = self.show_slide(slide_num)
        textframe = slide.Shapes(mem_loc_real + 1).TextFrame

        textframe.TextRange.Text = "{}: {}".format(hex(mem_loc), val)

    # Converts a value to hex string, then writes to memory
    def mem_write(self, mem_loc, val):
        hex_val = hex(val)
        raw = hex_val[2:]
        self.mem_write_raw(mem_loc, raw)

    # Reads a string from memory
    def mem_read_raw(self, mem_loc):
        mem_loc_real = mem_loc
        slide_num = self.MEM_0
        
        if mem_loc > 127:
            mem_loc_real = mem_loc - 128
            slide_num = self.MEM_1

        slide = self.show_slide(slide_num)
        textframe = slide.Shapes(mem_loc_real + 1).TextFrame

        strip_len = len(hex(mem_loc)) + 2
        val = textframe.TextRange.Text[strip_len:]

        return val

    # Reads a binary string from a register, 
    # then converts it to an int
    def mem_read(self, mem_loc):
        raw = self.reg_read_raw(mem_loc)
        val = int(raw, 16)

        return val

    def tape_write_raw(self, tape_loc, val):
        self.show_slide(tape_loc)

        lst = list(val)
        args = ["C:/Program Files/AutoHotkey/AutoHotkeyU64.exe",
                "hotkey/tape_write.ahk"]
        args += lst

        ahk = subprocess.Popen(args, stdout=subprocess.PIPE)
        ahk.wait()

    # Reads a tape and returns its raw output
    def tape_read_raw(self):
        ahk = subprocess.Popen(["C:/Program Files/AutoHotkey/AutoHotkeyU64.exe",
                                "hotkey/tape_read.ahk"], stdout=subprocess.PIPE)
        ahk.wait()
        out = ahk.stdout.read().decode()

        return out

    def execute(self):
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
