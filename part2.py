import math
import os

def filter_even(number_list):
    result_list = []
    for number in number_list:
        if number % 2 == 0:
            result_list.append(number) 
    
    return result_list

even_list = filter_even([1,2,3,4,5,6,7,8,9])
print(even_list)


#=========================================

def loan_emi(amount, duration, rate, down_pyment=0):
    
    """Calculates the equal monthly installment (EMI) for a loan.

    Arguments:
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """

    loan_amount = amount - down_pyment
    try:
        emi = loan_amount * rate * ((1 + rate) ** duration) / (((1 + rate) ** duration) - 1)
    except ZeroDivisionError:
       emi = loan_amount / duration
    emi = math.ceil(emi )
    return emi

emi1 = loan_emi(1260000, 8*12, 0.1/12, 3e5)
emi2 = loan_emi(1260000, 10*12, 0.08/12)
emi_with_interest = loan_emi(amount=100000, duration = 10*12,rate = 0.09/12 )
emi_without_interest = loan_emi(amount = 1000000, duration=10*12, rate=0)

print(emi1)
print(emi2)
print(emi_with_interest)
print(emi_without_interest)


#=====================================================
a = os.getcwd()
print(a)

 
