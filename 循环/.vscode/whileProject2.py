#计算1-100偶数累加和

#方法1
i = 1
result = 0
while i < 101:
    if i % 2 == 0:
        result += i
    i += 1

#输出结果
print(result)

#方法2
j = 2
result1 = 0
while j < 101:
    result1 += j
    j += 2

print(result1)