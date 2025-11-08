v1 = float(input())
v2 = float(input())
v3 = float(input())
food = int(input())
t = int(input())
answer = ""
if food / v1 <= t * 60:
    answer += "Самая длинная змея"
if food / v2 <= t * 60:
    if answer != "":
        answer += " "
    answer += "Самая толстая змея"
if food / v3 <= t * 60:
    if answer != "":
        answer += " "
    answer += "Питончик"
if answer != "":
    print(answer)
else:
    print("Не они")