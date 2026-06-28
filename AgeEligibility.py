age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")

if age >= 18 and citizen.lower() == "yes":
    print("Eligible")
else:
    print("Not Eligible")