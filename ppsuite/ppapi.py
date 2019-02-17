import subprocess
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
            "ISZ": 7
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

    #init instr cache page
    def init_inst_cache(self):
        self.pres.Slides.Add(self.INSTR_CACHE, 12)
        self.pres.SlideShowWindow.View.GoToSlide(self.INSTR_CACHE)

        slide = self.pres.Slides(self.INSTR_CACHE)

        slide.Shapes.AddTextbox(Orientation=0x1,
                                Left=100,
                                Top=20,
                                Width=300,
                                Height=30)
        slide.Shapes(1).TextFrame.TextRange.Text = "1"

    #loads program from ppasm file
    def load_ppasm(self, file_path):
        self.pres.SlideShowWindow.View.GoToSlide(self.INSTR_CACHE)
        instr_cache_slide = self.pres.Slides(self.INSTR_CACHE)
        shape_num = 2

        with open(file_path, 'r') as f:
            for asm_line in f:
                if instr_cache_slide.Shapes.Count < shape_num:
                    instr_cache_slide.Shapes.AddTextbox(Orientation=0x1,
                                                        Left=100,
                                                        Top=20 * shape_num,
                                                        Width=300,
                                                        Height=30)
                instr_cache_slide.Shapes(shape_num).TextFrame.TextRange.Text = asm_line.split('\t')[2]
                shape_num += 1

    #returns next instr
    def get_next_instr(self):
        instr_cache_slide = self.pres.Slides(self.INSTR_CACHE)
        ip_num = int(instr_cache_slide.Shapes(1).TextFrame.TextRange.Text)
        instr_cache_slide.Shapes(1).TextFrame.TextRange.Text = str(ip_num + 1)

        return instr_cache_slide.Shapes(ip_num).TextFrame.TextRange.Text

    #updates instruction counter
    def update_instr_ptr(self, new_num):
        instr_cache_slide = self.pres.Slides(self.INSTR_CACHE)
        instr_cache_slide.Shapes(1).TextFrame.TextRange.Text = str(new_num)

    # Initializes the register page
    def init_register(self):
        self.pres.Slides.Add(self.REG, 12)

        slide = self.pres.Slides(self.REG)
        self.pres.SlideShowWindow.View.GoToSlide(self.REG)

        for reg_num in range(1, 9):
            slide.Shapes.AddTextbox(Orientation=0x1,
                                    Left=100,
                                    Top=50 * reg_num,
                                    Width=300,
                                    Height=30)

            textframe = slide.Shapes(reg_num).TextFrame
            if (reg_num == (self.reg_table['SP'] + 1)):
                textframe.TextRange.Text = "X{}: 255".format(reg_num - 1)
            else:
                textframe.TextRange.Text = "X{}: 0".format(reg_num - 1)

    # Writes a val to a register
    def reg_write(self, reg_name, val):
        print(reg_name)
        reg_num = self.reg_table[reg_name]

        self.pres.SlideShowWindow.View.GoToSlide(self.REG)

        slide = self.pres.Slides(self.REG)
        textframe = slide.Shapes(reg_num + 1).TextFrame

        textframe.TextRange.Text = "X{}: {}".format(reg_num,val)

    # Reads a val from a register
    def reg_read(self, reg_name):
        print(reg_name)

        reg_num = self.reg_table[reg_name]

        self.pres.SlideShowWindow.View.GoToSlide(self.REG)

        slide = self.pres.Slides(self.REG)
        textframe = slide.Shapes(reg_num + 1).TextFrame
        val = int(textframe.TextRange.Text[4:])

        return val

    # Initializes the memory page
    def init_mem(self):
        self.pres.Slides.Add(self.MEM_0, 12)
        self.pres.Slides.Add(self.MEM_1, 12)
        slide_0 = self.pres.Slides(self.MEM_0)
        slide_1 = self.pres.Slides(self.MEM_1)
        self.pres.SlideShowWindow.View.GoToSlide(self.MEM_0)

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

    # Writes a val to mem
    def mem_write(self, mem_loc, val):
        overflow = mem_loc // 128

        if overflow == 0:
            slide = self.MEM_0
        elif overflow == 1:
            slide = self.MEM_1
        else:
            slide = self.MEM_1

        self.pres.SlideShowWindow.View.GoToSlide(slide)

        mem_loc_real = mem_loc

        if mem_loc > 127:
            mem_loc_real = mem_loc - 128

        slide = self.pres.Slides(slide)
        textframe = slide.Shapes(mem_loc_real + 1).TextFrame

        textframe.TextRange.Text = "{}: {}".format(hex(mem_loc), hex(val))

    # Reads a val from mem
    def mem_read(self, mem_loc):
        overflow = mem_loc // 128

        if overflow == 0:
            slide = self.MEM_0
        elif overflow == 1:
            slide = self.MEM_1
        else:
            slide = self.MEM_1

        self.pres.SlideShowWindow.View.GoToSlide(slide)

        mem_loc_real = mem_loc

        if mem_loc > 127:
            mem_loc_real = mem_loc - 128

        slide = self.pres.Slides(slide)
        textframe = slide.Shapes(mem_loc_real + 1).TextFrame

        strip_len = len(hex(mem_loc)) + 2
        # lol don't store data as hex strings
        val = int(str(bin(int(textframe.TextRange.Text[strip_len:], 16)))[2:])

        print(val)

        return val

    def tape_write_raw(self, tape_loc, val):
        self.pres.SlideShowWindow.View.GoToSlide(tape_loc)

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
        print(out)

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
