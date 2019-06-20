from sqlOperation import SqlOperation
class AdmisVer():
    def __init__(self,accountNumber,password):
        self.accountNumber = accountNumber
        self.password = password
    #’À∫≈√‹¬Î—È÷§
    def admisvarifiction(self):
        db = SqlOperation()
        sql = "select * from administrators where account ='%s'"%self.accountNumber
        data = db.get_one(sql)
        if data != None:
            if data[1] == self.password:
                return True
        return False