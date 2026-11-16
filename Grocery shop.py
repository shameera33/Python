initial_items = ["milk", "bread", "eggs"]
print("Items:", initial_items)

def add_item(item):
   initial_items.append(item)
   print("Item added", initial_items)

def remove_last_item():
   initial_items.pop()
   print("Item removed:", initial_items)

add_item("butter")

remove_last_item()

show_items = lambda item: print("Item:" , item)
for item in initial_items:
      show_items(item)


def count_characters(items):
      if len(items) == 0:
          return 0
      remaining_items = items[1:]
      return len(items[0]) + count_characters(remaining_items)

print("Total characters:", count_characters(initial_items))