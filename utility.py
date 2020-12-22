from tkinter import filedialog
from tkinter.constants import END
import subprocess
import re

def browseFiles():
    selectFile = filedialog.asksaveasfile(mode='a', defaultextension=".kts")
    if selectFile != None:
        return selectFile.name
    else:
   	    return None


def saveFile(contentFile):
    selectedFile = browseFiles()
    with open(str(selectedFile), 'w') as f :
        f.write(str(contentFile.get('1.0', END)))
    return selectedFile

def runScript(status, contentFile, console, runButton, returnCode):
    
    
    if status.cget('text') != 'Untitled.txt':
    	
        runButton.config(text="Running")
        with open(str(status.cget('text')), 'w') as f:
        	f.write(str(contentFile.get('1.0', END)))
        output = subprocess.run(["kotlinc", "-script", str(status.cget('text'))],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        result = output.stdout.decode()
       	
    else:
        runButton.config(text="Running")
        file = saveFile(contentFile)
        print(file)
        output = subprocess.run(["kotlinc", "-script", file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        result = output.stdout.decode()
        status.configure(text = str(file) )
        
    print(findError(str(result)))
    errors = findError(str(result))
    returnCode.config(text = "Return code: " + str(output.returncode))
    console.configure(state='normal')
    console.insert('end', result)
    for i in errors:
        idx = '1.0'
        while True:
            idx = console.search(i, idx, nocase=1, stopindex=END)
            if not idx: break
             
                
            endidx = '%s+%dc' % (idx, len(i))  
               
            console.tag_add(i, idx, endidx)  
            idx = endidx 
          
        console.tag_config(i, foreground='red', underline = True)
        console.tag_bind(i, "<Button-1>", lambda e: goTo(i, contentFile))
        
    console.configure(state='disabled')
    runButton.config(text = "Run")
    
def findError(errorMsg):
    err = re.findall("[a-zA-Z]*\.[a-z]*:[1-9]*:[1-9]*", errorMsg)
    return err
    
def goTo(err, console):
    rowcol = err.split(':')
    print(rowcol)
    console.mark_set("insert", "%d.%d" % (3 , 5 ))
    
