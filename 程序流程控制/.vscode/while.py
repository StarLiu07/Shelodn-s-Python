i = 0

while i * i < 1000:
    i += 1

print("i = " + str(i))#这里因为i是int型，所以要把它强制转换成str型才能正常拼接
print("i * i = " + str(i * i))

i = 0

while i * i < 10:
    i += 1
    if i == 3:
        break
    print(str(i) + '=' + str(i) + '=',i * i)
else:
    print("Whiel Over!")