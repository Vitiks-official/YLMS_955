for i in range(int(input()), int(input()) + 1):
    t = i // 1000
    s = i // 100 % 10
    d = i // 10 % 10
    e = i % 10
    if t != s and t != d and t != e and s != d and s != e and e != d:
        print(i)
