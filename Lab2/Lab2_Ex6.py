

init = float(raw_input("Please enter your initial investment: "))
int_rate = float(raw_input("Please enter annual interest rate (ex. 2.5): "))
payout = float(raw_input("Please enter the monthly annuity payout: "))

interest_rate = int_rate/(100*12)


if init <= payout :
    count = 0
    balance = init

else :
    count = 1
    balance = init + init*interest_rate - payout
    
    while balance >= payout - balance*interest_rate:
        balance -= payout - balance*interest_rate
        count += 1

print "After {} months, your balance is $ {:.2f}".format(count, balance)