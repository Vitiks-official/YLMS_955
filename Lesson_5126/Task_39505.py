letter = input()
maxp = 0
some = 0
for i in range(int(input())):
    if input() == letter:
        some += 1
    else:
        some = 0
    if some > maxp:
        maxp = some
print(maxp)