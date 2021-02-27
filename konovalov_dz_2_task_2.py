origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
new_list = []

for key in origin_list:
    if key.replace("+", "").isdigit() or key.replace("-", "").isdigit():
        if key.isdigit():
            new_list.append(f"'{int(key):02}'")
        else:
            new_list.append(f"'{key[0]}{int(key[1:]):02}'")
    else:
        new_list.append(key)

print(" ".join(new_list))
