# mainfile.py
import pandas as pd
from data_processing import convert_order_dates, calculate_revenue
from analysis import get_revenue_by_month, get_revenue_by_product, get_revenue_by_customer, get_top_customers

def main():
    # Load the data from the CSV file
    df = pd.read_csv('orders.csv')
    
    # Process the data
    df = convert_order_dates(df)
    df = calculate_revenue(df)

    # Perform analysis
    revenue_by_month = get_revenue_by_month(df)
    revenue_by_product = get_revenue_by_product(df)
    revenue_by_customer = get_revenue_by_customer(df)
    top_customers = get_top_customers(df)

    # Print the results
    print("Revenue by Month:\n", revenue_by_month)
    print("\nRevenue by Product:\n", revenue_by_product)
    print("\nRevenue by Customer:\n", revenue_by_customer)
    print("\nTop 10 Customers:\n", top_customers)

if __name__ == "__main__":
    main()
