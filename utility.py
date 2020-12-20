from tkinter import filedialog
from tkinter.constants import END

def browseFiles():
    selectFile = filedialog.asksaveasfile(mode='a', defaultextension=".txt")
    return selectFile.name

def saveFile(contentFile):
    selectedFile = browseFiles()
    with open(str(selectedFile), 'w') as f :
        f.write(str(contentFile.get('1.0', END)))
    return selectedFile

def runScript(status, contentFile):
    if status.cget('text') != 'Untitled.txt':
        pass
    else:
        file = saveFile(contentFile)
        status.configure(text = str(file) )
        isSaved = True


