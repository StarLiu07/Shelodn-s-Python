#break语句
print("----break语句-----")
for item in range(10): #去了大于等于0小于10的整数
    if item == 3:
        break #跳出循环
    print(item)

#continue语句
#continue语句用来结束本次循环，跳过循环体中尚未执行的语句，接着进行终止条件的判断以决定是否继续循环
print("----continue语句-----")
for item in range(10):
    if item == 3:
        continue
    print(item)