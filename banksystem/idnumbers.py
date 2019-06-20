import urllib.request
import ssl
import re
def writ_filetxt(html,topath):
    with open(topath,'a') as f:
        f.write(html)
topath=r"C:\Users\MyPC\PycharmProjects\银行管理系统 - 副本\数据材料\112.txt"
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
    HTML = response.read().decode("utf-8")
    # with open(r'C:\Users\MyPC\PycharmProjects\数据库资料\xiushi'
    #           r'.html','wb') as f:
    #     f.write(HTML)
    pat = r'<div id="contents"(.*?)<div class="pages">'
    re_joke = re.compile(pat,re.S)
    divlist = re_joke.findall(HTML)
    print(divlist[0])
    writ_filetxt(divlist[0],topath)
i=2
for i in range(2,9):
    url = r"http://www.wendangku.net/doc/eb368df77fd5360cbb1adb1b-"+str(i)+".html"
    info = xiushi(url)