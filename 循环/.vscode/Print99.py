#打印九九乘法表
'''
1.打印一个乘法表达式
2.一行打印多个表达式，个数与行号相等
3.打印多行表达式    循环一行表达式
'''

j = 1
while j < 10:
    i = 1
    while i <= j:
        print(f"{i}*{j}={i*j}",end = '\t')
        i += 1
        #一行的表达式结束
    print()
    j += 1