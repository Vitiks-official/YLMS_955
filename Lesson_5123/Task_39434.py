b = int(input())
c = int(input())
d = int(input())
print(d * 10 ** len(str(c)) + c)
if b * c + d < d * 10 ** len(str(c)) + c:
    print("ДА")
else:
    print("НЕТ")