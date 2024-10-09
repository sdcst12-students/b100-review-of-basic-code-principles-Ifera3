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
def annualRate():
  r = input("please enter just a number for your anual rate: ")
  try:
    r = r.replace('%','')
    r = float(r)/100
  except:
    r = annualRate()
  return r  

def main():
  investRight = True
  while investRight:
    iInvestment = input("Your initial investment: ")
    try:
      iInvestment = iInvestment.replace('$','')
      iInvestment = float(iInvestment)
      investRight = False
    except:
      investRight = True
  aRate = input("Your annual interest rate as a percentage: ")
  try:
    aRate = aRate.replace('%','')
    aRate = float(aRate)/100
  except:
    aRate = annualRate()
  timeRight = True
  while timeRight:
    iTime = input("Enter your investment time(incloud if it's in years, months or days): ")
    try:
      if iTime.find('years') > -1 or iTime.find('Years') > -1:
        typeTime = "years"
        iTime = iTime.replace('years','')
        iTime = iTime.replace('Years','')
        t = float(iTime)
        timeRight = False
      elif iTime.find('months') > -1 or iTime.find('Months') > -1:
        typeTime = "months"
        iTime = iTime.replace('months','')
        iTime = iTime.replace('Months','')
        t = float(iTime)/12
        timeRight = False
      elif iTime.find('days') > -1 or iTime.find('Days') > -1:
        typeTime = "days"
        iTime = iTime.replace('days','')
        iTime = iTime.replace('Days','')
        t = float(iTime)/365
        timeRight = False
      else:
        typeTime = "years"
        t = float(iTime)
        timeRight = False
    except:
      timeRight = True
  I = iInvestment*aRate*t
  print(f"Your intrest earnd on your ${iInvestment} in {iTime} {typeTime} at {aRate*100}% is ${round(I, 2)}")

if __name__ == "__main__":
  main()