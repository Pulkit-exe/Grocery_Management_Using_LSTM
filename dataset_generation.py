import numpy as np
import pandas as pd
from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

initial_inventory = 100
inventory_fluctuation = np.random.normal(0, 5, len(date_range))
inventory_levels = np.cumsum(inventory_fluctuation) + initial_inventory
day_of_week_factor = np.where(np.array([date.weekday() for date in date_range]) < 5, 1.0, 1.2)  # Increase sales on weekends
day_of_month_factor = np.where(np.array([date.day for date in date_range]) < 7, 1.2, 1.0)  # Increase sales at the beginning of the month
sales_noise = np.random.normal(0, 2, len(date_range))
sales = day_of_week_factor * day_of_month_factor + sales_noise
sales = np.maximum(0, sales)
synthetic_data = pd.DataFrame({
    'Date': date_range,
    'Inventory_Level': inventory_levels,
    'Sales': sales
})
synthetic_data.to_csv('grocery_inventory_data.csv', index=False)