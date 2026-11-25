import random
import math

names = input("Enter names of customers:")

name_list = names.split(",")

final_list = list(set(name_list))

winners = random.choices(final_list,k=2)

print("winners:", winners)

for winner in winners:
    print("reversed name:", winner[::-1])

count = len(final_list)

sqrt = round(math.sqrt(count))

print("Total participants:", count)
print("square root:", sqrt)