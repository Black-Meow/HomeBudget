from datetime import date
from decimal import Decimal

class Transaction:
    def __init__(self, amount: Decimal, category: str, date_: date):
        self.amount = amount
        self.category = category
        self.date = date_

    def is_valid(self) -> bool:
        return (
            isinstance(self.amount, Decimal) and
            self.amount != Decimal('0') and
            self.category != "" and
            isinstance(self.date, date) and
            self.date <= date.today()
        )
