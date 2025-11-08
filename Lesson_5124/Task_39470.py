num = int(input())
max1 = -1000
max2 = -1000
while abs(num) < 1000:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
    num = int(input())
print(max2)
