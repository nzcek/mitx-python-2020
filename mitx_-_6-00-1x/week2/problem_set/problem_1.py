#Defined by grader
#balance
#annualInterestRate
#monthlyPaymentRate

monthlyintrate = annualInterestRate/12.0


def debtkiller9000(balance,monthlyPaymentRate):
x = 0
while x < 12:
monthlypay= monthlyPaymentRate * balance
print(round(monthlypay,2))
balance = balance - monthlypay
balance = (balance * monthlyintrate) + balance
print(round(balance,2))
x+=1
continue
print(round(balance,2))
