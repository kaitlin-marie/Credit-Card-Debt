print("\033c")

print('ab')
#credit card looserman

#p1
B = float(input('enter outstanding balance:'))
P = float(input('Enter monthly payment as decimal:'))
I = float(input('enter yearly interest as decimal:'))
Balance = B

x = 0
TotalPaid = 0

while x < 12:
    Payment = round(Balance*P, 2)
    Interest = round(Balance*(I/12), 2)
    Balance = round(Balance - Payment + Interest, 2)
    print('Month:' + str(x+1))
    print('Remaining Balance: ' + str(Balance))
    print('Paid this month:' + str(Payment))

    TotalPaid = Payment + TotalPaid
    x += 1

print('Total Amount Paid:' + str(TotalPaid))
print('End of Year Balance:' + str(Balance))


#p2 via exhaustive

B = float(input('enter outstanding balance:'))
I = float(input('enter yearly interest as decimal:'))

Bal2 = B
FP = 0
TI = 0
y = 1

while Bal2 > 0:
    FP += 10
    Bal2 = B
    y = 1
#^^ resets the balance & months to intial amount for next loop
    while y < 12:
        IN = (I/12)*Bal2
        Bal2 = Bal2 - FP + IN
        y += 1
    RB = Bal2
    round(RB)
print('Minimum monthy payment is ', str(FP))
print('Number months required ', y)
print('Remaining Balance ', str(RB))



#p2 via bisection

B = float(input('enter outstanding balance:'))
I = float(input('enter yearly interest as decimal:'))

low = B/12
high = B/12 + (B*I)/12
FixPay = (low + high)/2
Bal3 = B
m = 0

while True:
    Bal3 = B
    m = 0
    for m in range(1,13):
        Int3 = (I/12)*Bal3
        Bal3 = Bal3 - FixPay + Int3
        if Bal3 <= 0:
            break   
    if (high - low) < .005:
        break
    if 0 >= Bal3 >= -50:
        print('Minimum monthy payment is ', str(FixPay))
        print('Number months required ', m)
        print('Remaining Balance ', str(Bal3))
        break
    if Bal3 > 0:
        low = FixPay
    if Bal3 < -50:
        high = FixPay
    FixPay = round((low + high)/2, 2)




