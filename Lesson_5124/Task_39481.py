num = int(input())
num1 = int(input())
cnt = 0
while num > num1:
    num //= 2
    cnt += 1
if num == num1:
    print(cnt)
else:
    print("IMPOSSIBLE")