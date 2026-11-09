fruits = ["apple", "mango", "watermelon", "grapes"]
vegetables = ["tomato", "carrot", "brinjal", "cucumber"]
beverages = ["mirinda", "mountaindew", "7up", "pepsi"]

fruits.append("orange")
vegetables.insert(2, "potato")
beverages.pop()

print(fruits)
print(vegetables)
print(beverages)

inventory = fruits + vegetables + beverages
print(inventory)

print(fruits[0:2])
print("last vegetable:", vegetables[-1])

fruits_length = [len(x) for x in fruits]
print("length of each fruit:",fruits_length)

print("water present in beverage:", "water" in beverages)

items1 = (fruits[0], vegetables[0], beverages[0])
print("first items:",items1)