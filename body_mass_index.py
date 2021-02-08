'''
Developer: Ömer ULUTÜRK
Date: 01.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes the name, surname,
weight and height. And it gives Body Mass Index and Classify of BMI.
'''
print("Welcome to Body Mass Index Calculation Program")

weight = int(input("Please insert your weight (kg):\n"))
height = int(input("Please insert your height (cm):\n"))
BMI=weight/(height*height*0.0001)

print("Your Body Mass Index (BMI) is ",BMI)

if(BMI<25):
    print("\nYour weight is 'NORMAL'\n")
elif(BMI<30):
    print("\nYour weight is 'OVERWEIGHT'\n")
elif(BMI<40):
    print("\nYour weight is 'OBESITY'\n")
else:
    print("\nYour weight is 'SUPER OBESITY'\n")
    


