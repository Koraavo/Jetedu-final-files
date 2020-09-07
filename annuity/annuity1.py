# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'

# write your code here
import math
import sys
import argparse

args = sys.argv



print("What do you want to calculate?")
print('type "periods" - for count of months')
print('type "annuity" - for annuity monthly payment')
print('type "principal" - for credit principal')
print('type "diff" - for differentiated payments')
type = input()

if type == 'periods':
    principal = int(input("Enter credit principal: "))
    annuity = int(input("Enter monthly payment: "))
    interest = float(input("Enter credit interest: "))
    i = (interest / (12 * 100))
    num = i * principal
    n = math.ceil(math.log((annuity) / (annuity-num), 1 + i))
    print(n)
    years = n // 12
    months = n % 12
    if months == 0:
        print(f"You need {years} years to repay this credit")
    elif years == 0:
        print(f"You need {months} months to repay this credit")
    else:
        print(f'You need {years} years and {months} months to repay this credit')

elif type == 'annuity':
    principal = int(input("Enter credit principal: "))
    periods = int(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    i = (interest / (12 * 100))
    a = math.ceil(principal * ((i * pow(1 + i, periods)) / ((pow(1 + i, periods)) - 1)))
    print("Your annuity payment =", a)

elif type == 'principal':
    annuity = float(input("Enter monthly payment: "))
    periods = int(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    i = (interest / (12 * 100))
    p = math.ceil(annuity / ((i * pow(1 + i, periods)) / ((pow(1 + i, periods)) - 1)))
    print(f"Your credit principal = {p}")

elif type == 'diff':
    principal = int(input("Enter credit principal: "))
    periods = int(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))

    i = (interest / (12 * 100))
    current_period = 1
    differential_payments = []
    while current_period <= periods:
        d = math.ceil((principal / periods) + i * (principal - (principal * (current_period - 1)) / periods))
        differential_payments.append(d)
        current_period += 1
        print(d)
        overpayment = principal - sum(differential_payments)
        print(f"Overpayment is {abs(overpayment)}")

else:
    print("Invalid parameter")