money = int(input())
perc = float(input()) / 100
years = float(input())
i = 0
while i < int(years):
    money += money * perc
    i += 1
if years != int(years):
    money += money * 0.01 * (years - int(years))
print(money)
