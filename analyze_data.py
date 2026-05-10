import csv
from collections import defaultdict
from datetime import datetime
import math

def analyze_data(transactions_file='transactions.csv'):
    """
    Analyzes the characteristics of fraudulent and non-fraudulent transactions.
    """
    fraudulent_transactions = []
    non_fraudulent_transactions = []

    with open(transactions_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                row['amount'] = float(row['amount'])
                row['timestamp'] = datetime.fromisoformat(row['timestamp'])
                if row['is_fraud'] == 'True':
                    fraudulent_transactions.append(row)
                else:
                    non_fraudulent_transactions.append(row)
            except (ValueError, TypeError, KeyError):
                continue

    print("Analysis of fraudulent transactions:")
    if fraudulent_transactions:
        print(f"Number of fraudulent transactions: {len(fraudulent_transactions)}")
        amounts = [t['amount'] for t in fraudulent_transactions]
        print(f"  Amount stats: Avg: {sum(amounts) / len(amounts):.2f}, Min: {min(amounts)}, Max: {max(amounts)}")
        hours = [t['timestamp'].hour for t in fraudulent_transactions]
        hour_counts = defaultdict(int)
        for hour in hours:
            hour_counts[hour] += 1
        print(f"  Transaction distribution by hour: {sorted(hour_counts.items())}")
    else:
        print("No fraudulent transactions found.")

    print("\nAnalysis of non-fraudulent transactions:")
    if non_fraudulent_transactions:
        print(f"Number of non-fraudulent transactions: {len(non_fraudulent_transactions)}")
        amounts = [t['amount'] for t in non_fraudulent_transactions]
        print(f"  Amount stats: Avg: {sum(amounts) / len(non_fraudulent_transactions):.2f}, Min: {min(amounts)}, Max: {max(amounts)}")
        hours = [t['timestamp'].hour for t in non_fraudulent_transactions]
        hour_counts = defaultdict(int)
        for hour in hours:
            hour_counts[hour] += 1
        print(f"  Transaction distribution by hour: {sorted(hour_counts.items())}")
    else:
        print("No non-fraudulent transactions found.")

if __name__ == '__main__':
    analyze_data()
