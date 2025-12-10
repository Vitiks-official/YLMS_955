stack = []
flag = True
line = input()
for i in line:
    if i in "{([<":
        stack.append(i)
    elif i == "}":
        if len(stack) and stack[-1] == "{":
            stack.pop()
        else:
            flag = False
            break
    elif i == ")":
        if len(stack) and stack[-1] == "(":
            stack.pop()
        else:
            flag = False
            break
    elif i == "]":
        if len(stack) and stack[-1] == "[":
            stack.pop()
        else:
            flag = False
            break
    elif i == ">":
        if len(stack) and stack[-1] == "<":
            stack.pop()
        else:
            flag = False
            break
if flag and not len(stack):
    print("YES")
else:
    print("NO")