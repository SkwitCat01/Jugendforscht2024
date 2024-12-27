import tkinter as tk
from tkinter import ttk
import os
import webbrowser

class SideWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Seitenwidget")
        
        # Fenstergröße und Position
        window_width = 250
        window_height = 230
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = screen_width - window_width
        y_position = screen_height - window_height - 50  # Anpassbare Taskleistenhöhe
        
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        self.root.attributes('-alpha', 0)  # Unsichtbar starten
        
        # Hauptrahmen
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.place(relwidth=1, relheight=1)  # Füllt das gesamte Fenster
        
        # Label
        self.label = ttk.Label(self.frame, text="Seitenwidget", font=('Arial', 12, 'bold'))
        self.label.place(x=10, y=10)  # Oben links
        
        # Erster Aktionsbutton
        self.first_button = ttk.Button(self.frame, text="Projekt01", command=self.cmdb)
        self.first_button.place(x=85, y=60)  # Mittig positionieren
        
        # Zweiter Aktionsbutton
        self.second_button = ttk.Button(self.frame, text="LEO", command=self.leob)
        self.second_button.place(x=85, y=100)  # Unter dem ersten Button

        self.eingabe = ttk.Entry(self.frame)
        self.eingabe.place(x=85, y=140)

        self.okob = ttk.Button(self.frame, text="Ok", command=self.okob)
        self.okob.place(x=150, y=140)

        # Stil für den Schließen-Button
        style = ttk.Style()
        style.configure('Close.TButton', foreground='red', font=('Arial', 10, 'bold'))
        
         # Schließen-Button
        self.close_button = ttk.Button(
             self.frame, 
             text="✖", 
             command=self.fade_out,  # Schließe mit Animation
             style='Close.TButton'
            )
        self.close_button.place(x=150, y=10)  # In der oberen rechten Ecke
         
   
        
        # Animation beim Start
        self.fade_in()
        
        # Drag-Funktion
        self.frame.bind("<ButtonPress-1>", self.start_move)
        self.frame.bind("<ButtonRelease-1>", self.stop_move)
        self.frame.bind("<B1-Motion>", self.do_move)
        
    # Animationen
    def fade_in(self):
        alpha = 0.0
        self.root.attributes('-alpha', alpha)
        
        def increase_alpha():
            nonlocal alpha
            alpha += 0.05
            if alpha <= 1.0:
                self.root.attributes('-alpha', alpha)
                self.root.after(50, increase_alpha)
        
        increase_alpha()

    def fade_out(self):
        alpha = self.root.attributes('-alpha')
        
        def decrease_alpha():
            nonlocal alpha
            alpha -= 0.05
            if alpha > 0:
                self.root.attributes('-alpha', alpha)
                self.root.after(50, decrease_alpha)
            else:
                self.root.quit()  # Beende nach dem Ausblenden
        
        decrease_alpha()
    
    # Buttons
    def okob(self):
        print(self.eingabe.get())
        self.label.config(text=self.eingabe.get())
        self.eingabe.delete(0, tk.END)



    def cmdb(self):
        import Programm1

    def leob(self):
        print("LEO wurde geklickt!")
        webbrowser.open("https://scratch.mit.edu/users/Skwit/")

    # Drag-Funktion
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

def main():
    root = tk.Tk()
    app = SideWidget(root)
    root.mainloop()
    

