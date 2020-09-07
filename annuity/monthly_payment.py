# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'

# write your code here
import math

credit_principal = int(input("Enter the credit principal: "))
print("What do you want to calculate?")
print('type "m" - for count of months')
print('type "p" - for monthly payment')
type = input()
if type == 'm':
    print("Enter monthly payment:")
    payment = int(input())
    months = round(credit_principal / payment)
    if months == 1:
        print(f"It takes {months} month to repay the credit")
    else:
        print(f"It takes {months} months to repay the credit")
elif type == 'p':
    print("Enter count of months:")
    months = int(input())
    payment = math.ceil(credit_principal / months)
    last_payment = credit_principal - ((months - 1) * payment)
    if payment == last_payment:
        print(f"Your monthly payment = {payment}")
    else:
        print(f"Your monthly payment = {payment} with last month payment = {last_payment}")
else:
    print("Wrong Option")