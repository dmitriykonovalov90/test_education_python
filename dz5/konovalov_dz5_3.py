def gen_tuple():
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    # Не очень понятно было одинарно выводить имя или со всеми классами. Сделал и так и так.

    # Первое, не очень такое решение
   # my_generator = ('(' + tutors[i] + ', ' + klasses[i] + ')\n ' for i in range(0, len(tutors)))
    # Второе решение
    my_generator = ((x, y) for x in tutors for y in klasses)
    print(*my_generator, sep='\n')
    print(type(my_generator))
    print(next(my_generator))



gen_tuple()