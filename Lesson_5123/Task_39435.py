h = int(input())
m = int(input())
h = (h % 12) * 30 + 30 * (m / 60)
print(abs(h - m * 6))