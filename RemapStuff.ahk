#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#singleInstance

RCtrl::
	Send, ^v
	return

F23::
    Run, "C:\Users\thoma\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\CreateWl-main\CreateWl-main\makeWl.py"
    return
