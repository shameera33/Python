rice_price_kg = 45
sugar_price_kg = 40
oil_price_kg = 130

rice_quantity = 3
sugar_quantity = 2.5
oil_quantity = 1.8

rice_total = rice_price_kg * rice_quantity
sugar_total = sugar_price_kg * sugar_quantity
oil_total = oil_price_kg * oil_quantity

print("Rice= " , rice_total)
print("Sugar= " , sugar_total)
print("Oil= " , oil_total)

total = rice_total +sugar_total + oil_total

print("total= " , total)
print("total int= " , int(total))
print("total str= " , total)

import random
delivery_charge = random.randrange(5,11)
final_bill_amount = total + delivery_charge
print("Final bill amount= " , final_bill_amount)