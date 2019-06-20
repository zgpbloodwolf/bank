import tkinter
from tkinter import *
import sys
from tkinter.messagebox import showinfo
from userviewVer import UserviewVer
from PIL import ImageTk,Image
class Userview():
    def __init__(self,name):
        self.userVer = UserviewVer()
        self.sucess_name = name
    #主页面
    def creat_page(self):
        crea_width=1000
        crea_height=750
        win = tkinter.Tk()
        win.title('用户使用')
        win.resizable(width=False, height=False)
        i = Image.open('uservie.gif')
        i = i.resize((crea_width,crea_height),Image.ANTIALIAS)
        i.save('uservie.gif',"GIF")
        canvas = tkinter.Canvas(win, height=crea_height,width=crea_width,)
        image_file = tkinter.PhotoImage(file=r"C:\Users\MyPC\PycharmProjects\dafsdf\uservie.gif")
        canvas.create_image(0, 0, anchor='nw',image=image_file)
        canvas.create_line(100,0,100,750,fill='white')
        canvas.pack()
        self.userview=win
        menubar12=tkinter.Menu(win)
        self.userview.config(menu=menubar12)
        menu1 = tkinter.Menu(menubar12, tearoff=False)
        menu2 = tkinter.Menu(menubar12, tearoff=False)
        menubar12.add_cascade(label="系统", menu=menu1)
        menubar12.add_cascade(label="帮助", menu=menu2)
        menu1.add_separator()
        menu1.add_command(label='退出', command=sys.exit)
        self.userview.geometry('1000x750+200+20')
        canvas.create_text(450, 30,text='欢  迎  使  用  银  行  管  理  系  统',fill='red',font=('宋体', 25))
        button1 = tkinter.Button(self.userview,text='查询',command = lambda:self.jumps('查询'),width=11, height=2)
        button1.place(x=10,y=70)
        button2 = tkinter.Button(self.userview,text='取款',command =lambda:self.jumps('取款'),width=11,height=2)
        button2.place(x=10,y=130)
        button3 = tkinter.Button(self.userview,text='存款',command =lambda:self.jumps('存款'), width=11, height=2)
        button3.place(x=10,y=190)
        button4 = tkinter.Button(self.userview,text='转账',command = lambda:self.jumps('转账'),width=11, height=2)
        button4.place(x=10,y=250)
        button5 = tkinter.Button(self.userview, text='改密', command=lambda:self.jumps('改密'),width=11, height=2)
        button5.place(x=10, y=310)
        button6 = tkinter.Button(self.userview,text='冻结',command = lambda:self.jumps('冻结'),width=11, height=2)
        button6.place(x=10,y=370)
        button7 = tkinter.Button(self.userview,text='补卡',command =lambda:self.jumps('补卡'), width=11, height=2)
        button7.place(x=10,y=430)
        button8 = tkinter.Button(self.userview,text='销户',command=lambda:self.jumps('销户'),width=11, height=2)
        button8.place(x=10, y=490)
        win.mainloop()
    #跳转
    def jumps(self,data):
        asd =data
        if asd == '查询':
            self.show_seach()
        if asd == '存款':
            self.deposit_number()
        if asd == '取款':
            self.withdraw_money_number()
        if asd == '转账':
            self.transfe_show()
        if asd == '改密':
            self.change_passward_show()
        if asd== '冻结':
            self.frozen_show()
        if asd == '销户':
            self.sales_show()
        if asd == '补卡':
            self.supplement_card_show()
    #查询
    def show_seach(self):
        win = tkinter.Tk()
        win.title("查询")
        seach_view=win
        seach_view.wm_attributes('-topmost',True)
        seach_view.geometry('420x320+400+180')
        accesss=True
        a= '您的余额为：'+str(self.userVer.searchVer(self.sucess_name))
        lable = tkinter.Label(seach_view,font =('楷体',20),width=20, height=6,text=a)
        lable.pack()
        button1 = tkinter.Button(seach_view, text='返回',width=7,height=2,command=seach_view.destroy)
        button1.pack()
    # 输入取款的钱数显示
    def withdraw_money_number(self):
        win = tkinter.Toplevel()
        win.title("取款")
        win.wm_attributes('-topmost', True)
        withdraw_money_view = win
        withdraw_money_view.geometry('420x320+400+180')
        lable2 = tkinter.Label(withdraw_money_view,text='取款金额：')
        lable2.place(x=80,y=100)
        user_prestore_money=tkinter.IntVar()
        entry = tkinter.Entry(withdraw_money_view,textvariable =user_prestore_money)
        entry.place(x=150,y=100)
        button1 = tkinter.Button(withdraw_money_view, text='返回', width=6, height=1,command=withdraw_money_view.destroy)
        button1.place(x=200,y=150)
        #取款
        def withdraw_money_number_confirm():
            money =user_prestore_money.get()
            if money>=0:
                if self.userVer.withdraw_money(self.sucess_name,money):
                    a = '您的余额为：' + str(self.userVer.searchVer(self.sucess_name))
                    lable1 = tkinter.Label(withdraw_money_view,font =('楷体',20), text=a)
                    lable1.place(x=90,y=20)
                else:
                    showinfo(title='错误提示：', message='余额不足')
            else:
                showinfo(title='错误提示：', message='取款不能小于0')
        button = tkinter.Button(withdraw_money_view, text='确定',command=withdraw_money_number_confirm,width=6, height=1)
        button.place(x=100,y=150)
        win.mainloop()
