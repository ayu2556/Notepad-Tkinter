from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import  askopenfilename,asksaveasfilename
from tkinter.ttk import *
  
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()
        
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitiled.txt",
                               defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            
            
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
    else:
        f=open(file,"w")
        f.write(text.get(1.0,END))
        f.close()
        
def saveas():
    global file
    file=asksaveasfilename(initialfile="Untitiled.txt",
                               defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
            
            
        f=open(file,"w")
        f.write(text.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+"-Notepad")
    
def quitapp():
    root.destroy()
def Cut():
    text.event_generate(("<<Cut>>"))
def Copy():
    text.event_generate(("<<Copy>>"))
def Paste():
    text.event_generate(("<<Paste>>"))
def undo():
    text.event_generate(("<<Undo>>"))
def about():
     showinfo("Notepad", "Notepad by Ayush Sahu")
def In():
    text.event_generate(("<<Control-F>>"))
def newWin(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(root) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("New Window") 
    newWindow.maxsize(300,300)
    # sets the geometry of toplevel 
    newWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="This is a new window").pack() 
  
    fram = Frame(newWindow)
    edit = Entry(fram)  
  
    #positioning of text box 
    edit.pack(side=LEFT, fill=X, expand=1,ipady=30)  
  
    #setting focus 
    edit.focus_set()  
  
    #adding of search button 
    butt = Button(fram, text='Find')   
    butt.pack(side=RIGHT)  
    fram.pack(side=TOP) 
  
#text box in root window 
    
  
#text input area at index 1 in text window 
      
    
  
  
#function to search string in text 
    def find(): 
      
    #remove tag 'found' from index 1 to END
        text.tag_remove('found', '1.0', END)  
      
    #returns to widget currently in focus
        s = edit.get()  
        if s:
            idx = '1.0'
            while 1: 
            #searches for desried string from index 1
                idx = text.search(s, idx, nocase=1,  
                              stopindex=END)
                if not idx: break
              
            #last index sum of current index and 
            #length of text
                lastidx = '%s+%dc' % (idx, len(s))  
              
            #overwrite 'Found' at idx
                text.tag_add('found', idx, lastidx)
                idx = lastidx 
          
        #mark located string as red 
            text.tag_config('found', foreground='red',background='yellow')  
        edit.focus_set() 
    butt.config(command=find) 
def replace():
    def replaceall():
         
        text.tag_remove('found', '1.0', END)  
      
    #returns to widget currently in focus
        findtext = edit.get()  
        replacetext = replace.get(1.0,END)
        alltext = str(text.get(1.0, END))
        alltext1 = all.replace(findtext, replacetext)
        text.delete(1.0, END)
        text.insert('1.0', alltext1)
    replacebox =Toplevel(root)
    replacebox.geometry("230x150")
    replacebox.title("Replace..")
    fram = Frame(replacebox)
    fn=Label(replacebox,text="find")
    
    fn.place(relx = 0.0,  
                 rely = 1.0,  
                 anchor ='nw') 
    
    edit = Entry(fram)  
    edit.pack(expand=1,ipady=5)
    edit.focus_set()  
    replace = Entry(fram).pack(expand=1,ipady=5)
    
    replaceallbutton = Button(fram, text="Replace..", command=replaceall)
    replaceallbutton.pack(side=RIGHT)
    fram.pack(side=TOP)



root=Tk()
root.title("Notepad")
root.wm_iconbitmap("notepad.ico")
root.geometry("600x400")

text=Text(root,font="lucida 13",wrap=NONE,undo=TRUE)
file=None
text.pack(expand="true",fill=BOTH)



scroll=Scrollbar(text,orient=VERTICAL)
scroll.pack(fill=Y,side=RIGHT)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

scroll1=Scrollbar(text,orient=HORIZONTAL)
scroll1.pack(fill=X,side=BOTTOM)
scroll1.config(command=text.xview)
text.config(xscrollcommand=scroll1.set)


Menubar=Menu(root)   #create menubar
Filemenu=Menu(Menubar,tearoff=0)
x=" "
#open new file
Filemenu.add_command(label=f"New{20*x}",command=newFile)
Filemenu.add_command(label=f"Open{20*x}",command=openFile)
Filemenu.add_command(label=f"Save{20*x}",command=saveFile)
Filemenu.add_command(label=f"SaveAs{20*x}",command=saveas)
Filemenu.add_separator()
Filemenu.add_command(label=f"Exit{20*x}",command=quitapp)
Menubar.add_cascade(label="File",menu=Filemenu)


Editmenu=Menu(Menubar,tearoff=0)

#Edit file
Editmenu.add_command(label=f"Undo{10*x}Ctrl+Z",command=text.edit_undo)
Editmenu.add_separator()
Editmenu.add_command(label=f"Cut{12*x} Ctrl+X",command=Cut)
Editmenu.add_command(label=f"Copy{10*x}Ctrl+C",command=Copy)
Editmenu.add_command(label=f"Paste{10*x}Ctrl+V",command=Paste)
Editmenu.add_command(label=f"Zoom in{10*x}Ctrl+V",command=In)

Menubar.add_cascade(label="Edit",menu=Editmenu)

#help
Helpmenu=Menu(Menubar,tearoff=0)
Helpmenu.add_command(label="About",command=about)
Menubar.add_cascade(label="Help",menu=Helpmenu)

Find=Menu(Menubar,tearoff=0)
Find.add_command(label="Find",command=newWin)
Find.add_command(label="Replace",command=replace)
Menubar.add_cascade(label="Find",menu=Find)
  
root.config(menu=Menubar)

statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
root.mainloop()
