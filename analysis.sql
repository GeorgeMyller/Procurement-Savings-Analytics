/*
 * Global Procurement Analytics & Savings Dashboard
 * BigQuery SQL Scripts
 * 
 * Simulated queries designed for a Procurement Process Specialist / Data Analyst role portfolio.
 */

-- 1. TOTAL SAVINGS BY REGION (YTD & OVERALL)
SELECT 
    Region,
    COUNT(Invoice_ID) AS Total_Transactions,
    SUM(Spend_Baseline_USD) AS Total_Baseline_Spend,
    SUM(Actual_Spend_USD) AS Total_Actual_Spend,
    SUM(Savings_Achieved_USD) AS Total_Savings,
    ROUND((SUM(Savings_Achieved_USD) / SUM(Spend_Baseline_USD)) * 100, 2) AS Savings_Percentage
FROM 
    `your_project.procurement_dataset.procurement_data`
WHERE 
    Status = 'Completed'
GROUP BY 
    Region
ORDER BY 
    Total_Savings DESC;


-- 2. SAVINGS PERFORMANCE OVER TIME (MONTHLY TREND)
SELECT 
    FORMAT_DATE('%Y-%m', PARSE_DATE('%Y-%m-%d', Date)) AS Month,
    Region,
    SUM(Savings_Achieved_USD) AS Monthly_Savings,
    ROUND((SUM(Savings_Achieved_USD) / SUM(Spend_Baseline_USD)) * 100, 2) AS Monthly_Savings_Pct
FROM 
    `your_project.procurement_dataset.procurement_data`
WHERE 
    Status = 'Completed'
GROUP BY 
    Month, Region
ORDER BY 
    Month ASC, Region;


-- 3. CATEGORY SPEND AND SAVINGS ANALYSIS
SELECT 
    Category,
    SUM(Spend_Baseline_USD) AS Total_Baseline_Spend,
    SUM(Savings_Achieved_USD) AS Total_Savings,
    ROUND((SUM(Savings_Achieved_USD) / SUM(Spend_Baseline_USD)) * 100, 2) AS Avg_Savings_Percentage,
    MAX(Savings_Achieved_USD) AS Max_Single_Transaction_Saving
FROM 
    `your_project.procurement_dataset.procurement_data`
WHERE 
    Status = 'Completed'
GROUP BY 
    Category
ORDER BY 
    Avg_Savings_Percentage DESC;


-- 4. IDENTIFYING UNDERPERFORMING INITIATIVES (NEGATIVE SAVINGS / OVERSPEND)
SELECT 
    Invoice_ID,
    Date,
    Region,
    Category,
    Spend_Baseline_USD,
    Actual_Spend_USD,
    Savings_Achieved_USD
FROM 
    `your_project.procurement_dataset.procurement_data`
WHERE 
    Savings_Achieved_USD < 0
ORDER BY 
    Savings_Achieved_USD ASC
LIMIT 10;
