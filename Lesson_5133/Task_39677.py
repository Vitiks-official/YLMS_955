r = int(input())
f = int(input())
for i in range(int(input())):
    nr = int(input())
    f = f * r * r
    f = f / nr / nr
    r = nr
    print((f"№{i + 1}", f))
