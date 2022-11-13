from random import randint


def get_unique_list_numbers(length=15) -> list[int]:
    list_ = []
    for _ in range(length):
        while True:
            number = randint(-10, 10)
            if number not in list_:
                break
        list_.append(number)

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
