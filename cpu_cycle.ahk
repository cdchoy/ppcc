; This attempts to click every position in the PPCPU TM
; Each loop of this program simulates about 1/4 of 
; a CPU cycle

; All of the random numbers are X, Y coordinates of items 
; on the powerpoint in a 1920x1080 resolution
; Have fun if that's not your resolution

; I'm sorry about the bad code
; AutoHotKey scripting is awful

Sleep, 20000

Loop {

    ; Were we able to click something?
    Clicked = 0

    ; Read buttons
    PixelGetColor, color_var, 857, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 857, 839, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 894, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 894, 839, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1006, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1006, 839, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1065, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1065, 839, 0
        Clicked = 1
        Click
    }

    ; Write buttons
    PixelGetColor, color_var, 857, 693 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 857, 693, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 894, 693 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 894, 693, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1006, 693 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1006, 693, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1065, 693 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1065, 693, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 857, 724 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 857, 724, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 894, 724 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 894, 724, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1006, 724 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1006, 724, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1065, 724 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1065, 724, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 857, 753 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 857, 753, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 894, 753 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 894, 753, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1006, 753 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1006, 753, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1065, 753 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1065, 753, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 857, 781 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 857, 781, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 894, 781 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 894, 781, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1006, 781 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1006, 781, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1065, 781 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1065, 781, 0
        Clicked = 1
        Click
    }

    ; Move buttons
    PixelGetColor, color_var, 857, 609 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 857, 609, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 894, 609 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 894, 609, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1006, 609 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1006, 609, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1065, 609 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1065, 609, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 857, 640 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 857, 640, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 894, 640 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 894, 640, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1006, 640 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1006, 640, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1065, 640 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1065, 640, 0
        Clicked = 1
        Click
    }

    ; Next buttons
    PixelGetColor, color_var, 858, 358
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 358, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 358
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 358, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 358
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 358, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 358
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 358, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 858, 382
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 382, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 382
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 382, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 382
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 382, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 382
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 382, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 858, 412
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 412, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 412
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 412, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 412
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 412, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 412
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 412, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 858, 440
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 440, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 440
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 440, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 440
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 440, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 440
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 440, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 858, 468
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 468, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 468
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 468, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 468
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 468, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 468
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 468, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 858, 497
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 497, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 497
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 497, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 497
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 497, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 497
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 497, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 858, 526
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 526, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 526
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 526, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 526
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 526, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 526
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 526, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 858, 555
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 555, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 555
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 555, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 555
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 555, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 555
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 555, 0
        Clicked = 1
        Click
    }


    if (Clicked == 0) {
        Break
    }
}

Return