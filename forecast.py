from datetime import date, timedelta
from decimal import Decimal

class ForecastEngine:
    def predict(self, transactions, months: int):
        """
        Zwraca prognozę salda na kolejne miesiące na podstawie średniego salda miesięcznego.
        """
        if not transactions:
            return {i: Decimal("0.00") for i in range(1, months + 1)}

        totals = {}
        for t in transactions:
            key = (t.date.year, t.date.month)
            totals[key] = totals.get(key, Decimal("0.00")) + t.amount

        avg = sum(totals.values()) / len(totals)
        forecast = {i: avg for i in range(1, months + 1)}
        return forecast
