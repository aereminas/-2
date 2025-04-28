def analyze_text(user_string):
    normalized_words = user_string.lower().split()
    word_frequency = {}

    for single_word in normalized_words:
        if single_word in word_frequency:
            word_frequency[single_word] += 1
        else:
            word_frequency[single_word] = 1

    for word, frequency in word_frequency.items():
        print(f"'{word}': {frequency}")


string_input = input("Пожалуйста, введите текст: ")
analyze_text(string_input)

