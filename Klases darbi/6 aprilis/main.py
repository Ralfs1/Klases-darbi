import tkinter as tk
import tkinter.ttk as ttk

class Window:
    def __init__(self,master):

         style = ttk.Style()
         style.theme_create("Custom")
         style.theme_settings("Custom", {
           "TButton": {
               "configure": {"padding": 10},
               "map": {
                   "background": [("active", "yellow3"),
                                  ("!disabled", "yellow")],
                   "foreground": [("focus", "Red"),
                                  ("active", "green"),
                                  ("!disabled", "Blue")]
               }
           }
        })

         style.theme_use("Custom")

         button = ttk.Button(master, text = "Uzspied!")
         button.pack(padx = 5, pady = 5)
        
        
         label = ttk.Label(master, text = "Es esmu Label")
         label.pack(padx = 5, pady = 5)

root = tk.Tk()
root.geometry('200x220')
window = Window(root)
root.mainloop()