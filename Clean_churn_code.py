
import pandas as pd
import numpy as np

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("churn_dataset.csv")

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# ==============================
# AGE
# ==============================
df['age_missing'] = df['age'].isna().astype(int)
df['age'] = df['age'].fillna(df['age'].median())
df['age'] = df['age'].astype(int)

# Remove unrealistic ages (domain logic)
df = df[(df["age"] >= 18) & (df["age"] <= 75)]

# ==============================
# SESSION + BEHAVIOR METRICS
# ==============================

# Session duration
df['session_duration_avg'] = df['session_duration_avg'].fillna(
    df['session_duration_avg'].median()
)

# Pages per session
df['pages_per_session'] = df['pages_per_session'].fillna(
    df['pages_per_session'].median()
)

# ==============================
# CART & WISHLIST
# ==============================

# Cart abandonment (convert % → ratio)
df['cart_abandonment_rate'] = df['cart_abandonment_rate'] / 100
df['cart_abandonment_rate'] = df['cart_abandonment_rate'].clip(0, 1)

# Wishlist
df['wishlist_items'] = df['wishlist_items'].fillna(
    df['wishlist_items'].median()
)

# ==============================
# PURCHASE BEHAVIOR
# ==============================

# Total purchases
df.loc[df['total_purchases'] < 0, 'total_purchases'] = np.nan
df['total_purchases'] = df['total_purchases'].fillna(
    df['total_purchases'].median()
)
df['total_purchases'] = df['total_purchases'].round().astype(int)

# Soft cap 
upper_limit = df['total_purchases'].quantile(0.99)
df['total_purchases'] = df['total_purchases'].clip(upper=upper_limit)

# ------------------------------
# AOV
# ------------------------------
# cleaning invalid values

df['average_order_value'] = df['average_order_value'].replace(
    [np.inf, -np.inf], np.nan
)
df['average_order_value'] = df['average_order_value'].fillna(
    df['average_order_value'].median()
)

# ==============================
# RECENCY
# ==============================

# Days since last purchase
max_days = df['days_since_last_purchase'].max()
df['days_since_last_purchase'] = df['days_since_last_purchase'].fillna(max_days + 1)

# ==============================
# DISCOUNT & RETURNS
# ==============================

# Discount usage (percentage → ratio)
df['discount_usage_rate'] = df['discount_usage_rate'] / 100
df['discount_usage_rate'] = df['discount_usage_rate'].clip(0, 1)
df['discount_usage_rate'] = df['discount_usage_rate'].fillna(
    df['discount_usage_rate'].median()
)

# Returns rate (percentage → ratio)
df['returns_rate'] = df['returns_rate'] / 100
df['returns_rate'] = df['returns_rate'].clip(0, 1)

df['returns_rate'] = df['returns_rate'].fillna(
    df['returns_rate'].median()
)

# ==============================
# ENGAGEMENT
# ==============================

# Email open rate
df['email_open_rate'] = df['email_open_rate'] / 100
df['email_open_rate'] = df['email_open_rate'].clip(0, 1)
df['email_open_rate'] = df['email_open_rate'].fillna(
    df['email_open_rate'].median()
)

# Customer service calls
df['customer_service_calls'] = df['customer_service_calls'].fillna(
    df['customer_service_calls'].median()
)

# Product reviews
df['product_reviews_written'] = df['product_reviews_written'].fillna(
    df['product_reviews_written'].median()
)

# Social media engagement
# Assumption: missing = no engagement
df['social_media_engagement_score'] = df['social_media_engagement_score'].fillna(0)

# Mobile app usage
df['mobile_app_usage'] = df['mobile_app_usage'].fillna(
    df['mobile_app_usage'].median()
)

# ==============================
# PAYMENT BEHAVIOR
# ==============================

df['payment_method_diversity'] = df['payment_method_diversity'].fillna(
    df['payment_method_diversity'].median()
)

# ==============================
# FINANCIAL
# ==============================

# Credit balance 
df['credit_balance'] = df['credit_balance'].fillna(
    df['credit_balance'].median()
)

# ==============================
# TARGET VARIABLE
# ==============================

df['churned'] = df['churned'].astype(int)
df = df.drop_duplicates()

# ==============================
# FINAL CHECK
# ==============================

print("Final Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

df.to_csv("churn_dataset_cleaned.csv", index=False)