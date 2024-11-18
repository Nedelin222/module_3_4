def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))

print('--------------')
print('Для проверки')
root_word = input("Введите искомый корень: ")
other_words = input('Введите строку с остальными словами: ').split()
print(single_root_words(root_word,*other_words )) # Так на всякий случай :)
