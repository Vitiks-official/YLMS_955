n, m = int(input()), int(input())
x = 0
step = int(input())
while step != 0:
    if step == 1:
        x += n
    else:
        x -= m
    step = int(input())
print(x)