from urllib.request import urlopen

#准备一个网址
url = "http://www.baidu.com"
#读取数据
resp = urlopen(url)

with open("mybaidu.html",mode = "w") as f:
    f.write(resp.read().decode("utf-8"))
print("over")