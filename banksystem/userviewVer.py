# -*- coding:utf-8 -*-
from sqlOperation import SqlOperation
import random
import re
import time
import datetime
class UserviewVer():
    def __init__(self):
        self.db= SqlOperation()
        self.scond = 0
    #正则表达式验证
    def reVer(self,pat,str):
        res = re.match(pat,str)
        if res != None:
            return True
        return False
    #开户验证
    def openviewVer(self,username,idnumber,phone,money,password,confirm_passward):
        username = username.get()
        idnumber = str(idnumber.get())
        phone = str(phone.get())
        money = str(money.get())
        password = str(password.get())
        confirm_passward = confirm_passward.get()
        p = True
        input_error = ""
        if len(username)>1:
            if len(idnumber) ==18:
                pat = r'[1-9]\d{17}'
                if self.reVer(pat,idnumber):
                    if len(phone) ==11:
                        pat = r'^1[3,5,7,8][0,1,2,3,5,6,7,8,' \
                              r'9]\d{8}'
                        if self.reVer(pat,phone):
                            pat = r'[0-9]\d*'
                            if self.reVer(pat,money):
                                if int(money) > 0:
                                    if self.reVer(pat,password):
                                        if password == \
                                                confirm_passward:
                                            sql = "select * from userinfor where idnumber ='%s'"%idnumber
                                            if  self.db.get_one(sql) == None:
                                                while p :
                                                    card_id = random.randint(10000, 100000)
                                                    sql = "select * from userinfor where " \
                                                      "card_id ='%d'" % card_id
                                                    if self.db.get_one(sql) == None:
                                                        p = False
                                                        sqlinsert = "insert into userinfor  values(%d,'%s',%s,%s,%d, %d,1,curdate());"%(card_id,username,phone,idnumber,int(money),int(password))
                                                        self.db.sqlInsert(sqlinsert)
                                                        return card_id
                                            else:
                                                input_error ='idnumber_error'
                                        else:
                                            input_error = 'con_password_format_error'
                                    else:
                                        input_error = 'password_format_error'
                                else:
                                    input_error = 'money_len_error'
                            else:
                                input_error = 'money_format_error'
                        else:
                            input_error = 'phone_format_error'
                    else:
                        input_error = 'phone_len_error'
                else:
                    input_error = 'idnumber_format_error'
            else:
                input_error ="idnumber_len_error"
        else:
            input_error = "name_len_error"
        return input_error
    #用户登录验证
    def user_verify(self,cardID,password):
        input_error = ''
        cardID = cardID
        password = int(password)
        sql = "select * from userinfor where card_id  ='%d'"%cardID
        data = self.db.get_one(sql)
        if data!= None:
            if data[6] == 1:
                if self.scond <3:
                    if data[5]==password:
                        self.scond = 0
                        return True
                    else:
                        self.scond += 1
                        input_error = 'password_error'
                else:
                    sql = "update userinfor set feed =0 where card_id=%d" % (cardID)
                    self.scond = 0
                    self.db.sqlInsert(sql)
                    input_error ='scond_error'
            else:
                input_error = 'feed_error'
        else:
            input_error = 'cardID_error'
        return input_error
    #查询验证
    def searchVer(self,cardID):
        money = 0
        sql = "select * from userinfor where card_id =%d" % cardID
        data = self.db.get_one(sql)
        money = data[4]
        return money
    #取款验证
    def withdraw_money(self,cardID,money):
        mon = self.searchVer(cardID)
        money = mon - int(money)
        if money>0:
            sql1 = "update userinfor set money =%d where card_id=%d"%(money,cardID)
            self.db.sqlInsert(sql1)
            return True
        else:
            return False
    #存款验证
    def deposit_money(self,cardID,money):
        mon = self.searchVer(cardID)
        money = mon + int(money)
        sql1 = "update userinfor set money =%d where card_id=%d"%(money,cardID)
        self.db.sqlInsert(sql1)
        return True
    #转账验证
    def transfe_money(self,account,transfer_account,
                      transfer_account_confirm,money):
        transfer_account = transfer_account.get()
        transfer_account_confirm = transfer_account_confirm.get()
        input_error = ''
        sql= "select * from userinfor where card_id " \
        "='%d'" % transfer_account
        transfer = self.db.get_one(sql)
        if transfer !=None:
            if transfer_account ==transfer_account_confirm:
                if self.withdraw_money(account,money):
                    self.deposit_money(transfer_account,money)
                    return True
                else:
                    input_error = 'money_error'
            else:
                input_error = 'transfer_confirm_error'
        else:
            input_error = 'transfer_error'
        return input_error
    #改密
    def change_password(self,accent,old_password,new_password,new_password_confirm):
        input_error = ''
        accent = accent
        old_password = int(old_password.get())
        sql = "select * from userinfor where card_id " \
              "='%d'"%accent
        data = self.db.get_one(sql)
        if data[5] == old_password:
            new_password = new_password.get()
            pat = r'[0-9]\d*'
            if self.reVer(pat,str(new_password)):
                new_password_confirm = new_password_confirm.get()
                if new_password == new_password_confirm:
                    sql = "update userinfor set password =%d where card_id=%d"%(int(new_password),accent)
                    self.db.sqlInsert(sql)
                    return True
                else:
                    input_error = 'password_error'
            else:
                input_error = 'password_format_error'
        else:
            input_error = 'old_password_error'
        return input_error
    #冻结
    def user_frozen(self,account,f_name,id_card,phone,i):
        input_error = ''

        f_name = int(f_name.get())
        sql = "select * from userinfor where card_id " \
              "='%d'" %f_name
        data = self.db.get_one(sql)
        id_card = id_card.get()
        phone = phone.get()
        i = int(i)
        if account == f_name:
            if data[3] == id_card:
                if data[2] == phone:
                    sql = "update userinfor set feed =%d where " \
                           "card_id=%d"%(i,f_name)
                    self.db.sqlInsert(sql)
                    return True
                else:
                    input_error = 'phone_error'
            else:
                input_error = 'id_number_error'
        else:
            input_error = 'account_error'
        return input_error
    #补卡
    def supplement_card(self,idnumber,phone,reset):
        input_error = ''
        p = True
        idnumber = idnumber.get()
        phone = phone.get()
        reset = reset.get()
        sql = "select * from userinfor where idnumber " \
              "='%s'" %idnumber
        data = self.db.get_one(sql)
        if data != None:
            if data[2] == phone:
                while p:
                    card_id = random.randint(10000, 100000)
                    sql = "select * from userinfor where " \
                          "card_id ='%d'" % card_id
                    if self.db.get_one(sql) == None:
                        p = False
                        sql = "update userinfor set card_id =%d " \
                      "where idnumber=%s"%(card_id,idnumber)
                        self.db.sqlInsert(sql)
                        if reset == 0:
                            sql = "update userinfor set " \
                                  "password =666666 " \
                                  "where idnumber=%s" % (idnumber)
                            self.db.sqlInsert(sql)
                        return True
            else:
                input_error = 'phone_error'
        else:
            input_error = 'idnumber_error'
        return input_error
    def supp_searchVer(self,idcard):
        cardid = 0
        sql = "select * from userinfor where idnumber " \
              "=%s" % idcard.get()
        data = self.db.get_one(sql)
        cardid = data[0]
        return cardid
    #销户
    def sales(self,account,idnumber,phone):
        input_error = ''
        idnumber = idnumber.get()
        phone = phone.get()
        sql = "select * from userinfor where card_id " \
              "='%d'"%account
        data = self.db.get_one(sql)
        if data[3] == idnumber:
            if data[2] == phone:
                sql = 'delete from userinfor where ' \
                      'card_id = %d'%account
                self.db.sqlInsert(sql)
                return True
            else:
                input_error = 'phone_error'
        else:
            input_error = 'idnumber_error'
        return input_error
