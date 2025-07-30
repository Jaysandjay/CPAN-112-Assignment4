
def getRate():
    #Create a menu for rate options
    print("Rate options")
    print("----------------------------")
    print("1. Annual interest rate")
    print("2. semi-annually rate")
    print("3. quarterly rate")
    print("4. Monthly interest rate")
    print("5. Weekly interest rate")
    print("6. Daily interest rate")

    # Get user input for rate choice
    choice = input("Enter the number corresponding to your choice: ")

    # Validate user input for choice
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter the number corresponding to your choice: ")
        print("")
    
    print("----------------------------")
    # Set rate and type based on user choice
    match choice:
        case "1":   
            rate = float(input("Enter the annual interest rate (in %): ")) / 100
            compoundingPeriod = "annually"
        case "2":
            rate = float(input("Enter the semi-annual interest rate (in %): ")) / 100 / 2   
            compoundingPeriod = "semi-annually"
        case "3":
            rate = float(input("Enter the quarterly interest rate (in %): ")) / 100 / 4
            compoundingPeriod = "quarterly"
        case "4":
            rate = float(input("Enter the monthly interest rate (in %): ")) / 100 / 12
            compoundingPeriod = "monthly"
        case "5":
            rate = float(input("Enter the weekly interest rate (in %): ")) / 100 / 52
            compoundingPeriod = "weekly"
        case "6":
            rate = float(input("Enter the daily interest rate (in %): ")) / 100 / 365
            compoundingPeriod = "daily"   
    print("")    
    return rate, compoundingPeriod
    
# Get user input for principal, rate, and time
principal = float(input("Enter the principal amount: "))
rate, compoundingPeriod = getRate()
year = int(input("Enter the number of years: "))
months = int(input("Enter the number of months: "))
days = int(input("Enter the number of days: "))

#Calculate total time in years
def getTime(year, months, days): 
    # Convert years, months, and days to total time in years
    totalYears = year + (int(months) / 12) + (int(days) / 365)
    print("")
    return totalYears

# Get total time in years in variable
time = getTime(year, months, days)

# Function to calculate compound interest
def compoundInterest(principal, rate, time):
    # Calculate compound interest
    amount = principal * (1 + rate) ** time
    interest = amount - principal
    # Round the interest to two decimal places
    interest = round(interest, 2)
    return interest

# Calculate compound interest in variable
cp = compoundInterest(principal, rate, time)

# Function to display the information
def displayInfo():
    print("----------------------------------------")
    print(f"Principal: ${principal:.2f}")
    print(f"Compounding period: {compoundingPeriod}")
    print(f"Rate: {rate * 100:.2f}%")
    print(f"Time: {time:.2f} years")
    print(f"Compound Interest Earned: ${cp:.2f}")
    print(f"Total Amount after interest: ${principal + cp:.2f}")
    print("----------------------------------------")

displayInfo()