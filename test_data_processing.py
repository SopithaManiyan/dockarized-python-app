# test_data_processing.py
import pytest
from data_processing import convert_order_dates, calculate_revenue
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'order_date': ['2023-07-01', '2023-07-15', '2023-08-01', '2023-08-10'],
        'product_price': [10, 20, 15, 25],
        'quantity': [1, 2, 3, 4]
    }
    return pd.DataFrame(data)

def test_convert_order_dates(sample_data):
    df = convert_order_dates(sample_data)
    assert pd.api.types.is_datetime64_any_dtype(df['order_date']), "order_date should be datetime type"

def test_calculate_revenue(sample_data):
    df = calculate_revenue(sample_data)
    expected_revenue = [10, 40, 45, 100]
    assert df['revenue'].tolist() == expected_revenue, "Revenue calculation is incorrect"
