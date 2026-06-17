# 🔄 Customer Churn Analysis

End-to-end churn analysis on 49,950 customers using Python and Power BI.

## 📊 Key Metrics
- Churn Rate: 28.89%
- Total Users: 49,950
- Avg Customer Lifetime Value: 1,440.59
- Avg Purchase Amount: 13.00

## 💡 Key Insights
- Low-value customers churn most (36.97%)
- Medium-value customers are most retained (17.04%)
- High-value customers show unexpected churn (32.54%)
- Lower app usage and longer inactivity are strongest churn drivers
- Q1–Q2 signup cohorts show higher churn than Q3–Q4

## ⚙️ Data Cleaning Highlights
- Age filtered to valid range (18–75)
- Percentages converted to ratios (cart, discount, returns, email)
- Outlier soft cap on total_purchases (99th percentile)
- Recency nulls filled with max+1 (inactive user logic)

## 🛠 Tools
Python | Pandas | NumPy | Power BI | DAX

## 👤 Author
**Abhishek Kumar**
