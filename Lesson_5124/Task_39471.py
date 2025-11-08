num = int(input())
cnt = 0
while num != 0:
    num1 = num
    num = int(input())
    if num > num1:
        cnt += 1
print(cnt)
