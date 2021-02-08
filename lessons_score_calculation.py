'''
Developer: Ömer ULUTÜRK
Date: 01.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes the student name and surname,
 names of lesson, midterm scores and final scores.
And it gives average score and result that specify as "pass" or "failed".
'''

print("Welcome to The Lesson Point Calculation Program")
student=input("Please enter your name and surname:").upper()
student_number=input("Please enter your student number:")
lessons=[]
lesson1_midterm_note=[]
lesson1_final_note=[]
average_note=[]
for i in range (0,4):
    lesson_name=input(f"Please enter your {i+1}. lesson:")
    lessons.append(lesson_name)
    midterm=int(input(f"Please enter midterm note for {lessons[i]} lesson:"))
    lesson1_midterm_note.append(midterm)
    final=int(input(f"Please enter final note for {lessons[i]} lesson:"))
    lesson1_final_note.append(final)
    average=(lesson1_midterm_note[i]*0.4)+(lesson1_final_note[i]*0.6)
    average_note.append(average)
print("Name:",student, "        Number:",student_number)
for i in range (0,4):
    if average_note[i] > 50:
        print(f"{lessons[i]}: PASSED  ({average_note[i]})")
    else:
        print(f"{lessons[i]}: FAILED  ({average_note[i]})")

