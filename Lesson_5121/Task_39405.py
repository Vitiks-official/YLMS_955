text = input()
if ("Вор" in text or 'вор' in text) and 'ворон' not in text:
    print("Полиция!")
elif "ворон" in text:
    print("Кар!")