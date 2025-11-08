old_n = int(input())
n = int(input())
k = 1
bigger = n > old_n
while True:
    if n < 0:
        print(k)
        break
    if n < 35 or old_n < 35:
        print("ALARM")
        break
    if old_n == n:
        k -= 1
    elif (old_n < n) != bigger:
        print(k)
        k = 1
        bigger = not bigger
    k += 1
    old_n = n
    n = int(input())
