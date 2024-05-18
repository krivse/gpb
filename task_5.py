# Задача 5


def generate_words(input_word):
    """Generate words from the list of words."""
    matched_words = []
    words_txt = open("words.txt", "r")
    for word in words_txt:
        if input_word not in word:
            for i in range(len(input_word) - 1):
                if all([input_word[i::] in word, input_word[i - 1:] not in word]):
                    match = input_word[:i] + word
                    matched_words.append(match)
    else:
        print("Word not found in the list of words")
    return matched_words


input_user = input("Enter a word: ").lower()
print("\n".join(generate_words(input_user)))
