#Variable to keep track
amount_due = 50
#loop until the amount due is greater than 0

while amount_due > 0:
    #print the Amount Due
    print("Amount Due:", amount_due)
    #Ask the user to insert coin
    insert_coin = int(input("Insert Coin: "))
    #Check if coin is 25, 10 or 5 cents using 'in'
    if insert_coin in [25, 10, 5]:
        #subtract value from amount due
        amount_due -= insert_coin

#calculate change_owed
change_owed = abs(amount_due)
#print the resuslt
print("Change Owed:", change_owed)

