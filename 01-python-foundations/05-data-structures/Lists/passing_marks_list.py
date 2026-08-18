marks=[55, 70, 83, 42, 91]
passing_marks=[]
failed_marks=[]
for mark in marks:
    if mark>=70:
        passing_marks.append(mark)
    else:
        failed_marks.append(mark)
print("Passing marks: ", passing_marks)        
print("Failed marks: ", failed_marks)
