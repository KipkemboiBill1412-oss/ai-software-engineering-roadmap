student={
    "name": "Bill",
    "age": 23,
    "language": "Python"
}
student["age"]= 24
student["country"]= "Kenya"  
print("Name: ", student["name"])
print("Age: ", student["age"])
print("Language: ", student["language"])
print("Number of items: ", len(student))
if "language" in student:
    print("language is a key: True")
else:
    print("Language is a key: False")
if "Python" in student.values():
    print("Python is a value: True")   
else:
    print("Python is a value: False")
removed=student.pop("language")
print("Removed language: ", removed)
print("Final dictionary: ",student)



