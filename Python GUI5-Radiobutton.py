import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

var= tk.StringVar()
l = tk.Label(window, bg='yellow', width=16,text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected'+var.get())
    
r1 = tk.Radiobutton(window,text='Option A',
                    variable=var,value='A',
                    command=print_selection).pack()



    
r2 = tk.Radiobutton(window,text='Option B',
                    variable=var,value='B',
                    command=print_selection).pack()



    
r3 = tk.Radiobutton(window,text='Option C',
                    variable=var,value='C',
                    command=print_selection).pack()



window.mainloop()
