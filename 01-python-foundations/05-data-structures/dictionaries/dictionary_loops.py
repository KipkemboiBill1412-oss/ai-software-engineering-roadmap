# SECTION ONE
# LOOPING THROUGH THE DICTIONARY
student={
    "name" : "Bill",
    "age": 17,
    "language" : "Python"


}
for key in student:
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key, "=" ,value)

# SECTION TWO
# MODIFYING VALUES
print("==================================SECTION 2===============================")
marks={
    "maths" : 73,
    "english" : 89,
    "python" : 87
}
for subject in marks:
    marks[subject] +=5
for subject,mark in marks.items():
    print(subject, "=" ,mark)