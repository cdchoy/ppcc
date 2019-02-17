; This toggles the execution stage of PPTM

; Ensure we're at the left end of the tape

sleep 500
MouseMove, 1013, 1016, 0
Click
sleep 2000 ; Wait for transition


i := A_Args[1]

FileAppend, %i%, *

; Write to the cell
if (i = 1) {
    loop 8 {
        sleep 100
        MouseMove, 895, 610, 0
        Click
    }
}