#     # 存款金额显示
    def deposit_number(self):
        win = tkinter.Toplevel()
        win.title("存款")
        win.wm_attributes('-topmost', True)
        deposit_number=win
        deposit_number.geometry('420x320+400+180')
        lable2 = tkinter.Label(deposit_number,text='存款金额：')
        lable2.place(x=80,y=100)
        user_deposit_money=tkinter.IntVar()
        entry = tkinter.Entry(deposit_number,textvariable =user_deposit_money)
        entry.place(x=150,y=100)
        button1 = tkinter.Button(deposit_number,text='返回',width=6, height=1,command=deposit_number.destroy)
        button1.place(x=200,y=150)
        #存款
        def deposit_money_number_confirm():
            money = user_deposit_money.get()
            if money>=0:
                if self.userVer.deposit_money(self.sucess_name,money):
                    a = '您的余额为：' + str(self.userVer.searchVer(self.sucess_name))
                    lable1 = tkinter.Label(deposit_number,font =('楷体',20), text=a)
                    lable1.place(x=90,y=20)
            else:
                showinfo(title='错误提示：', message='存款不能小于0')
        button = tkinter.Button(deposit_number, text='确定', width=6,  height=1,command=deposit_money_number_confirm)
        button.place(x=100,y=150)
        win.mainloop()
#     # 转账显示
    def transfe_show(self):
        win=tkinter.Toplevel()
        win.title("转账")
        win.wm_attributes('-topmost', True)
        win.geometry('430x300+400+180')
        lable3 = tkinter.Label(win,text='转账账户：')
        lable3.pack()
        transfer_name=tkinter.IntVar()
        entry11 = tkinter.Entry(win,textvariable=transfer_name)
        entry11.pack()
        lable4 = tkinter.Label(win,text='确认账户：')
        lable4.pack()
        transfer_account_confirm=tkinter.IntVar()
        entry2 = tkinter.Entry(win,textvariable=transfer_account_confirm)
        entry2.pack()
        lable2 = tkinter.Label(win,text='转账金额：')
        lable2.pack()
        transfe_mo = tkinter.IntVar()
        entry = tkinter.Entry(win,textvariable =transfe_mo)
        entry.pack()
        button1 = tkinter.Button(win, text='返回', width=6, height=1,command=win.destroy)
        button1.place(x=250,y=150)
        def transfe_money():
            money = transfe_mo.get()
            data = self.userVer.transfe_money(self.sucess_name,
                                              transfer_name,
                                              transfer_account_confirm,money)
            if money>=0:
                if data != "transfer_error":
                    if data != "transfer_confirm_error":
                        if data != "money_error":
                            a = '您的余额为：' + str(self.userVer.searchVer(self.sucess_name))
                            lable1 = tkinter.Label(win,font =('楷体',20), text=a)
                            lable1.place(x=100,y=200)
                        else:
                            showinfo(title='错误提示：', message='余额不足')
                    else:
                        showinfo(title='错误提示：',message='两次输入的账户不一致')
                else:
                    showinfo(title='错误提示：',message='转账的账户不存在')
            else:
                showinfo(title='错误提示：',message='转账金额要大于0')
        button = tkinter.Button(win, text='确定',width=6,height=1,command=transfe_money)
        button.place(x=130,y=150)
        win.mainloop()
