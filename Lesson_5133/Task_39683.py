alpe = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alpr = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for i in set(input()):
    if i in alpe:
        print((i, alpe.index(i) + 1))
    elif i in alpr:
        print((i, alpr.index(i) + 1))