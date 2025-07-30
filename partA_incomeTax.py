# Get user input for name and salary
name = input("Enter your name: ")
salary = float(input("Enter your salary: "))

#Check if salary is a valid positive number
while salary <= 0:
    print("Salary must be a positive number.")
    salary = float(input("Please enter a valid salary: "))


def calculateIncomeTax(salary):
    #Initialize tax variable
    tax = 0
    # First bracket
    if salary <= 55867:
        tax = salary * 0.15
    # Second bracket
    elif salary <= 111733:
        tax = 55867 * 0.15 + (salary - 55867) * 0.205
    # Third bracket
    elif salary <= 173205:
        tax = 55867 * 0.15 + (111733 - 55867) * 0.205 + (salary - 111733) * 0.26
    # Fourth bracket
    elif salary <= 246752:
        tax = (55867 * 0.15 +
               (111733 - 55867) * 0.205 +
               (173205 - 111733) * 0.26 +
               (salary - 173205) * 0.29)
    # Above fourth bracket
    else:
        tax = (55867 * 0.15 +
               (111733 - 55867) * 0.205 +
               (173205 - 111733) * 0.26 +
               (246752 - 173205) * 0.29 +
               (salary - 246752) * 0.33)
    #Round the tax to two decimal places    
    return round(tax, 2)

# Calculate income tax based on the salary
incomeTax = calculateIncomeTax(salary)

# Print the result
print(f"Hello {name}, your income tax is: {incomeTax}")