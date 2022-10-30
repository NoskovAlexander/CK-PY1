def get_count_char(str_):
    for letter in str_.lower():
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict


def get_letter_frequency(dict_):
    str_length = sum(dict_.values())
    for letter in dict_:
        dict_[letter] /= str_length
    return dict_


letter_dict = {}
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_letter_frequency(get_count_char(main_str)))
