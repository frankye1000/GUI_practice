import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('500x200')

def hit_me():
    #messagebox.showinfo(title='警告', message='這是info')
    #messagebox.showwarning(title='警告', message='這是warning')
    #messagebox.showerror(title='警告', message='這是error')
    #print(messagebox.askquestion(title='警告', message='這是question'))
    #print(messagebox.askyesno(title='警告', message='這是問對或錯'))
    print(messagebox.askokcancel(title='警告', message='這是okcancel'))

    
tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()
