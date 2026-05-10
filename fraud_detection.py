import csv

def detect_fraud(transactions_file='transactions.csv'):
    """
    Detects fraudulent transactions based on a simple amount threshold.
    """
    fraudulent_transactions = []
    with open(transactions_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                amount = float(row['amount'])
                if amount > 1000:
                    fraudulent_transactions.append(row['transaction_id'])
            except (ValueError, TypeError, KeyError):
                continue

    return fraudulent_transactions

if __name__ == '__main__':
    fraudulent_transactions = detect_fraud()
    print(f"Found {len(fraudulent_transactions)} fraudulent transactions:")
    print(fraudulent_transactions)