#     #改密显示
    def change_passward_show(self):
        win = tkinter.Toplevel()
        win.title("改密")
        win.wm_attributes('-topmost', True)
        win.geometry('430x300+400+180')
        lable3 = tkinter.Label(win, text='原密码：')
        lable3.pack()
        od_pass=tkinter.Variable()
        entry1 = tkinter.Entry(win,textvariable=od_pass)
        entry1.pack()
        lable4 = tkinter.Label(win, text='新密码：')
        lable4.pack()
        user_passward = tkinter.Variable()
        entry2 = tkinter.Entry(win,textvariable=user_passward)
        entry2.pack()
        lable2 = tkinter.Label(win,text='确认密码：')
        lable2.pack()
        user_ce_passward = tkinter.Variable()
        entry = tkinter.Entry(win,textvariable =user_ce_passward)
        entry.pack()
        button1 = tkinter.Button(win, text='返回',width=6, height=1,command=win.destroy)
        button1.place(x=250,y=150)
        #改密
        def change_password():
            data = self.userVer.change_password(self.sucess_name,od_pass,user_passward,user_ce_passward)
            if data != 'old_password_error':
                if data != 'password_format_error':
                    if data != 'password_error':
                        showinfo(title='提示：',message='改密成功，您的新密码为：{}'.format(user_passward.get()))
                    else:
                        showinfo(title='错误提示：',message='两次密码不一致')
                else:
                    showinfo(title='错误提示：',message='新密码格式错误，请输入数字')
            else:
                showinfo(title='错误提示：',message='原密码输入错误')
        button = tkinter.Button(win, text='确定',width=6, height=1,command=change_password)
        button.place(x=130,y=150)
        win.mainloop()
#     #冻结显示
    def frozen_show(self):
        win = tkinter.Toplevel()
        win.title("冻结")
        win.wm_attributes('-topmost', True)
        win.geometry('430x300+400+180')
        lable3 = tkinter.Label(win, text='冻结账户：')
        lable3.pack()
        frozen_name=tkinter.Variable()
        entry1 = tkinter.Entry(win,textvariable=frozen_name)
        entry1.pack()
        lable4 = tkinter.Label(win, text='身份证号：')
        lable4.pack()
        frozen_id_card= tkinter.Variable()
        entry2 = tkinter.Entry(win,textvariable=frozen_id_card)
        entry2.pack()
        lable2 = tkinter.Label(win, text='预留电话：')
        lable2.pack()
        frozen_phone= tkinter.Variable()
        entry = tkinter.Entry(win,textvariable=frozen_phone)
        entry.pack()
        button1 = tkinter.Button(win, text='返回', width=6, height=1,command=win.destroy)
        button1.place(x=250,y=150)
        i=0
        def user_frozen():
            data = self.userVer.user_frozen(self.sucess_name,frozen_name,frozen_id_card,frozen_phone,i)
            if data !='account_error':
                if data != 'id_number_error':
                    if data != 'phone_error':
                        if i ==0:
                            showinfo(title='提示：',message='冻结成功')
                        elif i ==1:
                            showinfo(title='提示：',message='解冻成功')
                    else:
                        showinfo(title='错误提示：',message='手机号错误')
                else:
                    showinfo(title='错误提示：',message='身份证号错误')
            else:
                showinfo(title='错误提示：',message='账号错误')
        button = tkinter.Button(win, text='确定',width=6, height=1,command=user_frozen)
        button.place(x=130,y=150)
        win.mainloop()
