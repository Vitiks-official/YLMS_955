first = input()
second = input()
if (first == "Быть" or first == "Не быть") and (second == "Быть" or second == "Не быть"):
    if first == second:
        print("Выбор сделан!")
    else:
        print("Вот в чём вопрос!")
else:
    print("Определитесь!")