a = input()
b = input()
c = input()
text = input()
answer = "В букете есть "
some = 0
if a in text or b in text or c in text:
	if a in text:
		answer = answer + a
		some = 1
	if b in text and some != 1:
		answer = answer + b
		some = 1
	elif b in text and some == 1:
		answer = answer + ", " + b
	if c in text and some != 1:
		answer = answer + c
		some = 1
	elif c in text and some == 1:
		answer = answer + ", " + c
	answer += "."
	print(answer)
else:
	print("Таких цветов в букете нет.")