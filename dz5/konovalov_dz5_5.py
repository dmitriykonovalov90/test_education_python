def unique_list():
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [y for y in src for x in src if y > x]
    print(result)
# задачу не доделал(((((
unique_list()