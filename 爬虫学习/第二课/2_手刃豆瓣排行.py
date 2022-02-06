#拿到页面源代码
#通过re来提取有效信息
import requests
import re
import csv

for index in range(0,250,25):
    url = f"https://movie.douban.com/top250?start={index}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
    }
    resp = requests.get(url,headers = headers)
    page_content = resp.text
    resp.close()

    #解析数据
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?'
    r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
    r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
    r' <span>(?P<comments>.*?)</span>',re.S)

    ret = obj.finditer(page_content)
    file = open("data.csv",mode = "a",newline = "",encoding = "utf-8")
    csvwriter = csv.writer(file)
    for i in ret:
        #print(i.group("name"),
        #i.group("year").strip(),
        #i.group("score").strip(),
        #i.group("comments").strip())#.strip()用来消除空白
        dic = i.groupdict()
        dic["year"] = dic["year"].strip()
        csvwriter.writerow(dic.values())
file.close()
print("over!")