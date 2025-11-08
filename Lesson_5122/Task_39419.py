first = int(input())
second = int(input())
if second != 0:
    print("Каждому по " + str(first // second))
    print("Осталось " + str(first % second))
else:
    print("Не делится!")