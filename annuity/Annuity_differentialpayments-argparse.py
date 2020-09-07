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


def periods(principal, payment, interest):
    i = (interest / (12 * 100))
    num = i * principal
    period = math.ceil(math.log((payment) / (payment - num), 1 + i))
    return period


def annuity(principal, periods, interest):
    i = (interest / (12 * 100))
    annuity = math.ceil(principal * ((i * pow(1 + i, periods)) / ((pow(1 + i, periods)) - 1)))
    return annuity


def principal(payment, periods, interest):
    i = (interest / (12 * 100))
    principal = math.floor(payment / ((i * pow(1 + i, periods)) / ((pow(1 + i, periods)) - 1)))
    return principal


def diff(principal, periods, interest):
    i = (interest / (12 * 100))
    current_period = 1
    differential_payments = []
    while current_period <= periods:
        d = math.ceil((principal / periods) + i * (principal - (principal * (current_period - 1)) / periods))
        differential_payments.append(d)
        current_period += 1
    return differential_payments


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Calculate annuity or differential_payments')
    parser.add_argument('--type', type=str, metavar='', required=False, help='Choose type',
                        choices=['annuity', 'diff'])
    parser.add_argument('--principal', type=int, metavar='', required=False, help='principal')
    parser.add_argument('--payment', type=int, metavar='', required=False, help='monthly payments')
    parser.add_argument('--interest', type=float, metavar='', required=False, help='interest')
    parser.add_argument('--periods', type=int, metavar='', required=False, help='periods in months')
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
    # group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
    args = parser.parse_args()
    if args.type == 'annuity':
        if args.principal and args.payment and args.interest:
            time = periods(args.principal, args.payment, args.interest)
            years = time // 12
            months = time % 12
            overpayment = (args.payment * time) - args.principal
            if months == 0:
                print(f"You need {years} years to repay this credit!")
            elif years == 0:
                print(f"You need {months} months to repay this credit!")
            else:
                print(f"You need {years} years and {months} months to repay this credit!")
            print(f"Overpayment = {overpayment}")


        elif args.principal and args.periods and args.interest:
            payment = annuity(args.principal, args.periods, args.interest)
            print(f"Your annuity payment = {payment}!")
            overpayment = (payment * args.periods) - args.principal
            print(f"Overpayment = {overpayment}")

        elif args.payment and args.periods and args.interest:
            prin = principal(args.payment, args.periods, args.interest)
            overpayment = (args.payment * args.periods) - prin
            print(f"Your credit principal is {prin}")
            print(f"Overpayment = {overpayment}")
        else:
            print("Incorrect parameters")

    elif args.type == 'diff':
        if args.principal and args.periods and args.interest:
            differ = diff(args.principal, args.periods, args.interest)
            month = 1
            while month <= args.periods:
                for d in differ:
                    print(f"Month {month}: paid out {d}")
                    month += 1
            overpayment = sum(differ) - args.principal
            print()
            print(f"Overpayment = {abs(overpayment)}")
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
