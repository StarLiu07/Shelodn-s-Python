import requests

url = "https://movie.douban.com/j/new_search_subjects"

#重新封装参数
dic = {
    "sort": "U",
    "range": "0,10",
    "tags": "",
    "start": 0,
    "genres": "喜剧"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
}

resp = requests.get(url = url,params = dic,headers = headers)

#print(resp.request.url)
print(resp.json())