num = int(input())
for i in range(int(input()) - 1):
    nnum = ""

    while num != 0:
        nnum += str(num % 2)
        num //= 2

    count = nnum.count("1")
    ncount = ""

    while count != 0:
        ncount += str(count % 2)
        count //= 2

    ncount += nnum
    num = 0

    for j in range(len(ncount)):
        num += int(ncount[j]) * (2 ** j)

print(num)

