print("Назовите себя, пожалуйста!")
name = input()
print("Введите текст.")
text = input()
print("Повторите текст.")
text2 = input()
if text != text2:
	print(name + ", пока не получилось, попробуйте снова!")
else:
	print(name + ", введено верно!")