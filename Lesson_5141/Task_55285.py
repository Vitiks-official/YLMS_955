num = int(input())
if (num // 100 + num // 10 % 10 + num % 10) % 8 == 0 and num % 10 != 1:
    print("Успеет")
else:
    print(num // 100 + num // 10 % 10 + num % 10, num % 10)