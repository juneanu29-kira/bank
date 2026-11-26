from bank import bank_operation

def test_successful_withdrawal():
    assert bank_operation(10000, 3000) == 7000

def test_insufficient_balance():
    assert bank_operation(10000, 12000) == "Insufficient Balance"

def test_negative_withdrawal():
    assert bank_operation(10000, -200) == "Invalid Withdrawal Amount"
