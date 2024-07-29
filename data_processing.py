# data_processing.py
'''This module contains functions for data processing, 
like converting dates and calculating revenue.'''

import pandas as pd

def convert_order_dates(df):
    # Converts 'order_date' to datetime, raising an error if it fails
    if 'order_date' not in df.columns:
        raise ValueError("Missing required column: 'order_date'")
    
    try:
        # Specify the expected date format to avoid parsing inconsistencies
        df['order_date'] = pd.to_datetime(df['order_date'], errors='raise', format='%Y-%m-%d')
    except Exception as e:
        raise ValueError(f"Invalid date format in 'order_date': {e}")

    # Check for dates outside of a sensible range
    min_date = pd.Timestamp('1900-01-01')
    max_date = pd.Timestamp('2100-01-01')
    if (df['order_date'] < min_date).any() or (df['order_date'] > max_date).any():
        raise ValueError("Date out of valid range (1900-2100) in 'order_date'")
    
    return df
def calculate_revenue(df):
    # Ensures necessary columns are there before calculating revenue
    required_columns = ['product_price', 'quantity']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    df['revenue'] = df['product_price'] * df['quantity']
    return df

