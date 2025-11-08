n = input()
print(", ".join([str(int("1" * i) ** 2) for i in range(1, len(n) + 1) if int("1" * i) <= int(n)]))