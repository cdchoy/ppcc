; This reads from the ALU and writes to stdout

; All of the random numbers are X, Y coordinates of items 
; on the powerpoint in a 1920x1080 resolution
; Have fun if that's not your resolution

Loop, 8 {
    sleep 500

    value = -1

    ; Read buttons
    PixelGetColor, color_var, 886, 833 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        value = _
    }
    PixelGetColor, color_var, 946, 835 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        value = 0
    }
    PixelGetColor, color_var, 1006, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        value = 1
    }
    PixelGetColor, color_var, 1065, 839 
    if (color_var == 0x317ded || color_var == 0x2444d1) {
        value = 2
    }

    ; Move to next cell
    MouseMove, 853, 639, 0
    Click

    FileAppend, %value%, *
}

Loop, 8 {

    ; Move to prev cell
    MouseMove, 853, 610, 0
    Click
}