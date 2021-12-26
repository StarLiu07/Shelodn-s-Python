#计算1-100的累加和

#准备数据
i = 1

#结果变量
result = 0

#开始循环
while i < 101:
    #加法运算 前两个数的结果 + 第二个数 没计算一次假发更新一次result变量值
    result += i
    i += 1
#打印最终结果
print(result)