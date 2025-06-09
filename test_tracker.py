import pytest
from decimal import Decimal
from datetime import date
from homebudget.models import Transaction
from homebudget.tracker import BudgetTracker

def valid_t():
    return Transaction(Decimal("50.00"), "Groceries", date.today())

def test_add_valid_transaction():
    bt = BudgetTracker()
    bt.add_transaction(valid_t())
    assert len(bt.transactions) == 1

def test_add_invalid_transaction_raises():
    bt = BudgetTracker()
    with pytest.raises(ValueError):
        bt.add_transaction(Transaction(Decimal("
