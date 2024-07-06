import random as ra


def get_numbers_ticket(min, max, quantity):
    if max - min < quantity or max - min < 0:
        raise ValueError("max minus min must be less than or equal to quantity")

    win_numbers_set = set()
    while len(win_numbers_set) < quantity:
        win_numbers_set.add(ra.randint(min, max))
    win_numbers_list = sorted(list(win_numbers_set))
    return win_numbers_list


result_list = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", result_list)
print(type(result_list))
