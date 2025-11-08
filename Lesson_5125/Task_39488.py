num = int(input())
sn = 1
while sn <= num:
    sn *= 2
sn -= 1
if num == 0:
    print(1)
else:
    print(sn - num)