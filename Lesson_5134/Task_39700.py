st = " ".join([str(i) + "," if i % 4 != 0 else str(i) + "; АХ!" for i in range(1, int(input()) + 1)])
if st[-1] == ",":
    print(st[:-1])
else:
    print(st)