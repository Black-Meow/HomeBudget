import os
from decimal import Decimal
from datetime import date
from homebudget.export import CSVExporter
from homebudget.models import Transaction

def test_export_creates_file(tmp_path):
    tx = [Transaction(Decimal("50.00"), "Test", date(2024, 1, 1))]
    path = tmp_path / "output.csv"
    exporter = CSVExporter()
    exporter.export_to_csv(tx, str(path))
    assert path.exists()

def test_export_has_correct_header(tmp_path):
    tx = [Transaction(Decimal("50.00"), "Test", date(2024, 1, 1))]
    path = tmp_path / "header.csv"
    CSVExporter().export_to_csv(tx, str(path))
    with open(path, "r") as f:
        header = f.readline().strip()
    assert header == "Amount,Category,Date"

def test_export_contains_data(tmp_path):
    tx = [Transaction(Decimal("123.45"), "Groceries", date(2024, 1, 1))]
    path = tmp_path / "data.csv"
    CSVExporter().export_to_csv(tx, str(path))
    with open(path) as f:
        lines = f.readlines()
    assert "123.45,Groceries,2024-01-01" in lines[1]

def test_export_multiple_rows(tmp_path):
    tx = [
        Transaction(Decimal("10"), "A", date(2024, 1, 1)),
        Transaction(Decimal("20"), "B", date(2024, 2, 1))
    ]
    path = tmp_path / "multi.csv"
    CSVExporter().export_to_csv(tx, str(path))
    with open(path) as f:
        lines = f.readlines()
    assert len(lines) == 3  # header + 2 transactions
