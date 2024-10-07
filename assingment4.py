"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

def initialDebt():
  i = input("please enter just a number for your debt: ")
  try:
    i = float(i)
  except:
    i = initialDebt()
  return i

def annualRate():
  r = input("please enter just a number for your anual rate: ")
  try:
    r = float(r)/100
  except:
    r = annualRate()
  return r

def mounthlyPayments():
  p = input("please enter just a number for your mounthly payments: ")
  try:
    p = float(p)
  except:
    p = mounthlyPayments()
  return p

def main():
    iDebt = input("Your initial investment: ")
    try:
        iDebt = float(iDebt)
    except:
        iDebt = initialDebt()
    debt = iDebt
    mPay = input("Your mounthly payments: ")
    try:
        mPay = float(mPay)
    except:
        mPay = mounthlyPayments()
    aRate = input("Your annual interest rate as a percentage: ")
    try:
        aRate = float(aRate)/100
    except:
        aRate = annualRate()
    mounths = 0
    inPayed = 0
    while debt > 0:
       inPayed = debt*aRate + inPayed
       debt = (debt*aRate + debt) - mPay
       mounths = mounths + 1
    print(f"You will pay off your ${iDebt} in {mounths} mounths and you will pay ${round(inPayed, 2)} in intrest")

if __name__ == "__main__":
  main()