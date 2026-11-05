python = """
     Python is a popular, high-level programming language. It is easy to learn and understand.
Python is used in web development, data science, artificial intelligence, and automation.
It is known for its simple syntax and readability
"""

print("Length:",len(python))
print("First character:",python.strip()[0])
print("Last character:",python.strip()[-1])

print("preview:",python[:50])
new_python = python.replace("Python","PYTHON")
print(new_python)

to_lower = python.lower()
print(to_lower)

whitespace = python.strip()
print(whitespace)

to_words = whitespace.split()
print(to_words)

if "course" in python:
    print("The word 'course' is found")

print("The course description is {} characters long and has {} words.".format(len(whitespace), len(to_words)))