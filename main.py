import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, E, END, LEFT, RIGHT, TOP, W, X, Y
import utility

keyWords = ['word', 'key', 'hello', 'somthing']


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
    print(words)
    for i in range(len(words) - 1):
        print(words[i])
        if words[i] in keyWords:
            print('here')
            idx = '1.0'
            while True:
                idx = editor.search(words[i], idx, nocase=1, stopindex=END)
                if not idx: break
                
                
                endidx = '%s+%dc' % (idx, len(words[i]))  
                
                editor.tag_add('key', idx, endidx)  
                idx = endidx 
            
            editor.tag_config('key', foreground='red')


        

window = tk.Tk()
window.geometry('800x500')
window.bind('<Key>', keyPressed)

scrollBar = tk.Scrollbar()
scrollBar.place(x = 890, y = 35)
scrollBar.pack(side = RIGHT, fill= Y)

editor = tk.Text( height=49, width=110, yscrollcommand=scrollBar.set)
editor.place(x = 5, y = 35)
scrollBar.config(command = editor.yview)

runButton = tk.Button( text='Run', width=10, command=lambda : utility.runScript(status,editor) )
runButton.place(x=5, y=2)

status = tk.Label(text='Untitled.txt')
status.place(x=130, y=6)

output = tk.Text(height= 49, width= 50)
output.configure(state='disabled')
output.place(x = 960, y = 35)


window.mainloop()