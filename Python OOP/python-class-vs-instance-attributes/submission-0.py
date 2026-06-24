class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
# TODO: Print the information using the mentioned format
alice_acc = BankAccount("Alice", 1000)
bob_acc  = BankAccount("Bob", 2000)

print(f"Alice's balance: ${str(alice_acc.balance)}")
print(f"Bob's balance: ${str(bob_acc.balance)}")
print(f"Total Accounts: {str(BankAccount.total_accounts)}")
print(f"Total Balance: ${str(BankAccount.total_balance)}")