from tkinter import filedialog
from tkinter.constants import END
import subprocess

def browseFiles():
    selectFile = filedialog.asksaveasfile(mode='a', defaultextension=".kts")
    return selectFile.name

def saveFile(contentFile):
    selectedFile = browseFiles()
    with open(str(selectedFile), 'w') as f :
        f.write(str(contentFile.get('1.0', END)))
    return selectedFile

def runScript(status, contentFile, console):
    
    if status.cget('text') != 'Untitled.txt':
        output = subprocess.run(["kotlinc", "-script", str(status.cget('text'))], stdout=subprocess.PIPE, text=True)
    else:
        file = saveFile(contentFile)
        output = subprocess.run(["kotlinc", str(file)])
        status.configure(text = str(file) )
    
    console.configure(state='normal')
    console.insert('end', output)
    console.configure(state='disabled')

