import Tkinter
from Tkinter import *

def validate(root,frame,dnName,orgName):
	if(dnName==""):
		errlabel = Label(frame, text="Please enter the Domain Name...",height=2,fg="red")
                errlabel.grid(row=7,column=1)
	elif(orgName==""):
		errlabel = Label(frame, text="Please Enter the Organization name...",height=2,fg="red")
                errlabel.grid(row=7,column=1)
	else:
		root.destroy()

		

def quit(root):
	root.destroy()

def dnWin():
	root = Tkinter.Tk()
        root.wm_title("LDAP INSTALLATION WINDOW")
        frame=Frame(root,width=500,height=700)
        #frame.title("LDAP intallation")
        frame.pack_propagate(0)
        frame.pack(fill=X,padx=200,pady=190)

        textlabel1 = Label(frame, text="Enter the Domain Name: ",height=2)
        textlabel1.config(font=("Courier", 15))
        textlabel1.grid(row=1,column=1)

        domainName = StringVar()
        textBox1 = Entry(frame, textvariable=domainName, width=40)
        textBox1.grid(row=2,column=1)

        textlabel2 = Label(frame, text="Enter the Organization name: ",height=2)
        textlabel2.config(font=("Courier", 15))
        textlabel2.grid(row=3,column=1)

        orgName = StringVar()
        textBox2 = Entry(frame, textvariable=orgName , width=40)
        textBox2.grid(row=4,column=1)

        okButton = Button(frame, text="OK", command=lambda: validate(root,frame,domainName.get(),orgName.get()),width=10)
        okButton.grid(row=5,column=1,pady=5)

        cancelButton = Button (frame, text= "CANCEL" , command = lambda: quit(root), width=10)
        cancelButton.grid(row=6, column=1)

	root.mainloop()
	dn=[]
	dn.append(domainName.get())
	dn.append(orgName.get())
	return dn




