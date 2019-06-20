from userview import *
from tkinter.messagebox import showinfo
from tkinter import *
from PIL import Image,ImageTk
from verification import Verification
from userviewVer import UserviewVer
class Admis():
    def __init__(self):
        self.userVer=UserviewVer()
        self.imagess = Verification()
    def creat_page(self):
        win = tkinter.Tk()
        win.title('欢迎注册')
        win.resizable(width=False, height=False)
        i = Image.open('de.gif')
        i = i.resize((1000, 750), Image.ANTIALIAS)
        i.save('de.gif', "GIF")
        canvas = tkinter.Canvas(win, height=750,width=1000)
        # 创建画布
        image_file = tkinter.PhotoImage(file=r"C:\Users\MyPC\PycharmProjects\dafsdf\de.gif")
        canvas.create_image(0, 0, anchor='nw',image=image_file)
        canvas.pack()
        self.mainview=win
        self.mainview.geometry('1000x750+200+20')
        self.title = canvas.create_text(500 ,90 ,text ='欢迎使用银行自助系统'
        ,fill = 'red',font = ('宋体',50))
        self.name=canvas.create_text(250 ,250 ,text = '     账号：'
        ,fill = 'red',font = ('宋体',25))
        self.name=canvas.create_text(250, 300,text='     密码：', fill='red',font=('宋体', 25))
        self.admis_name = tkinter.Variable()
        entr1 = tkinter.Entry(self.mainview,textvariable =self.admis_name,font=('宋体', 25))
        entr1.place(x=330,y=230)
        ad_nam =canvas.create_text(750, 250,text='',fill='red', font=('宋体',15))
        def ad_na(event):
            if self.admis_name.get()=='':
                canvas.itemconfig(ad_nam,text='账号不能为空',fill='red',font=('宋体',15))
            else:
                canvas.itemconfig(ad_nam, text='',fill='red', font=('宋体',15))
        entr1.bind('<FocusOut>', ad_na)
        self.admis_password = tkinter.Variable()
        entr2 = tkinter.Entry(self.mainview, show='*',font=('宋体', 25),textvariable=self.admis_password)
        entr2.place(x=330,y=280)
        ad_pas = canvas.create_text(750, 300,text='',fill='red', font=('宋体',15))
        def ad_p(event):
            if self.admis_password.get()=='':
                canvas.itemconfig(ad_pas,text='密码不能为空',fill='red',font=('宋体',15))
            else:
                canvas.itemconfig(ad_pas, text='',fill='red', font=('宋体',15))
        entr2.bind('<FocusOut>', ad_p)
        canvas.create_text(275, 350, text='验证码：',fill='red',font=('宋体', 25))
        i = self.imagess.verif()
        im =ImageTk.PhotoImage(image=i)
        self.Verification = tkinter.Variable()
        entr3 = tkinter.Entry(self.mainview,width=5,font=('宋体', 25),textvariable=self.Verification)
        entr3.place(x=330,y=330)
        ad_ver=canvas.create_text(620, 353, text='', fill='red',font=('宋体', 20))
        def ad_verif(event):
            if self.Verification.get().upper() ==self.imagess.verification_code.upper():
                canvas.itemconfig(ad_ver, text='', fill='red', font=('宋体',15))
            else:
                canvas.itemconfig(ad_ver, text='验证码错误',fill='red', font=('宋体',15))
        entr3.bind('<FocusOut>',ad_verif)
        self.lable3 = tkinter.Button(self.mainview,image=im,bd=0,command=self.change_verification)
        self.lable3.image = im
        self.lable3.place(x=430,y=335)
        button1 = tkinter.Button(self.mainview,text = '登录',width = 10,height = 2,command = self.login)
        button1.place(x=330,y=400)
        button2 = tkinter.Button(self.mainview, text='注册',width=10, height=2,command =self.openview)
        button2.place(x=460,y=400)
        button2 = tkinter.Button(self.mainview, text='其他',width=10,height=2, command=self.other_function)
        button2.place(x=590, y=400)
        win.mainloop()
    #验证码变换
    def change_verification(self):
        i = self.imagess.verif()
        im = ImageTk.PhotoImage(image=i)
        self.lable3 = tkinter.Button(self.mainview,image=im,bd=0,command=self.change_verification)
        self.lable3.image = im
        self.lable3.place(x=430,y=335)
    #验证密码登录
    def login(self):
        try:
            if self.Verification.get().upper() == self.imagess.verification_code.upper():
                data = self.userVer.user_verify(int(self.admis_name.get()),self.admis_password.get())
                self.change_verification()
                if data!="cardID_error":
                    if data != "feed_error":
                        if data != "scond_error":
                            if data != "password_error":
                                self.mainview.destroy()
                                Userview(int(self.admis_name.get())).creat_page()
                            else:
                                showinfo(title='错误提示',message='密码错误')
                        else:
                            showinfo(title='错误提示', message='错误次数过多，您的卡已被冻结')
                    else:
                        showinfo(title='错误提示',message='您的账号已被冻结')
                else:
                    showinfo(title='错误提示',message='账号不存在，请注册')
            else:
                self.Verification.set('')
                showinfo(title='错误提示', message='验证码错误')
        except:
            showinfo(title='错误提示', message='账号，密码不能为空')
    #注册开户
    def openview(self):
        self.mainview.destroy()
        win = tkinter.Tk()
        win.title('欢迎注册')
        win.resizable(width=False, height=False)
        i = Image.open('zhu.gif')
        i = i.resize((1000, 750), Image.ANTIALIAS)
        i.save('zhu.gif', "GIF")
        canvas = tkinter.Canvas(win, height=750, width=1000)  # 创建画布
        image_file = tkinter.PhotoImage(file=r"C:\Users\MyPC\PycharmProjects\dafsdf\zhu.gif")
        canvas.create_image(0, 0, anchor='nw',image=image_file)
        canvas.pack()
        self.openv=win
        self.openv.geometry('1000x750+200+20')
        win.resizable(width=False, height=False)
        canvas.create_text(330, 250, text='姓名：',fill='black',font=('宋体', 20))
        self.user_name=tkinter.Variable()
        entry1 = tkinter.Entry(self.openv,font=('宋体',20),textvariable =self.user_name)
        entry1.place(x=360,y=235)
        op_name=canvas.create_text(710, 255, text='',fill='red',font=('宋体',15))
        def op_na(event):
            if self.user_name.get()=='':
                canvas.itemconfig(op_name,text='姓名不能为空',fill='red',font=('宋体',15))
            else:
                canvas.itemconfig(op_name, text='',fill='red', font=('宋体',15))
        entry1.bind('<FocusOut>', op_na)
        canvas.create_text(288, 300, text='身份证号码：',fill='black', font=('宋体', 20))
        self.id_card=tkinter.Variable()
        entry2 = tkinter.Entry(self.openv,font=('宋体',20),textvariable=self.id_card)
        entry2.place(x=360,y=285)
        op_id_card = canvas.create_text(740,305,text='',fill='red',font=('宋体', 15))
        def op_id_ca(event):
            if self.id_card.get() == '':
                canvas.itemconfig(op_id_card,text='身份证号码不能为空',fill='red', font=('宋体',15))
            else:
                canvas.itemconfig(op_id_card, text='',fill='red', font=('宋体',15))
        entry2.bind('<FocusOut>', op_id_ca)
        canvas.create_text(315, 350, text='手机号：',fill='black',font=('宋体', 20))
        self.user_phone_number = tkinter.Variable()
        entry3 = tkinter.Entry(self.openv,font=('宋体', 20), textvariable=self.user_phone_number)
        entry3.place(x=360,y=335)
        op_phone = canvas.create_text(730, 355,text='',fill='red',font=('宋体', 15))
        def op_ph(event):
            if self.user_phone_number.get() == '':
                canvas.itemconfig(op_phone,text='电话号码不能为空',fill='red', font=('宋体',15))
            else:
                canvas.itemconfig(op_phone, text='',fill='red', font=('宋体',15))
        entry3.bind('<FocusOut>', op_ph)
        canvas.create_text(313, 400, text='预存款：',fill='black',font=('宋体', 20))
        self.user_prestore_money=tkinter.IntVar()
        entry4 = tkinter.Entry(self.openv,font=('宋体',20),textvariable=self.user_prestore_money)
        entry4.place(x=360,y=385)
        canvas.create_text(328, 450, text='密码：',fill='black',font=('宋体', 20))
        self.user_passward=tkinter.Variable()
        entry5 = tkinter.Entry(self.openv,show = '*',font=('宋体', 20),textvariable=self.user_passward)
        entry5.place(x=360,y=435)
        op_passward = canvas.create_text(710, 455,text='',fill='red',font=('宋体', 15))
        def op_pas(event):
            if self.user_passward.get() == '':
                canvas.itemconfig(op_passward,text='密码不能为空',fill='red', font=('宋体',15))
            else:
                canvas.itemconfig(op_passward, text='',fill='red', font=('宋体',15))
        entry5.bind('<FocusOut>', op_pas)
        canvas.create_text(298, 500, text='确认密码：',fill='black',font=('宋体', 20))
        self.user_confirm_passward=tkinter.Variable()
        entr6 = tkinter.Entry(self.openv,show = '*',font=('宋体', 20),textvariable = self.user_confirm_passward)
        entr6.place(x=360,y=485)
        canvas.create_text(313, 550, text='验证码：',fill='black',font=('宋体', 20))
        i = self.imagess.verif()
        im = ImageTk.PhotoImage(image=i)
        self.ver=tkinter.Variable()
        entr3 = tkinter.Entry(self.openv, width=5,font=('宋体', 20),textvariable=self.ver)
        entr3.place(x=360, y=535)
        op_ver = canvas.create_text(630,555, text='', fill='red',font=('宋体', 15))
        def ad_verif(event):
            if self.ver.get().upper() ==self.imagess.verification_code.upper():
                canvas.itemconfig(op_ver, text='',fill='red', font=('宋体',15))
            else:
                canvas.itemconfig(op_ver, text='验证码错误',fill='red', font=('宋体',15))

        entr3.bind('<FocusOut>', ad_verif)
        lable3 = tkinter.Button(self.openv,image=im, bd=0,command=self.user_change_verification)
        lable3.image = im
        lable3.place(x=440, y=535)
        buttom = tkinter.Button(self.openv, text='返回',width=10,height=2,command = lambda:self.renturn(self.openv))
        buttom.place(x=500,y=600)
        buttom = tkinter.Button(self.openv, text='确认',width=10, height=2,command=self.confirm )
        buttom.place(x=360,y=600)
        win.mainloop()
    def user_change_verification(self):
        i = self.imagess.verif()
        im = ImageTk.PhotoImage(image=i)
        lable3 = tkinter.Button(self.openv,image=im, bd=0,command=self.user_change_verification)
        lable3.image = im
        lable3.place(x=440, y=535)
    #注册
    def confirm(self):
        if self.ver.get().upper() ==self.imagess.verification_code.upper():
            data = self.userVer.openviewVer(self.user_name,
                                            self.id_card,
                                            self.user_phone_number,
                                            self.user_prestore_money,
                                            self.user_passward,
                                            self.user_confirm_passward)
            if data != 'name_len_error':
                self.user_change_verification()
                if data != 'idnumber_len_error':
                    if data != 'idnumber_format_error':
                        if data != 'phone_len_error':
                            if data != 'phone_format_error':
                                if data != 'money_format_error':
                                    if data != 'money_len_error':
                                        if data !='password_format_error':
                                            if data !='con_password_format_error':
                                                if data != 'idnumber_error':
                                                    showinfo(title='提示：', message='注册成功\n' + '你的账号为：' + str(data)+'\n' + '请牢记')
                                                    self.openv.destroy()
                                                    self.creat_page()
                                                else:
                                                    showinfo(title='错误提示：',message='该身份证号已注册')
                                            else:
                                                showinfo(title='错误提示：',message='两次输入的密码不一致')
                                        else:showinfo(title='错误提示：',message='密码请输入数字')
                                    else:
                                        showinfo(title='错误提示：',message='预存款请要大于0')
                                else:
                                    showinfo(title='错误提示：',message='预存款请输入数字')
                            else:
                                showinfo(title='错误提示：',message='电话号码格式错误')
                        else:
                            showinfo(title='错误提示：',message='电话号码长度错误')
                    else:
                        showinfo(title='错误提示：',message='身份证号格式错误')
                else:
                    showinfo(title='错误提示：', message='身份证号长度错误')
            else:
                showinfo(title='错误提示：', message='姓名错误')
        else:
            showinfo(title='错误提示：', message='验证码错误')
    def renturn(self,a):
        a.destroy()
        self.creat_page()

