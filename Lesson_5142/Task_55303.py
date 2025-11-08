line = input()
n = int(input())
k = 0
for i in range(n):
    line2 = input()
    if line in line2 or "туннел" in line2:
        k += 1
if k >= 3:
    print("МЫСЛЬ ЕСТЬ!")
else:
    print("ПОСИДИМ ЕЩЕ")
print((1 - k / n) * 100)