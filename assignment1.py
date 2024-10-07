"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
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
  t = input("please enter just a number for your investment time: ")
  try:
    t = float(t)
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
  typeTime = input("Type of investment time(years, months or days): ")
  while True:
    typeTime = input("Type of investment time (please type years, months or days): ")
    if typeTime == "mounts":
      break
    elif typeTime == "days":
      break
    elif typeTime == "years":
      break
  iTime = input(f"Your investment time in {typeTime}: ")
  try:
    iTime = float(iTime)
  except:
    iTime = investmentTime()
  if typeTime == "months":
    t = iTime / 12
  elif typeTime == "days":
    t = iTime / 365
  elif typeTime == "years":
    t = iTime
  I = iInvestment*aRate*t
  print(f"Your intrest earnd on your ${iInvestment} in {iTime} {typeTime} at {aRate*100}% is ${I}")

if __name__ == "__main__":
  main()