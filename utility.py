from tkinter import filedialog
from tkinter.constants import END

def browseFiles():
    selectFile = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    return selectFile

def saveFile(contentFile):
    selectedFile = browseFiles()
    selectedFile.write(str(contentFile.get('1.0', END)))
    selectedFile.close()

def runScript(isSaved, status, contentFile):
    if isSaved:
        pass
    else:
        saveFile(contentFile)
        isSaved = True

