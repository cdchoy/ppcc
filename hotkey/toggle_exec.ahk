; This toggles the execution stage of PPTM

; Ensure we're at the left end of the tape
Loop, 8 {
    sleep 100

    ; Move to prev cell
    MouseMove, 895, 610, 0
    Click
}

sleep 500
MouseMove, 1013, 1016, 0
Click
sleep 2000 ; Wait for transition