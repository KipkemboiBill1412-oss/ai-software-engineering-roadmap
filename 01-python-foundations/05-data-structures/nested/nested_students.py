students=[
    {"name": "Bill", "age": 23, "language": "python"},
    {"name": "John", "age": 18, "language": "java"},
    {"name": "Mark", "age": 20, "language" : "sql"},
     {"name": "Daniel", "age": 48, "language": "C#"}
   
]
print("All students:")
for student in students:
    print(student["name"])

print("\nStudents 18 or older:")
for student in students:
    if student["age"] >= 18:
        print(student["name"])

print("\nPython students:")
for student in students:
    if student["language"] == "python":
        print(student["name"])
