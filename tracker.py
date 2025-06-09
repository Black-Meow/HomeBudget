class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, t: Transaction):
        if not t.is_valid():
            raise ValueError("Invalid transaction")
        self.transactions.append(t)
