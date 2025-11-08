a = input()
b = input()
c = input()
answer = ""
some = 0
if a > b:
	a, b = b, a
if b > c:
	b, c = c, b
if a > b:
	a, b = b, a
if " 0" in a:
	answer += a
	some = 1
if " 0" in b and some == 0:
	answer += b
	some = 1
elif " 0" in b and some == 1:
	answer = answer + ", " + b
if " 0" in c and some == 0:
	answer += c
elif " 0" in c and some == 1:
	answer = answer + ", " + c
print(answer)