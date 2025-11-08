n = int(input())
left = True
k = 0
for i in range(int(input())):
    line = input()
    if left:
        if len(" " * k + line) < n:
            print(" " * k + line)
            k += 1
        elif len(" " * k + line) == n:
            print(" " * k + line)
            left = False
            k = 1
        else:
            print(" " * (n - len(line)) + line)
            left = False
            k = 1
    else:
        if n - len(line) - k > 0:
            print((n - len(line) - k) * " " + line)
            k += 1
        elif n - len(line) - k <= 0:
            print(line)
            left = True
            k = 1
