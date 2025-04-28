def get_common_numbers():
    try:
        first_sequence_text = input("Первая последовательность (числа через пробел): ")
        first_sequence = [int(num) for num in first_sequence_text.split()]

        second_sequence_text = input("Вторая последовательность (числа через пробел): ")
        second_sequence = [int(num) for num in second_sequence_text.split()]

        shared_numbers = set(first_sequence) & set(second_sequence)

        if shared_numbers:
            print("Совпадающие числа:", " ".join(map(str, sorted(list(shared_numbers)))))
        else:
            print("Совпадений не обнаружено.")

    except ValueError:
        print("Ошибка! Убедитесь, что введены числа, разделенные пробелами.")

get_common_numbers()
