from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 20)


class Application(tk.Tk):
    # 切换界面
    def __init__(self):
        super().__init__()

        self.wm_title("学生信息管理系统")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # 循环功能界面
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    # 主页面
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="学生信息管理系统", bg="blue", font=LARGE_FONT)
        label.pack(pady=100)
        ft2=tkFont.Font(size=16)
        Button(self, text="添加学生信息",font=ft2,command=lambda: root.show_frame(PageOne),width=30,height=2,fg='white',bg='green',activebackground='black',activeforeground='white').pack()
        Button(self, text="删除学生信息",font=ft2,command=lambda: root.show_frame(PageTwo),width=30,height=2).pack()
        Button(self, text="修改学生信息",font=ft2,command=lambda: root.show_frame(PageThree),width=30,height=2,fg='white',bg='green',activebackground='black',activeforeground='white').pack()
        Button(self, text="查询学生信息",font=ft2,command=lambda: root.show_frame(PageFour),width=30,height=2).pack()
        Button(self,text='退出系统',height=2,font=ft2,width=30,command=root.destroy,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()


class PageOne(tk.Frame):
    # 添加学生信息
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="添加学生信息", font=LARGE_FONT)
        label.pack(pady=100)

        ft3 = tkFont.Font(size=14)
        ft4 = tkFont.Font(size=12)
        Label(self, text='学生学号：', font=ft3).pack(side=TOP)
        global e1
        e1 = StringVar()
        Entry(self, width=30, textvariable=e1, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='学生姓名：', font=ft3).pack(side=TOP)
        global e2
        e2 = StringVar()
        Entry(self, width=30, textvariable=e2, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='学生电话号码：', font=ft3).pack(side=TOP)
        global e3
        e3 = StringVar()
        Entry(self, width=30, textvariable=e3, font=ft3, bg='Ivory').pack(side=TOP)
        Button(self, text="返回首页", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack(pady=20)
        Button(self, text="确定保存", width=8, font=ft4, command=self.save).pack(side=TOP)

    def save(self):
        with open('student_infor.txt', 'a+') as student_infor:
            num = str(e1.get())
            name = str(e2.get())
            score = str(e3.get())
            student_infor.write(num + ' ' + name + ' ' + score + '\n')


class PageTwo(tk.Frame):
    #删除学生信息
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="删除学生信息", font=LARGE_FONT)
        label.pack(pady=100)

        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        Label(self,text='请输入你要删除的学生学号：',font=ft3).pack(side=TOP)
        global e4
        e4=StringVar()
        Entry(self,width=30,textvariable=e4,font=ft3,bg='Ivory').pack(side=TOP)
        Button(self, text="确定删除",width=8,font=ft4,command=self.del1).pack(pady=20)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack()
        #button1 = ttk.Button(self, text="回到首页", command=lambda: root.show_frame(StartPage)).pack()
        #button2 = ttk.Button(self, text="去到第一页", command=lambda: root.show_frame(PageOne)).pack()
    def del1(self):
        num2=str(e4.get())
        with open('student_infor.txt','r') as f:
            lines=f.readlines()
            with open('student_infor.txt','w') as f_w:
                for line in lines:
                    if num2 in line:
                        continue
                    f_w.write(line)


class PageThree(tk.Frame):
    # 修改学生信息
    def __init__(self, parent, root):
        super().__init__(parent)
        tk.Label(self, text="修改学生信息", font=LARGE_FONT).pack(pady=100)

        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        Label(self,text='请输入你要修改的学生学号：',font=ft3).pack(side=TOP)
        self.e5=StringVar()
        Entry(self,width=30,textvariable=self.e5,font=ft3,bg='Ivory').pack(side=TOP)
        Label(self,text='学生姓名：',font=ft3).pack(side=TOP)
        self.e6=StringVar()
        Entry(self,width=30,textvariable=self.e6,font=ft3,bg='Ivory').pack(side=TOP)
        Label(self,text='学生电话号码：',font=ft3).pack(side=TOP)
        self.e7=StringVar()
        Entry(self,width=30,textvariable=self.e7,font=ft3,bg='Ivory').pack(side=TOP)
        Button(self, text="确定修改",width=8,font=ft4,command=self.modify).pack(pady=20)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack()

    def modify(self):
        num3=str(self.e5.get())
        name3=str(self.e6.get())
        score3=str(self.e7.get())
        with open('student_infor.txt','r') as r_w:
            lines1=r_w.readlines()
            with open('student_infor.txt','w') as rr_w:
                for line1 in lines1:
                    if num3 in line1:
                        rr_w.write(num3+' '+name3+' '+score3+'\n')
                        continue
                    rr_w.write(line1)


class PageFour(tk.Frame):
    # 查询学生信息
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="查询学生信息", font=LARGE_FONT)
        label.pack(pady=100)
        tree_data=ttk.Treeview()
        ft4=tkFont.Font(size=12)
       #滚动条

        scro=Scrollbar(self)

        scro.pack(side=RIGHT,fill=Y)
        lista=Listbox(self,yscrollcommand=scro.set,width=50)

        f=open('student_infor.txt','r')
        text=("                 %-16s%-16s%-16s"%("学号","姓名","电话号码"))

        li=[]
        for i in f.readlines():
            j=i.split(' ')
            j[2]=j[2].replace('\n','')
            li.append(j)
            li.sort(key=lambda x:x[2],reverse=False)
        for i in li:
            text1=("                %-16s%-16s%-16s"%(i[0],i[1],i[2]))
            lista.insert(0,text1)
        f.close()
        lista.insert(0,text)
        lista.pack()
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=40)


if __name__ == '__main__':
    app = Application()
    app.mainloop()
