v = int(input())
d = int(input())
k = 0
flag = False
grad = False
while True:
    if d == 0:
        break
    if d > 20 and not flag:
        grad = True
    v -= d
    if not flag:
        k += 1
    if v <= 0 and not flag:
        flag = True
    d = int(input())
if v <= 0:
    print(f"Время заполнения {k} секунд.")
else:
    print("Ведро не полное.")
if grad:
    print("Град был!")
else:
    print("Града не было.")