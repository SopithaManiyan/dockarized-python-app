# test_main.py
import pytest
import pandas as pd
from mainfile import convert_order_dates, calculate_revenue

@pytest.fixture
def sample_data():
    # Provides sample data for testing purposes
    data = {
        'order_date': ['2023-07-01', '2023-07-15', '2023-08-01', '2023-08-10'],
        'customer_id': [1, 2, 1, 3],
        'product_price': [10, 20, 15, 25],
        'quantity': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    return df

def test_convert_order_dates(sample_data):
    # Tests if 'order_date' is correctly converted to datetime
    df = convert_order_dates(sample_data)
    assert pd.api.types.is_datetime64_any_dtype(df['order_date']), "order_date should be datetime type"

def test_convert_order_dates_missing_column():
    # Ensures an error is raised when 'order_date' column is missing
    data = {
        'product_price': [10, 20, 15, 25],
        'quantity': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Missing required column: 'order_date'"):
        convert_order_dates(df)

def test_convert_order_dates_invalid_format():
    # Tests handling of invalid date formats in 'order_date'
    data = {
        'order_date': ['invalid-date', '2023-07-15', '2023-08-01', '2023-08-10'],
        'product_price': [10, 20, 15, 25],
        'quantity': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Invalid date format in 'order_date'"):
        convert_order_dates(df)

def test_calculate_revenue(sample_data):
    # Checks if the revenue is calculated correctly
    df = calculate_revenue(sample_data)
    expected_revenue = [10, 40, 45, 100]
    assert df['revenue'].tolist() == expected_revenue, "Revenue calculation is incorrect"

def test_calculate_revenue_missing_columns():
    # Ensures an error is raised when 'quantity' column is missing
    data = {
        'order_date': ['2023-07-01', '2023-07-15', '2023-08-01', '2023-08-10'],
        'product_price': [10, 20, 15, 25]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Missing required columns: quantity"):
        calculate_revenue(df)
