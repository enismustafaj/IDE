from tkinter import filedialog
from tkinter.constants import END
import tkinter as tk
import subprocess
import re
import time

# select the file to save
def browseFiles():
    selectFile = filedialog.asksaveasfile(mode='a', defaultextension=".kts")
    if selectFile != None:
        return selectFile.name
    else:
   	    return None

# save the file
def saveFile(contentFile):
    selectedFile = browseFiles()
    with open(str(selectedFile), 'w') as f :
        f.write(str(contentFile.get('1.0', END)))
    return selectedFile


# function which is trigerred when the script is running
def runScript(status, contentFile, console, runButton, returnCode):
    
    runButton.config(fg = "green")
	
	# check if the file is saved
	# if not save first then run
    if status.cget('text') != 'Untitled.txt':
          
        with open(str(status.cget('text')), 'w') as f:
        	f.write(str(contentFile.get('1.0', END)))
        output = subprocess.run(["kotlinc", "-script", str(status.cget('text'))],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        result = output.stdout.decode()
       	
    else:
    
        file = saveFile(contentFile)
        output = subprocess.run(["kotlinc", "-script", file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        result = output.stdout.decode()
        status.configure(text = str(file) )
    
    # get all the error locations in the code
    errors = list(findError(str(result)))
    
    returnCode.config(text = "Return code: " + str(output.returncode))
    
    # write the output ot output pane
    console.configure(state='normal')
    console.delete('1.0', END)
    console.insert('end', result)
    count = 0
    
    # add a tag to each error and funtion to redirect to the location
    for i in errors:
        idx = '1.0'
        idx = console.search(i, idx, nocase=1, stopindex=END)
        endidx = '%s+%dc' % (idx, len(i))        
        console.tag_add("err " + str(count), idx, endidx)   
        console.tag_config("err " + str(count), foreground='red', underline = True)
        console.tag_bind("err " + str(count), "<Button-1>", lambda l: goTo(i, contentFile))
        count += 1
        
    console.configure(state='disabled')
    
    runButton.configure(fg = "gray")

# function to get all the errors    
def findError(errorMsg):
    err = re.findall("[a-zA-Z]*\.[a-z]*:[1-9]*:[1-9]*", errorMsg)
    return set(err)

#function to go to the location of the error    
def goTo(err, console):
    rowcol = err.split(':')
    idx = console.search(err, '1.0', nocase=1, stopindex=END)
    console.mark_set("insert", idx)
    
