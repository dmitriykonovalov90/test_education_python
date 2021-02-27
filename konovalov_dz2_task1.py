result1 = 15 * 3
result2 = 15 / 3
result3 = 15 // 2
result4 = 15 ** 2
list_results = [result1, result2, result3, result4]

for key, type_values in enumerate(list_results, 1):
    print("Тип", key, "результата выражения: ", type(type_values))
