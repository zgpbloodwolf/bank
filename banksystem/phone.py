import random
def writ_filetxt(html,topath):
    with open(topath,'a') as f:
        f.write(html)
topath = r"/数据材料/phone.txt"
phonelist=[]
for n in range(1,1000000):
    i = random.choice([3,5,7,8])
    k =random.choice([0,1,2,3,5,6,7,8,9])
    j =random.randint(0,99)
    l =random.randint(0,99)
    m = random.randint(0, 99)
    o = random.randint(0, 99)
    phonenumber = str(1)+str(i)+str(k)+str(j)+str(l)+str(m)+str(o)
    if len(phonenumber) == 11:
        if phonenumber not in phonelist:
            phonelist.append(phonenumber)
            writ_filetxt(phonenumber+'\n',topath)