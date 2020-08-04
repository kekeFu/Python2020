import tkinter as tk

window = tk.Tk()
window.title("学生信息管理系统")
window.geometry("500x500")


e = tk.Entry(window, show=None)  # show="*"，不显示
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert("end", var)


b1 = tk.Button(window, text="insert_point", width=15, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text="insert_end", width=15, height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()


# while 点一下就会更新数据
window.mainloop()

