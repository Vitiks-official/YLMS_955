n = float(input())
if abs(n) < 10 ** -9:
    print("INFINITELY LARGE")
elif abs(n) > 10 ** 9:
    print("INFINITELY SMALL")
else:
    print(1 / n)