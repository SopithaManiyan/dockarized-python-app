import pandas as pd
import random
from datetime import datetime, timedelta

# Generate sample data
num_samples = 50
order_ids = list(range(1, num_samples + 1))
customer_ids = [random.randint(100, 110) for _ in range(num_samples)]
start_date = datetime(2023, 1, 1)
order_dates = [start_date + timedelta(days=random.randint(0, 180)) for _ in range(num_samples)]
product_ids = [random.randint(1000, 1005) for _ in range(num_samples)]
product_names = ['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget E', 'Widget F']
product_prices = [20.00, 15.00, 40.00, 25.00, 50.00, 35.00]
quantities = [random.randint(1, 5) for _ in range(num_samples)]

# Map product IDs to names and prices
product_mapping = {
    1000: ('Widget A', 20.00),
    1001: ('Widget B', 15.00),
    1002: ('Widget C', 40.00),
    1003: ('Widget D', 25.00),
    1004: ('Widget E', 50.00),
    1005: ('Widget F', 35.00)
}

data = {
    'order_id': order_ids,
    'customer_id': customer_ids,
    'order_date': order_dates,
    'product_id': [random.choice(list(product_mapping.keys())) for _ in range(num_samples)],
    'product_name': [],
    'product_price': [],
    'quantity': quantities
}

# Assign product names and prices based on product IDs
for product_id in data['product_id']:
    product_name, product_price = product_mapping[product_id]
    data['product_name'].append(product_name)
    data['product_price'].append(product_price)

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('orders.csv', index=False)

print("Sample 'orders.csv' file with 50 entries created.")
