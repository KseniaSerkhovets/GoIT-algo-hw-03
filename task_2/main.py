import random

def get_numbers_ticket(min, max, quantity):
    numbers_list = []

    if min < 1 or min > 999:
        print("Min is invalid")
    elif max <= min or max > 1000:
        print("Max is invalid")
    elif quantity > max - min:
        print("Quantity is invalid")
    else:
        min_max = list(range(min, max))
        numbers_list = random.sample(min_max, quantity)
        numbers_list.sort()
    
    return numbers_list


min = int(input("Enter min: "))
max = int(input("Enter max: "))
quantity = int(input("Enter quantity: "))

lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)
