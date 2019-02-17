; This attempts to click every position in the PPCPU TM
; Each loop of this program simulates about 1/4 of 
; a CPU cycle

; All of the random numbers are X, Y coordinates of items 
; on the powerpoint in a 1920x1080 resolution
; Have fun if that's not your resolution

; I'm sorry about the bad code
; AutoHotKey scripting is awful

Loop {

    ; Were we able to click something?
    Clicked = 0

    ; Read buttons
    PixelGetColor, color_var, 858, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 839, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 839, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 839, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 839, 0
        Clicked = 1
        Click
    }

    ; Write buttons
    PixelGetColor, color_var, 858, 693 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 693, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 693 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 693, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 693 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 693, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 693 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 693, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 858, 724 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 724, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 724 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 724, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 724 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 724, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 724 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 724, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 858, 753 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 753, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 753 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 753, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 753 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 753, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 753 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 753, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 858, 781 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 781, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 781 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 781, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 781 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 781, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 781 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 781, 0
        Clicked = 1
        Click
    }

    ; Move buttons
    PixelGetColor, color_var, 858, 609 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 609, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 914, 609 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 609, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 609 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 609, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 609 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 609, 0
        Clicked = 1
        Click
    }

    PixelGetColor, color_var, 858, 640 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 858, 640, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 914, 640 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 914, 640, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 972, 640 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 972, 640, 0
        Clicked = 1
        Click
    }
    PixelGetColor, color_var, 1030, 640 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        MouseMove, 1030, 640, 0
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