#忘记密码
    def forget_password(self,account,idcard,phone):
        account = int(account.get())
        idcard=idcard.get()
        phone=phone.get()
        sql = "select * from userinfor where card_id " \
              "='%d'" % account
        input_error = ''
        data = self.db.get_one(sql)
        if data !=None:
            if data[3]==idcard:
                if data[2]==phone:
                    newpas=999999
                    sql = "update userinfor set password " \
                          "=%d where card_id=%d" % (
                    newpas, account)
                    self.db.sqlInsert(sql)
                    return True
                else:
                    input_error='phone_error'
            else:
                input_error = 'idcard_error'
        else:
            input_error='account_error'
        return input_error
    def thaw_account(self,account,idcard,phone):
        account = int(account.get())
        idcard=idcard.get()
        phone=phone.get()
        sql = "select * from userinfor where card_id " \
              "='%d'" % account
        input_error = ''
        data = self.db.get_one(sql)
        if data !=None:
            if data[3]==idcard:
                if data[2]==phone:
                    i=1
                    sql = "update userinfor set feed =%d " \
                          "where " \
                          "card_id=%d" % (i, account)
                    self.db.sqlInsert(sql)
                    return True
                else:
                    input_error='phone_error'
            else:
                input_error = 'idcard_error'
        else:
            input_error='account_error'
        return input_error



