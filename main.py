import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, E, END, LEFT, RIGHT, TOP, W, X, Y
import utility

# keywords that are recognized
keyWords = ['var', 'for', 'if', 'else', 'when', 'as', 'break', 'continue', 'class', 'true', 'false', 'null', 'return ', 'val']


# function that is trigerred when a key is pressed 
def keyPressed(event):
    global currStr
    global keyWords
    global editor
    idx = '1.0'
    editor.tag_remove('key', '1.0', END)
    
    # get all the words in the editor 
    text = editor.get('1.0', END).replace('\n',' ')
    words = text.split(' ')
    words.remove('')
    
    for i in range(len(words) - 1):
        # if a word is a keyword add a tag to it and make it blue
        if words[i] in keyWords:
            
            idx = '1.0'
            while True:
                idx = editor.search(words[i], idx, nocase=1, stopindex=END)
                if not idx: break
                
                
                endidx = '%s+%dc' % (idx, len(words[i]))  
                
                editor.tag_add('key', idx, endidx)  
                idx = endidx 
            
            editor.tag_config('key', foreground='blue')
        
        # if a word is a function add a tag to it and make it green
        if '(' in words[i]:
            func = list(words[i].split('('))[0]
            idx = '1.0'
            while True:
                idx = editor.search(func, idx, nocase=1, stopindex=END)
                if not idx: break
                
                
                endidx = '%s+%dc' % (idx, len(func))  
                
                editor.tag_add('function', idx, endidx)  
                idx = endidx 
            
            editor.tag_config('function', foreground='green')
            


# initialize the window
window = tk.Tk()
window.geometry('800x500')
photo = tk.PhotoImage(file = './icon.png')
window.title("KIDE")
window.iconphoto(False, photo)
window.bind('<Key>', keyPressed)

scrollBar = tk.Scrollbar()
scrollBar.place(x = 890, y = 35)
scrollBar.pack(side = RIGHT, fill= Y)

# add the editor pane
editor = tk.Text( height=49, width=110, yscrollcommand=scrollBar.set)
editor.place(x = 5, y = 35)
scrollBar.config(command = editor.yview)

runButton = tk.Button( text='Run', width=10, command=lambda : utility.runScript(status,editor, output, runStatus, returnCode) )
runButton.place(x=5, y=2)

status = tk.Label(text='Untitled.txt')
status.place(x=130, y=6)

# add the output pane
output = tk.Text(height= 49, width= 50)
output.configure(state='disabled')
output.place(x = 960, y = 35)

runStatus = tk.Label(text = "Running", fg = "gray")
runStatus.place(x=600, y=6)

returnCode = tk.Label(text = " ")
returnCode.place(x=900, y=6)

window.mainloop()
