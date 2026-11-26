import sys

total_balance = 10000
withdrawal_amount = 3000

def bank_operation(total_balance, withdrawal_amount):

    if withdrawal_amount <= 0:
        return "Invalid Withdrawal Amount"

    elif withdrawal_amount <= total_balance:
        available_balance = total_balance - withdrawal_amount

        return available_balance

    else:
        return "Insufficient withdrawl amount"


available_balance = bank_operation(
    total_balance, withdrawal_amount
)

print("Total Balance:", total_balance)
print("Withdrawal Amount:", withdrawal_amount)

if isinstance(available_balance, (int, float)):
    print("Available Balance:", available_balance)
else:
    print(available_balance)
