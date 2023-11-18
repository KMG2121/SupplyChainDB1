import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(0)

# Define time period for the data
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
date_range = pd.date_range(start_date, end_date)

# Generate synthetic data
data = {
    'Date': np.random.choice(date_range, 1000),
    'Inventory_Level': np.random.randint(100, 1000, 1000),
    'Supplier': np.random.choice(['Supplier A', 'Supplier B', 'Supplier C'], 1000),
    'Delivery_Time_Days': np.random.normal(10, 2, 1000),
    'Order_Fulfillment_Cycle_Time': np.random.normal(5, 1.5, 1000),
    'Shipment_Volume': np.random.randint(10, 200, 1000),
    'Region': np.random.choice(['North America', 'Europe', 'Asia', 'South America', 'Africa'], 1000),
    'Actual_Demand': np.random.randint(500, 1500, 1000),
    'Forecasted_Demand': np.random.randint(500, 1500, 1000),
    'On_time_Delivery': np.random.choice([True, False], 1000)
}

df = pd.DataFrame(data)

# Adjust date format and sort by date
df['Date'] = pd.to_datetime(df['Date']).dt.date
df.sort_values(by='Date', inplace=True)

# Save to CSV
df.to_csv('supply_chain_data.csv', index=False)

print("Dataset created successfully!")
