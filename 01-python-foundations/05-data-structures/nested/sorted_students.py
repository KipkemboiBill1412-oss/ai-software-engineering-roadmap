students=[
    {"name": "Bill", "age":23, "language": "Python"},
    {"name": "John", "age": 21, "language": "Java"},
    {"name": "Mark", "age": 24, "language": "C++"},
    {"name": "Ella", "age": 18, "language": "C#"}

]
students.sort(key=lambda student: student["age"])
print("Youngest to oldest: \n")
for student in students:
    print(student["name"], student["age"])
students.sort(key=lambda student: student["age"], reverse=True)
print("Oldest to youngest: \n")
for student in students:
    print(student["name"], student["age"])
students.sort(key=lambda student: student["name"])
print("Alphabetical: \n")
for student in students:
    print(student["name"])
