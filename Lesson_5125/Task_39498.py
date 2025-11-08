num = int(input())
new_num = int(input())
if len(str(num)) == 4:
    if num // 1000 != 9 and num + 1000 == new_num:
        print("ДА 1")
    elif num // 1000 == 9 and num == new_num:
        print("ДА 1")
    elif num - 1 == new_num:
        print("ДА 2")
    elif num // 10 + num % 10 * 1000 == new_num:
        print("ДА 3")
    elif num % 1000 * 10 + num // 1000 == new_num:
        print("ДА 4")
    else:
        print("НЕТ")
else:
    if num // 10000 != 9 and num + 10000 == new_num:
        print("ДА 1")
    elif num // 10000 == 9 and num == new_num:
        print("ДА 1")
    elif num - 1 == new_num:
        print("ДА 2")
    elif num // 10 + num % 10 * 10000 == new_num:
        print("ДА 3")
    elif num % 10000 * 10 + num // 10000 == new_num:
        print("ДА 4")
    else:
        print("НЕТ")
