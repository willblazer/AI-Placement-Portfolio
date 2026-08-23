# Student Performance Analysis
student_score=int(input("Enter the student's score (0-100): "))
if student_score >=70 and student_score <=100:
    print("Your Result is : Distinction.")
elif student_score >=60 and student_score <70:
    print("Your Result is : Merit.")
elif student_score >=50 and student_score <60:
    print("Your Result is : Pass.")
else:
    print("Your Result is : Fail.")

# moddified version of the student performance analysis program with more detailed grading criteria
students_score=int(input("Enter the student's score (0-100): "))
if students_score >=90 and students_score <=100:
    print("Your Result is : Outstanding.")
elif students_score >=70 and students_score <90:
    print("Your Result is : Distinction.")
elif students_score >=60 and students_score <70:
    print("Your Result is : Merit.")
elif students_score >=50 and students_score <60:
    print("Your Result is : Pass.")
elif students_score >=0 and students_score <50:
    print("Your Result is : Fail.")
else:
    print("Invalid score. Please enter a score between 0 and 100.")

# another version of writting the code having in mind pythons uses a compiler and executes the code line by line.
if students_score >= 90:
    print("Outstanding")
elif students_score >= 70:
    print("Distinction")
elif students_score >= 60:
    print("Merit")
elif students_score >= 50:
    print("Pass")
elif students_score >= 0:
    print("Fail")
else:
    print("Invalid score")