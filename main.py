import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, E, LEFT, RIGHT, TOP, W, X, Y
import utility

isSaved = False


window = tk.Tk()

scrollBar = tk.Scrollbar()
scrollBar.place(x = 890, y = 35)
scrollBar.pack(side = RIGHT, fill= Y)

editor = tk.Text( height=49, width=110, yscrollcommand=scrollBar.set)
editor.place(x = 5, y = 35)
scrollBar.config(command = editor.yview)

runButton = tk.Button( text='Run', width=10, command=lambda : utility.saveFile(editor) )
runButton.place(x=5, y=2)

status = tk.Label(text='Untitled.txt')
status.place(x=130, y=6)

output = tk.Text(height= 49, width= 50)
output.configure(state='disabled')
output.place(x = 960, y = 35)


window.mainloop()