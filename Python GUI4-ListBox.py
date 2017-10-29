import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

var1 = tk.StringVar()
l = tk.Label(window, bg='red', width=5, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='print selection', width=15,
              height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44,55))

lb = tk.Listbox(window, height=16,listvariable=var2)
list_items=['三','百','壯','士','是','我']
for item in list_items:
    lb.insert('end',item)
lb.insert(0,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()



window.mainloop()
