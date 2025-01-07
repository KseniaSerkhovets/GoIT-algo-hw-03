import random

def get_numbers_ticket(min, max, quantity):
    min_max = []

    for i in range(min, max):
        min_max.append(i)

    numbers_list = random.sample(min_max, quantity)
    numbers_list.sort()
    
    return numbers_list


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
