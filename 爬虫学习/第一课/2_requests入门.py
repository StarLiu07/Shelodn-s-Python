import requests

query = input("请输入一个你喜欢的明星")

url = f'https://www.sogou.com/web?query={query}'

dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
}

resp = requests.get(url,headers = dic)



print(resp)
print(resp.text)
resp.close()