# analysis.py
'''This module contains functions for performing specific analyses, 
such as calculating revenue by month or identifying top customers.'''

def get_revenue_by_month(df):
    df['month'] = df['order_date'].dt.to_period('M')
    return df.groupby('month')['revenue'].sum()


def get_revenue_by_product(df):
    return df.groupby('product_id').apply(lambda x: (x['revenue']).sum())

def get_revenue_by_customer(df):
    return df.groupby('customer_id').apply(lambda x: (x['revenue']).sum())

def get_top_customers(df, top_n=10):
    revenue_by_customer = get_revenue_by_customer(df)
    return revenue_by_customer.sort_values(ascending=False).head(top_n)
