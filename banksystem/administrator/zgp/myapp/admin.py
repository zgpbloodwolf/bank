# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Userinfor


# Register your models here.
@admin.register(Userinfor)
class UserinforAdmin(admin.ModelAdmin):
    def cardId(self):
        return  self.card_id
    cardId.short_description = '卡号'
    def nae(self):
        return self.name
    nae.short_description = '姓名'
    def phon(self):
        return self.phone
    phon.short_description = '电话号码'
    def namID(self):
        return self.idnumber
    namID.short_description = '身份证号码'
    def moey(self):
        return self.money
    moey.short_description = '存款'
    def fe(self):
        return self.feed
    fe.short_description = '冻结状态'
    def pas(self):
        return self.password
    pas.short_description = '密码'
    def tim(self):
        return self.satime
    tim.short_description = '日期'
    list_display = [cardId, nae, phon,
                    namID,moey,fe,pas,tim]
    search_fields = ['name','card_id','idnumber']
    list_per_page = 5
admin.site.site_header='银行管理系统'
admin.site.site_title='银行管理系统'