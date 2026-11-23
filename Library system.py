import re

try:
    title = input("Enter book title: ")
    year = input("Enter publication year: ")

    errors = ""

    if re.search("^[A-Za-z ]+$", title):
        print("Book title:", title)
    else:
        errors += "Invalid book title!\n"

    if re.search("^(19|20)[0-9]{2}$", year):
        print("Publication year:", year)
    else:
        errors += "Invalid publication year!\n"

    if errors:
        raise ValueError(errors)

except ValueError as error:
    print(error)

finally:
    print("Library system execution completed.")