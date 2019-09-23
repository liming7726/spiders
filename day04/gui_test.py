from tkinter import *




root = Tk()

root.title('你说的标题')
root.geometry("800x600")



w = Menubutton(master=root,cnf={
    '1':'1',
})

w.pack()





root.mainloop()
