import requests

url = "https://fanyi.baidu.com/sug"

s = input("请输入您想要翻译的单词")

dat = {
    "kw":s
}

resp = requests.post(url,data = dat)
print(resp.json())