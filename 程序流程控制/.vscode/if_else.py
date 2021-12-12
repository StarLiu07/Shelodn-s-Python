score = int(input("请输入一个0-100的整数：\t"))

if score >= 60:
    if score >= 85:
        print("您真优秀")
    else:
        print("您仍需继续努力")
else:
    print("您需要加倍努力")