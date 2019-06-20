import random
import re
with open(r"C:\Users\MyPC\PycharmProjects\银行管理系统 - 副本\数据材料\112.txt",'r') as f:
    list1 =f.read()
a = re.compile(r"\d{6}").findall(list1)
idnumbers=[]
def writ_filetxt(html,topath):
    with open(topath,'a') as f:
        f.write(html)
topath = r"C:\Users\MyPC\PycharmProjects\银行管理系统 - 副本\数据材料\IdNumber.txt"
for i in range(10000):
    c = random.choice(a)
    year1 = random.choice([194,195,196,197,198,199,200,201])
    year2 = random.randint(0,9)
    year = str(year1)+str(year2)
    month = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12'])
    daylist=['10','20','30','31']
    for j in range(10000):
        day1 = random.choice([0,1,2])
        day2 = random.randint(1,9)
        days = str(day1)+str(day2)
        if days not in daylist:
            daylist.append(days)
    day = random.choice(daylist)
    id1= random.randint(0,9)
    id2= random.randint(0,9)
    id3= random.randint(0,9)
    id4= random.randint(0,9)
    id = str(id1)+str(id2)+str(id3)+str(id4)
    idnumber = c+year+month+day+id
    if idnumber not in idnumbers:
        print(i)
        idnumbers.append(idnumber)
        writ_filetxt(idnumber+'\n',topath)