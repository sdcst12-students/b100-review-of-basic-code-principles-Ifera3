"""
### Assignment 2
#### Calculation of an investment with a recurring deposit
The simple interest formula only works if the principal or initial investment is not touched.  If an amount is added to the principal every year, then the interest must be calculated and added along with the future deposit to determine the starting balance at the beginning of the next year.

For example, suppose you invest $100 every year, and earn 5% interest per year.
At the start of the first year, you will have your $100 that you invested.  At the start of the second year, you will have the initial $100, $5 interest as well as an additional $100 that is invested in the second year, for a total of $205 dollars.  Write a program that uses a for loop to determine the amount of money in an account after a certain number of years.

Criteria:
Your program should ask the user for
* the annual investment
* the annual interest rate (as a percentage)
* the number of years
* calculate the amount of money at the end of each year until the specified number of years has been reached.
* appropriate formatting and variable names will be important
* use a *for* loop to iterate through the years.

Sample data
annual investment: 100
rate: 5%
10 years
final balance: 1320.68

"""

def initialInvestment():
  i = input("please enter just a number for your initial investment: ")
  try:
    i = float(i)
  except:
    i = initialInvestment()
  return i

def annualRate():
  r = input("please enter just a number for your anual rate: ")
  try:
    r = float(r)/100
  except:
    r = annualRate()
  return r

def investmentTime():
  t = input("please enter just a intager for your investment time: ")
  try:
    t = int(t)
  except:
    t = annualRate()
  return t

def main():
    iInvestment = input("Your initial investment: ")
    try:
        iInvestment = float(iInvestment)
    except:
        iInvestment = initialInvestment()
    aRate = input("Your annual interest rate as a percentage: ")
    try:
        aRate = float(aRate)/100
    except:
        aRate = annualRate()
    iTime = input(f"Your investment time in years: ")
    try:
        iTime = int(iTime)
    except:
        iTime = investmentTime()
    erand = iInvestment*aRate + iInvestment
    for i in range(iTime - 1):
        erand = (erand + iInvestment)*aRate + erand + iInvestment
    print(f"Your intrest earnd on your ${iInvestment} in {iTime} years at {aRate*100}% compunded yearly is ${erand}")

if __name__ == "__main__":
  main()