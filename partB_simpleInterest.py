# Get user input
year = int(input("Enter the number of years: "))
months = int(input("Enter the number of months: "))
days = int(input("Enter the number of days: "))
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))

def getTime(year, months, days): 
    # Convert years, months, and days to total time in years
    totalYears = year + (int(months) / 12) + (int(days) / 365)
    print(f"    Total time in years is {totalYears:.2f} years")
    return totalYears



def simpleInterest():
    # Calculate simple interest
    interest = principal * (rate / 100) * getTime(year, months, days)
    # Round the interest to two decimal places
    interest = round(interest, 2)
    print(f"    Total interest earned is ${interest}")
    return interest

simpleInterest()


