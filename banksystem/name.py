import urllib.request
import ssl
import re
def xiushi(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; "
                      "WOW64) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) Chrome/63.0.3239.26 "
                      "Safari/537.36 Core/1.63.5514.400 "
                      "QQBrowser/10.1.1660.400"}
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    htmls = response.read().decode("utf-8")
    # with open(r'C:\Users\MyPC\PycharmProjects\银行管理系统 - 副本\数据材料\1.html','wb+') as f:
    #     f.write(htmls)
    # print(htmls)
    pat = r'<div class="listbox1_text">(.*?)<div class="clear">'
    re_joke = re.compile(pat,re.S)
    divlist = re_joke.findall(htmls)
    # print(len(divlist))
    for div in divlist:
    #     #姓名
        re_u = re.compile(r"<li>(.*?)</li>",re.S)
        names = re_u.findall(div)
        for name in names:
            name = name.strip()
            print(name)
            writename(name+'\n')
    return name
def writename(name):
    with open(r"/数据材料/name.txt","a") as f:
        f.write(name)
for i in range(1,100):
    for j in [0,1]:
        try:
            url = r"https://www.yw11.com/html/mi/3-"+str(i)+"-"+str(j)+"-1.htm"
            info = xiushi(url)
        except:
            pass