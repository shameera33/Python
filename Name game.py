import random
import math

names = input("Enter the names of guest:")

names_list = names.split(",")

new_list = list(set(names_list))

random_name = random.choice(new_list)

reverse_name = random_name[::-1]

total_names = len(new_list)

sqrt = round(math.sqrt(total_names))

print("Names:", new_list)
print("selected name:", random_name)
print("reversed:", reverse_name)
print("count of names:", total_names)
print("square root:", sqrt)
