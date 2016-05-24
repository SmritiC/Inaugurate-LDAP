import Tkinter
from Tkinter import *

samepassword=1

def same(passwd1,passwd2):
        if(passwd1==passwd2):
                return 1
        else:
                return 0

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def takePassword(root,frame,passwd1,passwd2):
	global samepassword
	password1=passwd1.get()
	password2=passwd2.get()
	if(password1=="" or password2==""):
		errlabel = Label(frame, text="Please Enter the password...",height=2,fg="red")
                errlabel.grid(row=7,column=1)
	else:
		if(same(password1,password2)):
			samepassword=1
			root.destroy()
		else:
			samepassword=0
			errlabel = Label(frame, text="Password does not match the confirm password...",height=2,fg="red")
			errlabel.grid(row=7,column=1)

def quit(root):
	root.destroy()

def passwordWin():
	root = Tkinter.Tk()
	#win = Toplevel(root)
	#center(win)
	root.wm_title("LDAP INSTALLATION WINDOW")
	frame=Frame(root,width=500,height=700)
	#frame.title("LDAP intallation")
	frame.pack_propagate(0)
	frame.pack(fill=X,padx=200,pady=190)

	textlabel1 = Label(frame, text="Enter Password for LDAP: ",height=2)
	textlabel1.config(font=("Courier", 15))
	textlabel1.grid(row=1,column=1)
	
	passwd1 = StringVar()
	textBox1 = Entry(frame, show="*", textvariable=passwd1, width=40)
	textBox1.grid(row=2,column=1)

	textlabel2 = Label(frame, text="Re-enter Password for LDAP: ",height=2)
	textlabel2.config(font=("Courier", 15))
	textlabel2.grid(row=3,column=1)

	passwd2 = StringVar()
	textBox2 = Entry(frame, show="*",textvariable=passwd2 , width=40)
	textBox2.grid(row=4,column=1)

	okButton = Button(frame, text="OK", command=lambda: takePassword(root,frame,passwd1,passwd2),width=10)
	okButton.grid(row=5,column=1,pady=5)

	cancelButton = Button (frame, text= "CANCEL" , command = lambda: quit(root), width=10)
	cancelButton.grid(row=6, column=1)

	root.mainloop()
	if(samepassword):
		return(passwd1.get())
	else:
		return None

