header = """
BOOKSTORE RECEIPT"""

book_1 = "Python Basics"
book_1_price = 450

book_2 = "Data Science Intro"
book_2_price = 600

book1 = "\nBook Title:{}\tPrice:{}".format(book_1, book_1_price)
book2 = "\nBook Title:{}\tPrice:{}".format(book_2, book_2_price)

total_price = book_1_price + book_2_price

total = "\nTotal price:{}\t".format(total_price)

thank_you = "\nThank you for shopping"

receipt = header + book1 + book2 + total + thank_you
print(receipt.upper())