V = int(input())
v = int(input())
c = int(input())
for i in range(1, c + 1):
    if V >= v:
        V -= v
        print(f"Чашечка {i} полная. В чайнике осталось {V}.")
    elif V <= 0:
        print(f"Чашечка {i} пустая. В чайнике осталось {V}.")
    else:
        V = 0
        print(f"Чашечка {i} неполная. В чайнике осталось {V}.")