#水仙花数
#水仙花数是一个三位数，三位数各位的的立方之和等于三位数本身
#利用while循环计算出100-1000的水仙花数

number = 100#定义初始值，即从100开始寻找
'''
三位数的三个位数求法(三位数用x代替)
个位：x - x / 100 * 100
十位：(x - x / 100 * 100) / 10
百位：x / 100
'''



while number < 1001:
    #百位
    ohBit = int(number / 100)

    #三位数中的后两位 比如 123 中的 23
    temp = number - int(number / 100) * 100

    #十位
    ten = int(temp / 10)

    #个位
    bit = temp - ten * 10
    if bit**3 + ten**3 + ohBit**3 == number:
        print(number)
    number += 1