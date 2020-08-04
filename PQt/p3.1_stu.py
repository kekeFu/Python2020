import tkinter as tk

window = tk.Tk()
window.title("学生信息管理系统")
window.geometry("500x500")

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg="blue", font=('Arial',12), width=15, height=2)
# 放置, 点：l.place()
l.pack()

on_hit = False


def hit_me():
    global on_hit
    if not on_hit:
        on_hit = False
        var.set('Sno')
    else:
        on_hit = True
        var.set("学号")


b = tk.Button(window, text="Sno", width=15, height=2, command=hit_me)
b.pack()


# while 点一下就会更新数据
window.mainloop()