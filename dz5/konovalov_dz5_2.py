def nums_gen(end):
    my_generator = (num for num in range(1, end + 1, 2))
    print(*my_generator)


nums_gen(int(input("Enter to the end value: ")))