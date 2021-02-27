import random

price_list = []

for key in range(1, 21):
    price_list.append(random.uniform(10, 100))

print("\n*** Задание А ***\n")
for key in price_list:
    print(f"{int(key // 1)} руб. {int(100 * (key % 1) // 1):02} коп.")

print("\n\n*** Задание В ***\n")
price_list.sort()
for key in price_list:
    print(f"{int(key // 1)} руб. {int(100 * (key % 1) // 1):02} коп.")

print("\n\n*** Задание С ***\n")
price_list.sort(reverse=True)
for key in price_list:
    print(f"{int(key // 1)} руб. {int(100 * (key % 1) // 1):02} коп.")




