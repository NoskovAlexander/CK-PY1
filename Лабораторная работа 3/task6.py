list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

pos = 0

for i, val in enumerate(list_numbers):
    if list_numbers[pos] < val:
        pos = i

list_numbers[pos], list_numbers[-1] = list_numbers[-1], list_numbers[pos]

print(list_numbers)
