import Tkinter
import ttk
import time
import threading


#Define your Progress Bar function, 
def task(root,str):
    ft = ttk.Frame(width=500,height=500)
    ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP,padx=100,pady=100)
    infolabel = ttk.Label(ft, text=str)
    infolabel.config(font=("Courier", 15))
    infolabel.pack(side = Tkinter.TOP,pady=15)
    pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate',length=300)
    pb_hD.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.BOTTOM)
    pb_hD.start(50)

# Define the process of unknown duration with root as one of the input And once done, add root.quit() at the end.
# Now define our Main Functions, which will first define root, then call for call for "task(root)" --- that's your progressbar, and then call $

def progressBar():
    root = Tkinter.Tk()
    t1=threading.Thread(target= installMethod, args=(root,))
    t1.start()
    task(root,str)  # This will block while the mainloop runs
    root.mainloop()
    t1.join()
