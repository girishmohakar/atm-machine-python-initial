
print('Welcome to world bank')
intialamount = 1000
x = input('\n enter password ')
if x == "1234" :
    print("welcome user")
    y = int(input('enter the amount you want to deposit'))

    if y <= intialamount :
        y = intialamount - y
        print('amount has been deposited available balance', y)
        print('thank you and have nice day')
    else : 
        print ('withdrawal exeed available balance ')
else :
    print('invalid password')    










