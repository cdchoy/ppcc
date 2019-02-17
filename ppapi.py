import subprocess
import win32com.client

class PPAPI:

    def __init__(self, pres, init_mem_reg=True):
        self.pres = pres

        self.SLIDE_MEM_0 = 1
        self.SLIDE_MEM_1 = 2
        self.SLIDE_REG = 3

        if (init_mem_reg == True):
            self.init_mem()
            self.init_register()

    # Initializes the register page
    def init_register(self):
        self.pres.Slides.Add(self.SLIDE_REG, 12)

        slide = self.pres.Slides(self.SLIDE_REG)

        for reg_num in range(1, 9):
            slide.Shapes.AddTextbox(Orientation=0x1,
                                    Left=100,
                                    Top=50 * reg_num,
                                    Width=300,
                                    Height=30)

            textframe = slide.Shapes(reg_num).TextFrame
            textframe.TextRange.Text = "X{}: 0".format(reg_num - 1)

    # Writes a val to a register
    def reg_write(self, reg_num, val):
        slide = self.pres.Slides(self.SLIDE_REG)
        textframe = slide.Shapes(reg_num + 1).TextFrame

        textframe.TextRange.Text = "X{}: {}".format(reg_num,val)

    # Reads a val from a register
    def reg_read(self, reg_num):
        slide = self.pres.Slides(self.SLIDE_REG)
        textframe = slide.Shapes(reg_num + 1).TextFrame

        val = int(textframe.TextRange.Text[4:])

        return val

    # Initializes the memory page
    def init_mem(self):
        self.pres.Slides.Add(self.SLIDE_MEM_0, 12)
        self.pres.Slides.Add(self.SLIDE_MEM_1, 12)
        slide_0 = self.pres.Slides(self.SLIDE_MEM_0)
        slide_1 = self.pres.Slides(self.SLIDE_MEM_1)

        for reg_num in range(1, 129):
            x = 100 + ((reg_num - 1) % 16) * 50
            y = 50 + 50 * ((reg_num - 1) // 16)

            slide_0.Shapes.AddTextbox(Orientation=0x1,
                                    Left=x,
                                    Top=y,
                                    Width=60,
                                    Height=20)

            slide_1.Shapes.AddTextbox(Orientation=0x1,
                                    Left=x,
                                    Top=y,
                                    Width=60,
                                    Height=20)

            textframe_0 = slide_0.Shapes(reg_num).TextFrame
            textframe_0.TextRange.Text = "{}: 0".format(hex(reg_num - 1))
            textframe_1 = slide_1.Shapes(reg_num).TextFrame
            textframe_1.TextRange.Text = "{}: 0".format(hex(reg_num - 1 + 128))

    # Writes a val to mem
    def mem_write(self, mem_loc, val):
        overflow = mem_loc // 128

        if overflow == 0:
            slide = self.SLIDE_MEM_0
        elif overflow == 1:
            slide = self.SLIDE_MEM_1
        else:
            slide = self.SLIDE_MEM_1

        mem_loc_real = mem_loc

        if mem_loc > 127:
            mem_loc_real = mem_loc - 128

        slide = self.pres.Slides(slide)
        textframe = slide.Shapes(mem_loc_real + 1).TextFrame

        textframe.TextRange.Text = "{}: {}".format(hex(mem_loc), val)

    # Reads a val from mem
    def mem_read(self, mem_loc):
        overflow = mem_loc // 128

        if overflow == 0:
            slide = self.SLIDE_MEM_0
        elif overflow == 1:
            slide = self.SLIDE_MEM_1
        else:
            slide = self.SLIDE_MEM_1

        mem_loc_real = mem_loc

        if mem_loc > 127:
            mem_loc_real = mem_loc - 128

        slide = self.pres.Slides(slide)
        textframe = slide.Shapes(mem_loc_real + 1).TextFrame

        strip_len = len(hex(mem_loc)) + 2
        val = int(textframe.TextRange.Text[strip_len:])

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

        return out

if __name__ == "__main__":
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Application.Visible = True
    pres = Application.ActivePresentation

    api = PPAPI(pres)
