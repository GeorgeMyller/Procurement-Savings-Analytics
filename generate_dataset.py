import csv
import random
from datetime import datetime, timedelta
import os

# Set seed for reproducibility
random.seed(42)

# Configurations for dataset
num_records = 1500
regions = ['EMENA', 'Americas', 'Asia']
categories = ['IT Hardware', 'Software Licenses', 'Professional Services', 'Logistics', 'Raw Materials', 'Marketing', 'Office Supplies']
status_options = ['Completed', 'Pending', 'In Progress']

# Generate data
data = []
start_date = datetime(2025, 1, 1)

for i in range(1, num_records + 1):
    invoice_id = f"INV-{10000 + i}"
    region = random.choice(regions)
    category = random.choice(categories)
    
    # Baseline spend based on category
    base_amounts = {
        'IT Hardware': (5000, 50000),
        'Software Licenses': (1000, 20000),
        'Professional Services': (10000, 100000),
        'Logistics': (2000, 40000),
        'Raw Materials': (50000, 500000),
        'Marketing': (5000, 80000),
        'Office Supplies': (500, 5000)
    }
    
    min_spend, max_spend = base_amounts[category]
    spend_baseline = round(random.uniform(min_spend, max_spend), 2)
    
    # Savings percentage generally between 2% and 15%
    savings_pct = random.uniform(0.02, 0.15)
    
    # Add some randomness - maybe negative savings (overspend) occasionally
    if random.random() < 0.05:
        savings_pct = random.uniform(-0.05, 0)
        
    savings_achieved = round(spend_baseline * savings_pct, 2)
    actual_spend = round(spend_baseline - savings_achieved, 2)
    
    # Generate random date
    days_offset = random.randint(0, 450)
    invoice_date = start_date + timedelta(days=days_offset)
    
    data.append({
        'Invoice_ID': invoice_id,
        'Date': invoice_date.strftime('%Y-%m-%d'),
        'Region': region,
        'Category': category,
        'Spend_Baseline_USD': spend_baseline,
        'Actual_Spend_USD': actual_spend,
        'Savings_Achieved_USD': savings_achieved,
        'Savings_Percentage': round((savings_achieved / spend_baseline) * 100, 2),
        'Status': random.choices(status_options, weights=[0.8, 0.1, 0.1])[0]
    })

# Sort by Date
data.sort(key=lambda x: x['Date'])

os.makedirs('data', exist_ok=True)
with open('data/procurement_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Invoice_ID', 'Date', 'Region', 'Category', 'Spend_Baseline_USD', 'Actual_Spend_USD', 'Savings_Achieved_USD', 'Savings_Percentage', 'Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("Successfully generated data/procurement_data.csv with 1500 records.")
