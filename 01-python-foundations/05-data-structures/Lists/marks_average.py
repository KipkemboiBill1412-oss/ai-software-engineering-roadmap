marks=[55, 70, 83, 42, 91]
passing_marks=[]
for mark in marks:
    if mark>=70:
        passing_marks.append(mark)
average=sum(passing_marks)/len(passing_marks)        
print("Passing marks: ", passing_marks)
print(f"Average: {average:.2f}")
