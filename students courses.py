python = {"Emma", "Sarah", "steve", "Alex"}
datascience = {"Anna", "Sarah", "Emily", "john"}

python.add("Sam")
print(python)

datascience.remove("Anna")
print(datascience)

print(python & datascience)
print(python - datascience)
print(python ^ datascience)

course = {
    "python" : 5,
    "datascience" : 3
}

for x,y in course.items():
    print("course:", x,",", "students:", y)

course_new = {x:y*2 for x,y in course.items()}
print(course_new)