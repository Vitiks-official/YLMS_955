num = int(input())
s = 0
answer = ""
for i in range(num):
    if answer != "":
        answer += "_"
    answer += input()
print(answer, end="")