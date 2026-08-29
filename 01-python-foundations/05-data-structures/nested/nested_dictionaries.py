student={
    "name": "Bill",
    "age": 23, 
    "details": {
        "language": "python",
        "level": "beginner"

    }
         }
print("Student's name: ", student["name"])
print("Language: ", student["details"]["language"])
student["details"]["level"]= "intermediate"
student["details"]["experience"]=1
print(student)