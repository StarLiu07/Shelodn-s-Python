import re

#第一部分放正则表达式，第二部分放要匹配的字符串
#返回一个列表
#finall：匹配字符串中所有符合正则的内容
print("————————————findall————————————————")
list = re.findall(r"\d+","我的电话号是:10086,张三的电话是:10010")
print(list)

#finditer:匹配字符串中所有内容，返回迭代器,从迭代器中拿到内容要.group()方法
print("——————————finditer————————————————")
it = re.finditer(r"\d+","我的电话号是:10086,张三的电话是:10010")
#print(it)
#遍历
for i in it:
    print(i.group())

#search
#search返回的是match对象，用group()提取数据
#找到一个结果就返回，所以无法返回10010
print("——————————search————————————")
s = re.search(r"\d+","我的电话号是:10086,张三的电话是:10010")
print(s.group())

#match
#match从头开始匹配
print("——————————match————————————")
s = re.match(r"\d+","10086,张三的电话是:10010")
print(s.group())

#预加载正则表达式
print("——————————预加载正则表达式————————")
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号是:10086,张三的电话是:10010")
for i in ret:
    print(i.group())
#obj可以反复使用
ret = obj.findall("我是数字:12345")
print(ret)

print("————————————进阶————————————————")
s = """
<div class = 'jay'><span id = '1'>郭麒麟</span></div>
<div class = 'ji'><span id = '2'>宋轶</span></div>
<div class = 'sylar'><span id = '3'>大聪明</span></div>
<div class = 'jack'><span id = '4'>范思哲</span></div>
<div class = 'sheldon'><span id = '5'>胡说八道</span></div>
"""
#re.S：让.*?能匹配换行符
#(?P<放一个名字>)这个语法可以单独提取处这个数据
obj = re.compile(r"<div class = '.*?'><span id = '(?P<id>\d+)'>(?P<name>.*?)</span></div>",re.S)
result = obj.finditer(s)
#print(result)
for a in result:
    print(a.group("name"))
    print(a.group("id"))