import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, E, END, LEFT, RIGHT, TOP, W, X, Y
import utility

keyWords = ['var', 'for', 'if', 'else', 'when', 'as', 'break', 'continue', 'class', 'true', 'false', 'null', 'return ', 'val']


currStr = ''
def keyPressed(event):
    global currStr
    global keyWords
    global editor
    idx = '1.0'
    editor.tag_remove('key', '1.0', END) 
    text = editor.get('1.0', END).replace('\n',' ')
    words = text.split(' ')
    
    words.remove('')
    
    for i in range(len(words) - 1):
        
        if words[i] in keyWords:
            
            idx = '1.0'
            while True:
                idx = editor.search(words[i], idx, nocase=1, stopindex=END)
                if not idx: break
                
                
                endidx = '%s+%dc' % (idx, len(words[i]))  
                
                editor.tag_add('key', idx, endidx)  
                idx = endidx 
            
            editor.tag_config('key', foreground='blue')


window = tk.Tk()
window.geometry('800x500')
window.bind('<Key>', keyPressed)

scrollBar = tk.Scrollbar()
scrollBar.place(x = 890, y = 35)
scrollBar.pack(side = RIGHT, fill= Y)

editor = tk.Text( height=49, width=110, yscrollcommand=scrollBar.set)
editor.place(x = 5, y = 35)
scrollBar.config(command = editor.yview)

runButton = tk.Button( text='Run', width=10, command=lambda : utility.runScript(status,editor, output, runStatus, returnCode) )
runButton.place(x=5, y=2)

status = tk.Label(text='Untitled.txt')
status.place(x=130, y=6)

output = tk.Text(height= 49, width= 50)
output.configure(state='disabled')
output.place(x = 960, y = 35)

runStatus = tk.Label(text = " ")
runStatus.place(x=500, y=6)

returnCode = tk.Label(text = " ")
returnCode.place(x=800, y=6)

window.mainloop()
