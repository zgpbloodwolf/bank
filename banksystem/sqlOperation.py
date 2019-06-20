# -*- coding:utf-8 -*-
import pymysql
class SqlOperation():
    def connet(self):
        self.db = pymysql.connect('localhost', 'root',
                                  '123456','bank_systems')
        self.cutsor = self.db.cursor()
    def close(self):
        self.cutsor.close()
        self.db.close()
    def get_one(self,sql):
        res = None
        try:
            self.connet()
            self.cutsor.execute(sql)
            res = self.cutsor.fetchone()
            self.close()
        except:
            pass
        return res
    def sqlInsert(self,sql):
        try:
            self.connet()
            self.cutsor.execute(sql)
            self.db.commit()
        except:
            # 插入失败时回归
            self.db.rollback()