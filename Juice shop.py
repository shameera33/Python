apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25

total_volume = apple_juice + orange_juice + grape_juice
print(total_volume)

total_volume_int = int(total_volume)
print(total_volume_int)

total_vol_str = str(total_volume_int)
print("total volume is: " + total_vol_str)

import random
bonus = random.randrange(5, 10)
final_total = bonus + total_volume
print("final total volume is: " + str(final_total))