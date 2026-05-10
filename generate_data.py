import csv
import random
from datetime import datetime, timedelta

def generate_data(num_transactions=10000, fraud_percentage=0.01):
    """
    Generates a CSV file with simulated financial transaction data.
    """
    fieldnames = ['transaction_id', 'user_id', 'amount', 'timestamp', 'is_fraud']
    with open('transactions.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        start_time = datetime(2023, 1, 1)
        for i in range(num_transactions):
            user_id = random.randint(1, 100)
            amount = round(random.uniform(1, 1000), 2)
            timestamp = start_time + timedelta(minutes=i)
            is_fraud = False

            # Introduce some fraud patterns
            # Pattern 1: Multiple small transactions in a short period of time
            if i > 10 and i % 100 < 5:
                is_fraud = True
                amount = round(random.uniform(1, 10), 2)
            # Pattern 2: Unusually large transaction
            elif i % 500 == 0:
                is_fraud = True
                amount = round(random.uniform(5000, 10000), 2)
            # Pattern 3: Transactions from a compromised user
            elif user_id == 42:
                if random.random() < 0.5:
                    is_fraud = True


            writer.writerow({
                'transaction_id': i,
                'user_id': user_id,
                'amount': amount,
                'timestamp': timestamp.isoformat(),
                'is_fraud': is_fraud
            })

if __name__ == '__main__':
    generate_data()
