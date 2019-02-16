import win32com.client

REG_SLIDE = 2

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

# Writes a val a register
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





if __name__ == "__main__":
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Application.Visible = True
    presentation = Application.ActivePresentation
    # win = pres.SlideShowWindow.View.GoToSlide(1)

    # pres.Slides(1).Shapes(1).TextFrame.TextRange.Text = "BBBBBBBBBBBBBB"

    
    init_register(presentation)
    reg_write(presentation, 2, 4)
    print(reg_read(presentation, 2))