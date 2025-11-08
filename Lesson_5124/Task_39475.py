num1 = int(input())
num2 = num1
cnt = 0
num3 = num1
while num1 != -1:
    if num2 > num1 and num2 > num3:
        cnt += 1
    num3 = num2
    num2 = num1
    num1 = int(input())
print(cnt)
