def power_operation():
    try:
        input_data = input("Введите элементы (числа или текст) через пробел: ")
        elements = input_data.split()

        exponent = int(input("Укажите степень: "))

        result_list = []
        for item in elements:
            try:
                number = int(item)
                result_list.append(number ** exponent)
            except ValueError:
                result_list.append(item * exponent)

        print("Результат:", " ".join(map(str, result_list)))

    except ValueError:
        print("Ошибка! Степень должна быть целочисленной.")

power_operation()
