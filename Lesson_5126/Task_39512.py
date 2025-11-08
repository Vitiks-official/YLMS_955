flag = True
cnt = 0
for i in input():
    if i == " ":
        flag = True
    elif i in "аяоёэеуюыи" and flag:
        flag = False
    elif i in "аяоёэеуюыи" and not flag:
        cnt += 1
print(cnt)