name = input("enter your name:")
age = int(input("enter your age: "))
height = float(input("enter you height in meters: "))
student = bool(input("are you a student? (True/False): "))  
print(name, age, height, student)

print("Name:",name, "Age:",age, "Height:",height, "student:",student)

months = age * 12
days = age * 365
remainder = age % 7
raised_age = age ** 2
print("Months:",months, "Days:",days, "Remainder:",remainder, "Raised_Age:",raised_age)