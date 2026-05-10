import csv

def detect_fraud(transactions_file='transactions.csv'):
    """
    A simple and inefficient fraud detection script.
    """
    fraudulent_transactions = []
    with open(transactions_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # A very simple and ineffective rule
            if float(row['amount']) > 9000:
                fraudulent_transactions.append(row['transaction_id'])

    return fraudulent_transactions

if __name__ == '__main__':
    fraudulent_transactions = detect_fraud()
    print(f"Found {len(fraudulent_transactions)} fraudulent transactions:")
    print(fraudulent_transactions)
