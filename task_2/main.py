import random

def get_numbers_ticket(min, max, quantity):
    min_max = []

    for i in range(min, max):
        min_max.append(i)

    numbers_list = random.sample(min_max, quantity)
    numbers_list.sort()
    
    return numbers_list

def check_input(min, max, quantity):
    if min < 1 or min > 999:
        print("Min is invalid")
        return False
    elif max <= min or max > 1000:
        print("Max is invalid")
        return False
    elif quantity > max - min:
        print("Quantity is invalid")
        return False
    return True

min = int(input("Enter min: "))
max = int(input("Enter max: "))
quantity = int(input("Enter quantity: "))


if check_input(min, max, quantity):
    lottery_numbers = get_numbers_ticket(min, max, quantity)
    print("Ваші лотерейні числа:", lottery_numbers)
