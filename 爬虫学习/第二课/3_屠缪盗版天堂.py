#1.定位到2022必看影片
#2.从中提取到子页面的链接
#3.请求子页面地址，拿到下载地址

import requests
import re

domain = "https://dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
}
resp = requests.get(domain,headers = headers,verify = False) #verify = False 去掉安全验证
resp.encoding = "gb2312"
#print(resp.text)
resp.close()

obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名　(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for i in result1:
    ul = i.group("ul")
    
    result2 = obj2.finditer(ul)
    for it in result2:
        #拼接子页面的url地址
        child_href = domain + it.group("href").strip("/")
        #把链接存到列表
        child_href_list.append(child_href)

#提取子页面链接
for href in child_href_list:
    child_resp = requests.get(href,verify = False)
    child_resp.encoding = "gb2312"
    result3 = obj3.finditer(child_resp.text)
    for i in result3:
        print(i.group("name"))
        print(i.group("download"))
        
