# Below is grading system showing  how the students scored
marks=int(input("Enter student marks:"))
#print("the entered marks is;",marks)
if marks >0 and marks <30:
    print("below Average")
elif marks>=30 and marks <40:
    print("Average")
elif marks>=40 and marks <70:
    print("Above Average")
elif marks>=70 and marks<=100:
    print("Excelent")
else:
    print("invalid input")
