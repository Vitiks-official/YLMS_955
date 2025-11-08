line = input()
ll = 0
while "Бэггинс" not in line:
    if "добр" in line and (ll == 0 or len(line) < ll):
        ll = len(line)
    line = input()
print(ll)