#     #补卡显示
    def supplement_card_show(self):
        win = tkinter.Toplevel()
        win.title("补卡")
        win.wm_attributes('-topmost', True)
        win.geometry('430x300+400+180')
        lable4 = tkinter.Label(win, text='身份证号：')
        lable4.pack()
        supp_id_card=tkinter.Variable()
        entry2 = tkinter.Entry(win,textvariable=supp_id_card)
        entry2.pack()
        lable2 = tkinter.Label(win,text='预留电话：')
        lable2.pack()
        supp_phone=tkinter.Variable()
        entry = tkinter.Entry(win,textvariable=supp_phone)
        entry.pack()
        supp_r = tkinter.Variable()
        supp_r.set(1)
        radiobutton = tkinter.Radiobutton(win,text='不重置密码',value=1,variable=supp_r)
        radiobutton.place(x=130,y=100)
        radiobutton = tkinter.Radiobutton(win,text='重置密码', value=0,variable=supp_r,)
        radiobutton.place(x=250,y=100)
        button1 = tkinter.Button(win, text='返回',width=6, height=1,command=win.destroy)
        button1.place(x=250,y=150)
        def supplement_card_confirm():
            data = self.userVer.supplement_card(supp_id_card,supp_phone,supp_r)
            if data != "idnumber_error":
                if data != "phone_error":
                    if data ==True:
                        if supp_r.get()==0:
                            showinfo(title='提示：',message='补卡成功\n你的新卡号为：{}\n密码已重置\n密码：666666\n请尽快修改密码'.format(self.userVer.supp_searchVer(supp_id_card)))
                        else:
                            showinfo(title='提示：',message='补卡成功\n你的新卡号为:{}'.format(self.userVer.supp_searchVer(supp_id_card)))
                    else:
                        showinfo(title='错误提示：',message='补卡失败请重试')
                else:
                    showinfo(title='错误提示：',message='电话输入错误')
            else:
                showinfo(title='错误提示：',message='身份证号输入错误')
        button = tkinter.Button(win, text='确定',width=6, height=1,command=supplement_card_confirm)
        button.place(x=130,y=150)
        win.mainloop()
    #销户显示
    def sales_show(self):
        win = tkinter.Toplevel()
        win.geometry('430x300+400+180')
        win.title("销户")
        win.wm_attributes('-topmost', True)
        lable4 = tkinter.Label(win, text='身份证号：')
        lable4.pack()
        sales_id_card= tkinter.Variable()
        entry2 = tkinter.Entry(win,textvariable=sales_id_card)
        entry2.pack()
        lable2 = tkinter.Label(win,text='预留电话：')
        lable2.pack()
        sales_phone=tkinter.Variable()
        entry = tkinter.Entry(win,textvariable=sales_phone)
        entry.pack()
        button1 = tkinter.Button(win, text='返回',width=6, height=1,command=win.destroy)
        button1.place(x=250,y=100)
        def sales_confirm():
            data = self.userVer.sales(self.sucess_name,
        sales_id_card,sales_phone)
            if data != "idnumber_error":
                if data != "phone_error":
                    if data ==True:
                        showinfo(title='提示：',message='销户成功')
                        sys.exit()
                    else:
                        showinfo(title='错误提示：',message='销户失败请重试')
                else:
                    showinfo(title='错误提示：',message='电话输入错误')
            else:
                showinfo(title='错误提示：',message='身份证号输入错误')
        button = tkinter.Button(win, text='确定', width=6, height=1,command=sales_confirm)
        button.place(x=130,y=100)
        win.mainloop()