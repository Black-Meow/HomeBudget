from datetime import date, timedelta
from decimal import Decimal
from homebudget.models import Transaction

def test_valid_transaction():
    t = Transaction(Decimal('100.00'), "Salary", date.today())
    assert t.is_valid()

def test_zero_amount_invalid():
    t = Transaction(Decimal('0.00'), "Food", date.today())
    assert not t.is_valid()

def test_empty_category():
    t = Transaction(Decimal('10.00'), "", date.today())
    assert not t.is_valid()

def test_future_date():
    future = date.today() + timedelta(days=1)
    t = Transaction(Decimal('10.00'), "Other", future)
    assert not t.is_valid()
