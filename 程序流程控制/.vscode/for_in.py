#python的for循环可以简单地遍历一个可迭代数组

print("---字符串-----")
for item in 'Hello':
    print(item) #遍历了Hello

numbers = [43,32,55,74]#创建了一个数组
print("-----整数列表-----")
for item in numbers:
    print(item)#遍历了numbers数组

for item in range(10): #range(10)函数返回整数序列，它的取值大于等于0且小于10，总共有10个整数
    print(item)
else:
    print("For Over!") #for循环没有中断，执行else语句