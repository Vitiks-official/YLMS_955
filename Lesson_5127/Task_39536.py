while True:
    num = int(input())
    if num == 0:
        break
    if num % 3 == 0:
        if num % 7 == 0:
            print("Караул!")
            break
        else:
            print("несчастливое")
    elif num % 7 == 0:
        print("опасное")
    else:
        print(num)
