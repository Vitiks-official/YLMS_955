n = int(input())
k = 0
while True:
    line = input()
    if line == "КОНЕЦ":
        break
    if k == n:
        continue
    if "доска" in line or "дощечка" in line:
        k += 1
        print(f"Прибили {k} дощечку.")
        if k == n:
            print("ГОТОВО")
if k != n:
    print("МАЛОВАТО")
