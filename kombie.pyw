import keyboard  
import wgt3

def on_hotkey():  
    print("Hotkey gedrückt!")  
    wgt3.main()


# Definiert eine Tastenkombination (z.B. Alt+H)  
keyboard.add_hotkey('alt+l', on_hotkey)  

# Programm läuft, bis die 'esc'-Taste gedrückt wird  
keyboard.wait('esc')