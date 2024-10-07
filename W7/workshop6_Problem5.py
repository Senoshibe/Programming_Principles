opening_balance = int(input("Opening balance of account: "))
deposits = 0 
withdrawals = 0

for x in range(5):
    deposit_withdraw = int(input("Amount deposited or withdrew (negative value): "))
    if deposit_withdraw < 0:
        deposits += abs(deposit_withdraw)
    
    else: 
        withdrawals += deposit_withdraw

closing_balance = opening_balance - deposits + withdrawals

print("Opening balance: ", opening_balance)
print("Deposits: ", deposits)
print("Withdrawals: ", withdrawals)
print("Closing balance: ", closing_balance)