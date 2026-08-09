print("====================STUDENT GRADE CALCULATOR====================")

name = input("Enter your name: ")
print("Welcome,", name)

english = float(input("Enter English marks: "))
kiswahili = float(input("Enter Kiswahili marks: "))
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
physics = float(input("Enter Physics marks: "))


def calculate_total(english, kiswahili, maths, science, physics):
    return english + kiswahili + maths + science + physics


def calculate_average(total):
    return total / 5


def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"


total = calculate_total(english, kiswahili, maths, science, physics)
average = calculate_average(total)
grade = calculate_grade(average)


print("Total:", total)
print("Average:", average)
print("Grade:", grade)