; Writes a series of values to a tape
; These must be passed in as separate command line args

sleep 2000

loop %0% {
    Sleep 800

    i := A_Args[A_Index]

    ; Write to the cell
    if (i =  _) {
        MouseMove, 889, 697, 0
        Click
    }
    if (i = 0) {
        ; Had to replace 0 with 3 because this stupid
        ; language is dumb with comparisons to 0
        MouseMove, 889, 721, 0
        Click
    }
    if (i = 1) {
        MouseMove, 889, 752, 0
        Click
    }
    if (i = 2) {
        MouseMove, 889, 780, 0
        Click
    }

    ; Move to next cell
    MouseMove, 853, 639, 0
    Click
}

Loop, 8 {
    sleep 100

    ; Move to prev cell
    MouseMove, 895, 610, 0
    Click
}