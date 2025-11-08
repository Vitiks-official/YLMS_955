num = input()
num = " " + num + " "
if num in ' 5 6 7 8 9 10 ':
    print("Утро")
elif num in " 11 12 13 14 15 16 17 ":
    print("День")
elif num in " 18 19 20 21 22 ":
    print("Вечер")
elif num in " 23 0 1 2 3 4 ":
    print("Ночь")
else:
    print("Ошибка")