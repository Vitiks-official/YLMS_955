text = input()
if " " not in text and ("?" in text or "*" in text):
    print("Возможно маска")
else:
    print("Нет, это не маска!")