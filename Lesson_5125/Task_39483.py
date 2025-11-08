num = int(input())
if num == 0:
    print(50)
elif num <= 30:
    print(int(num + num / 2))
elif num <= 70:
    print(int(num + num * 0.1))
else:
    print(num)