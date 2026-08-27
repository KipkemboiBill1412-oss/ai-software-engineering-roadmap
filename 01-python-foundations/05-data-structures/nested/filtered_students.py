students=[
  {  "name" : "Bill", "language": "Python", "age": 23},
   { "name": "Mark", "language": "C#", "age": 24},
    {"name": "Frank", "language": "Java","age": 19},
   { "name": "John", "language": "CSS", "age": 17}
]
adult_students=[]
for student in students:
    if student["age"]>=20:
        adult_students.append(student)
print("Adult students\n")
for student in adult_students:
     print(student["name"])
         

print(f"Number of adult students: {len(adult_students)}")
python_students=[]
for student in students:
    if student["language"]== "Python":
        python_students.append(student)
print("Python students: ")
for student in python_students:
    print(student["name"])
print("Number of Python students: ", len(python_students))


