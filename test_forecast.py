from datetime import date
from decimal import Decimal
from homebudget.forecast import ForecastEngine
from homebudget.models import Transaction

def test_forecast_with_no_data():
    engine = ForecastEngine()
    result = engine.predict([], 3)
    assert result == {1: Decimal("0.00"), 2: Decimal("0.00"), 3: Decimal("0.00")}

def test_forecast_with_monthly_data():
    engine = ForecastEngine()
    tx = [
        Transaction(Decimal("100"), "Job", date(2024, 1, 1)),
        Transaction(Decimal("200"), "Job", date(2024, 2, 1)),
        Transaction(Decimal("300"), "Job", date(2024, 3, 1)),
    ]
    result = engine.predict(tx, 2)
    assert result == {1: Decimal("200"), 2: Decimal("200")}

def test_forecast_rounding():
    engine = ForecastEngine()
    tx = [Transaction(Decimal("100.50"), "Test", date(2024, 1, 1))]
    result = engine.predict(tx, 1)
    assert result[1] == Decimal("100.50")

def test_forecast_handles_duplicates():
    engine = ForecastEngine()
    tx = [
        Transaction(Decimal("50"), "X", date(2024, 1, 1)),
        Transaction(Decimal("50"), "X", date(2024, 1, 15))
    ]
    result = engine.predict(tx, 1)
    assert result[1] == Decimal("100")
