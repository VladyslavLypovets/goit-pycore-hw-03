import random

def get_numbers_ticket(min, max, quantity):
  list = range(min, max)
  result = random.sample(list, quantity)
  return sorted(result)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)