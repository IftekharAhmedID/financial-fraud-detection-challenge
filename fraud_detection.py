import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score

def detect_fraud(transactions_file='transactions.csv'):
    """
    An improved fraud detection script using a Random Forest classifier.
    """
    # Load the dataset
    df = pd.read_csv(transactions_file)

    # Feature engineering
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour_of_day'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek

    # Prepare the data for training
    features = ['amount', 'hour_of_day', 'day_of_week']
    target = 'is_fraud'

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"F1 Score: {f1}")

    # Return the fraudulent transactions
    fraudulent_transactions = df.loc[model.predict(X) == True, 'transaction_id'].tolist()
    return fraudulent_transactions

if __name__ == '__main__':
    fraudulent_transactions = detect_fraud()
    print(f"Found {len(fraudulent_transactions)} fraudulent transactions:")
    print(fraudulent_transactions)