#其他功能
    def other_function(self):
        self.mainview.destroy()
        win = tkinter.Tk()
        win.title('其他功能')
        win.resizable(width=False, height=False)
        i = Image.open('oth.gif')
        i = i.resize((1000, 750), Image.ANTIALIAS)
        i.save('oth.gif', "GIF")
        canvas = tkinter.Canvas(win, height=750,width=1000)
        # 创建画布
        image_file = tkinter.PhotoImage(file=r"C:\Users\MyPC\PycharmProjects\dafsdf\oth.gif")
        canvas.create_image(0, 0, anchor='nw',image=image_file)
        canvas.pack()
        self.other = win
        self.other.geometry('1000x750+200+20')
        win.resizable(width=False, height=False)
        canvas.create_text(330, 50, text='账号：',fill='red',font=('宋体', 25))
        for_card_id=tkinter.Variable()
        entry1=tkinter.Entry(self.other, font=('宋体',25),textvariable=for_card_id)
        entry1.place(x=360,y=35)
        canvas.create_text(280, 150, text='身份证号码：',fill='red',font=('宋体', 25))
        fo_id_card = tkinter.Variable()
        entry2 = tkinter.Entry(self.other, font=('宋体',25), textvariable=fo_id_card)
        entry2.place(x=360, y=135)
        op_id_card = canvas.create_text(800, 150, text='',fill='red',font=('宋体', 15))
        def op_id_ca(event):
            if fo_id_card.get() == '':
                canvas.itemconfig(op_id_card,text='身份证号码不能为空',fill='red', font=('宋体',15))
            else:
                canvas.itemconfig(op_id_card, text='',fill='red', font=('宋体',15))
        entry2.bind('<FocusOut>', op_id_ca)
        canvas.create_text(315, 250, text='手机号：',fill='red',font=('宋体', 25))
        fo_phone_number = tkinter.Variable()
        entry3 = tkinter.Entry(self.other, font=('宋体', 25), textvariable=fo_phone_number)
        entry3.place(x=360, y=235)
        op_phone = canvas.create_text(790, 250,text='', fill='red',font=('宋体', 15))
        def op_ph(event):
            if fo_phone_number.get() == '':
                canvas.itemconfig(op_phone,text='电话号码不能为空',fill='red', font=('宋体',15))
            else:
                canvas.itemconfig(op_phone, text='', fill='red', font=('宋体',15))
        entry3.bind('<FocusOut>', op_ph)
        canvas.create_text(313, 350, text='验证码：',fill='red',font=('宋体', 25))
        i = self.imagess.verif()
        im = ImageTk.PhotoImage(image=i)
        self.ver = tkinter.Variable()
        entr3 = tkinter.Entry(self.other, width=5,font=('宋体', 25),textvariable=self.ver)
        entr3.place(x=360, y=335)
        op_ver = canvas.create_text(630, 353, text='',fill='red',font=('宋体', 15))
        def ad_verif(event):
            if self.ver.get().upper() == self.imagess.verification_code.upper():
                canvas.itemconfig(op_ver, text='',fill='red', font=('宋体',15))
            else:
                canvas.itemconfig(op_ver, text='验证码错误',fill='red', font=('宋体',15))
        entr3.bind('<FocusOut>', ad_verif)
        def other_change_verification():
            i = self.imagess.verif()
            im = ImageTk.PhotoImage(image=i)
            lable3 = tkinter.Button(self.other,image=im,bd=0, command=other_change_verification)
            lable3.image = im
            lable3.place(x=460, y=338)
        lable3 = tkinter.Button(self.other,image=im,bd=0,command=other_change_verification)
        lable3.image = im
        lable3.place(x=460, y=338)
        #解冻账号
        def thaw_account():
            i=1
            try:
                th_data=self.userVer.thaw_account(for_card_id,fo_id_card,fo_phone_number)
                if self.ver.get().upper() ==self.imagess.verification_code.upper():
                    if th_data !='account_error':
                        if th_data != 'idcard_error':
                            if th_data != 'phone_error':
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
                else:
                    showinfo(title='错误提示：',message='验证码错误')
            except:
                showinfo(title='错误提示：', message='信息不能为空')
        buttom = tkinter.Button(self.other, text='解冻账号',width=10,height=2,command=thaw_account)
        buttom.place(x=500, y=450)
        # 忘记密码
        def forget_pas():
            try:
                foget_data = self.userVer.forget_password(for_card_id,fo_id_card,fo_phone_number)
                if self.ver.get().upper() ==self.imagess.verification_code.upper():
                    if foget_data !='account_error':
                        if foget_data != 'idcard_error':
                            if foget_data != 'phone_error':
                                showinfo(title='修改成功：', message=' 您的密码为：999999')
                            else:
                                showinfo(title='错误提示：',message='手机号错误')
                        else:
                            showinfo(title='错误提示：',message='身份证号错误')
                    else:
                        showinfo(title='错误提示：',message='账号错误')
                else:
                    showinfo(title='错误提示：', message='验证码错误')
            except:
                showinfo(title='错误提示：', message='信息不能为空')
        buttom1 = tkinter.Button(self.other, text='忘记密码', width=10,height=2,command=forget_pas)
        buttom1.place(x=360, y=450)
        buttom2 = tkinter.Button(self.other, text='返回',width=10,height=2,command=lambda:self.renturn(self.other))
        buttom2.place(x=640, y=450)
        win.mainloop()
if __name__=='__main__':
    a = Admis()
    a.creat_page()
