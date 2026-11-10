frontend = {"Emma", "Sarah", "steve", "Alex"}
backend = {"Anna", "Sarah", "Emily", "john"}

backend.add("Sam")
print(frontend)

frontend.remove("Alex")
print(frontend)

print(frontend & backend)
print(backend - frontend)

no_of_students = len(frontend | backend)
print(no_of_students)

fullstack = {
    "frontend" : 3,
    "backend" : 5
}

for x,y in fullstack.items():
    print("course:", x,",", "students:", y)

updated_courses = {
    course: count for course, count in fullstack.items()
}

updated_courses = {
    **updated_courses,
    "Fullstack": sum(fullstack.values())
}

print(updated_courses)