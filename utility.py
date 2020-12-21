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

def runScript(status, contentFile, console, runButton):
    
    
    if status.cget('text') != 'Untitled.txt':
    	
        runButton.config(text="Running")
        with open(str(status.cget('text')), 'w') as f:
        	f.write(str(contentFile.get('1.0', END)))
        output = subprocess.Popen("kotlinc " + "-script "+ str(status.cget('text')), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std_out, std_err = output.communicate()
        if output.returncode != 0:
            result = str(std_err.strip())
        else:
       	
            result = str(std_out)
    else:
        runButton.config(text="Running")
        file = saveFile(contentFile)
        output = subprocess.Popen("kotlinc " + "-script "+ file, shell=True, stdout=subprocess.PIPE)
        std_out, std_err = output.communicate()
        if output.returncode != 0:
            result = str(std_err)
        else:
       	
            result = str(std_out)
        status.configure(text = str(file) )
    
    print(output.returncode)
    console.configure(state='normal')
    console.insert('end', result)
    console.configure(state='disabled')
    runButton.config(text = "Run")
    

