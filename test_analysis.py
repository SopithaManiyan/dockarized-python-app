# test_analysis.py
import pytest
from analysis import get_revenue_by_month, get_revenue_by_product, get_revenue_by_customer, get_top_customers
from data_processing import calculate_revenue, convert_order_dates
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'order_date': ['2023-07-01', '2023-07-15', '2023-08-01', '2023-08-10'],
        'product_price': [10, 20, 15, 25],
        'quantity': [1, 2, 3, 4]
    }
    return pd.DataFrame(data)

def test_get_revenue_by_month(sample_data):
    df = convert_order_dates(sample_data)
    df = calculate_revenue(df)
    revenue_by_month = get_revenue_by_month(df)
    assert revenue_by_month.iloc[0] == 50, "Revenue by month calculation is incorrect"

# Add more tests for the other functions...
