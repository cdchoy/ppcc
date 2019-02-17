import win32com.client

REG_SLIDE = 2
MEM_SLIDE_0 = 3

# Initializes the register page
def init_register(pres):
    pres.Slides.Add(REG_SLIDE, 12)

    slide = pres.Slides(REG_SLIDE)

    for reg_num in range(1, 9):
        slide.Shapes.AddTextbox(Orientation=0x1,
                                Left=100,
                                Top=50 * reg_num,
                                Width=300,
                                Height=30)

        textframe = slide.Shapes(reg_num).TextFrame
        textframe.TextRange.Text = "X{}: 0".format(reg_num - 1)

# Writes a val to a register
def reg_write(pres, reg_num, val):
    slide = pres.Slides(REG_SLIDE)
    textframe = slide.Shapes(reg_num + 1).TextFrame

    textframe.TextRange.Text = "X{}: {}".format(reg_num,val)

# Reads a val from a register
def reg_read(pres, reg_num):
    slide = pres.Slides(REG_SLIDE)
    textframe = slide.Shapes(reg_num + 1).TextFrame

    val = int(textframe.TextRange.Text[4:])

    return val

# Initializes the memory page
def init_mem(pres):
    pres.Slides.Add(MEM_SLIDE_0, 12)
    pres.Slides.Add(MEM_SLIDE_0 + 1, 12)
    slide_0 = pres.Slides(MEM_SLIDE_0)
    slide_1 = pres.Slides(MEM_SLIDE_0 + 1)

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
def mem_write(pres, mem_loc, val):
    slide_num = mem_loc // 128 + MEM_SLIDE_0
    mem_loc_real = mem_loc

    if mem_loc > 127:
        mem_loc_real = mem_loc - 128

    slide = pres.Slides(slide_num)
    textframe = slide.Shapes(mem_loc_real + 1).TextFrame

    textframe.TextRange.Text = "{}: {}".format(hex(mem_loc), val)

# Reads a val from mem
def mem_read(pres, mem_loc):
    slide_num = mem_loc // 128 + MEM_SLIDE_0
    mem_loc_real = mem_loc

    if mem_loc > 127:
        mem_loc_real = mem_loc - 128

    slide = pres.Slides(slide_num)
    textframe = slide.Shapes(mem_loc_real + 1).TextFrame

    strip_len = len(hex(mem_loc)) + 2
    val = int(textframe.TextRange.Text[strip_len:])

    return val


if __name__ == "__main__":
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Application.Visible = True
    pres = Application.ActivePresentation
    # win = pres.SlideShowWindow.View.GoToSlide(1)

    # pres.Slides(1).Shapes(1).TextFrame.TextRange.Text = "BBBBBBBBBBBBBB"

    
    init_register(pres)
    reg_write(pres, 2, 4)
    print(reg_read(pres, 2))

    init_mem(pres)

    for i in range(0, 256):
        mem_write(pres, i, i + 3)
        print(mem_read(pres, i))
