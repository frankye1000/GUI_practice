import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('1000x900')

canvas= tk.Canvas(window,bg='blue',height=400,width=600)

image_file=tk.PhotoImage(file='D:\周莫煩python\GUI\python.png')
image= canvas.create_image(10,10,anchor='nw',image=image_file)
x0,y0,x1,y1=100,100,300,300
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
arc  = canvas.create_arc(x0,y0,x1,y1, start=0, extent=180,fill='yellow')
rect = canvas.create_rectangle(100,30,100+20,30+20)



canvas.pack()



def moveit1():
    canvas.move(oval,10,0)

b1 = tk.Button(window,text='move oval', command = moveit1).pack()

def moveit2():
    canvas.move(arc,10,0)

b2 = tk.Button(window,text='move arc', command = moveit2).pack()

window.mainloop()
