origin_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names_list = []

for key in origin_list:
    names_list.append((key.split()[-1]).capitalize())

for key in names_list:
    print(f"'Привет, {key}!'")
