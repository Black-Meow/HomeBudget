import csv

class CSVExporter:
    def export_to_csv(self, transactions, filepath: str):
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Amount', 'Category', 'Date'])
            for t in transactions:
                writer.writerow([str(t.amount), t.category, t.date.isoformat()])
