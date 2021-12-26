#条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
a = 1
b = 2

c = a if a > b else b
print(c)

#有两个变量，比较大小 如果变量1 大于 大于变量2 执行 变量1 - 变量2 否则 变量2 - 变量1
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print (cc)