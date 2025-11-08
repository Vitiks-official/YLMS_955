h, m = int(input()), int(input())
n = int(input())
m += h * 60
m = 60 * 12 - m
if m < n:
    print("Не останавливаемся!")
else:
    print(f"{m // n} минут")