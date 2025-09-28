word1 = input("Введите первое слово: ").lower()
word2 = input("Введите второе слово: ").lower()


if len(word1) != len(word2):
    print(False)
else:

    temp_word2 = list(word2)
    is_anagram = True

    for char in word1:
        found = False

        for i in range(len(temp_word2)):
            if temp_word2[i] == char:

                temp_word2[i] = None
                found = True
                break

        if not found:
            is_anagram = False
            break

    print(is_anagram)