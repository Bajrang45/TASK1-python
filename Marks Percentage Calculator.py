# Marks Percentage Calculator

m1 = float(input("Enter Marks of Subject 1: "))
m2 = float(input("Enter Marks of Subject 2: "))
m3 = float(input("Enter Marks of Subject 3: "))
m4 = float(input("Enter Marks of Subject 4: "))
m5 = float(input("Enter Marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 35:
    print("Grade: C")
else:
    print("Grade: Fail")