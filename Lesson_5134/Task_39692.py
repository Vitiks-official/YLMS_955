n = int(input())
print(", ".join(["БОСИКОМ" if (i + 1) % n == 0 else str(i + 1) for i in range(int(input()))]))