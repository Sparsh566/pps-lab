#display grade
marks=[]
for i in range(1,6):
    marks.append(float(input(f"subject {i}: ")))

avg_marks = sum(marks)/5

if 90<=avg_marks<=100:
    grade = "A"
elif 80 <=avg_marks<=90:
    grade = "B"
elif 70 <=avg_marks<=80:
    grade = "C"
elif 60 <=avg_marks<=70:
    grade = "D"
else:
    grade = "F"

print(f"Average Marks: {avg_marks:.2f}")
print(f"Grade: {grade}")
