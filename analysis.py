# ============================================================
# Superstore Sales Analysis
# End-to-End Data Analyst Portfolio Project
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── 0. SETUP ────────────────────────────────────────────────
sns.set_theme(style="whitegrid")
os.makedirs("outputs", exist_ok=True)   # all charts + clean CSV go here

# ── 1. LOAD DATA ────────────────────────────────────────────
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin-1")

print("=== RAW DATA SNAPSHOT ===")
print(df.shape)           # rows × columns
print(df.dtypes)          # data types
print(df.isnull().sum())  # null counts
print(df.duplicated().sum())  # duplicate rows

# ── 2. CLEAN DATA ───────────────────────────────────────────

# Fix date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"]  = pd.to_datetime(df["Ship Date"])

# Drop duplicates
df.drop_duplicates(inplace=True)

# Strip whitespace from string columns
str_cols = df.select_dtypes(include="object").columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# ── 3. FEATURE ENGINEERING ──────────────────────────────────

df["Profit Margin (%)"] = (df["Profit"] / df["Sales"] * 100).round(2)
df["Order Year"]        = df["Order Date"].dt.year
df["Order Month"]       = df["Order Date"].dt.to_period("M").astype(str)
df["Days to Ship"]      = (df["Ship Date"] - df["Order Date"]).dt.days

print("\n=== CLEANED DATA SNAPSHOT ===")
print(df.shape)
print(df.head(3))

# ── 4. BUSINESS QUESTIONS ───────────────────────────────────

# ── Q1: Which product category drives the most revenue? ─────
q1 = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\n--- Q1: Sales by Category ---")
print(q1)

ax = q1.plot(kind="bar", color=["#2196F3","#4CAF50","#FF9800"], edgecolor="white")
ax.set_title("Total Sales by Category", fontsize=14, fontweight="bold")
ax.set_xlabel("Category")
ax.set_ylabel("Total Sales ($)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
for p in ax.patches:
    ax.annotate(f"${p.get_height():,.0f}", (p.get_x() + p.get_width()/2, p.get_height()),
                ha="center", va="bottom", fontsize=9)
plt.tight_layout()
plt.savefig("outputs/q1_sales_by_category.png", dpi=150)
plt.clf()

# ── Q2: Which region is most profitable? ────────────────────
q2 = df.groupby("Region")[["Sales","Profit"]].sum().sort_values("Profit", ascending=False)
print("\n--- Q2: Profit by Region ---")
print(q2)

q2["Profit"].plot(kind="bar", color="#4CAF50", edgecolor="white")
plt.title("Total Profit by Region", fontsize=14, fontweight="bold")
plt.xlabel("Region")
plt.ylabel("Total Profit ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/q2_profit_by_region.png", dpi=150)
plt.clf()

# ── Q3: What is the monthly sales trend over time? ──────────
q3 = df.groupby("Order Month")["Sales"].sum()
print("\n--- Q3: Monthly Sales Trend ---")
print(q3.tail(12))

q3.plot(figsize=(14,4), color="#2196F3", linewidth=2)
plt.title("Monthly Sales Trend", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45, ha="right", fontsize=7)
plt.tight_layout()
plt.savefig("outputs/q3_monthly_sales_trend.png", dpi=150)
plt.clf()

# ── Q4: Which sub-categories are losing money? ──────────────
q4 = df.groupby("Sub-Category")[["Sales","Profit"]].sum().sort_values("Profit")
print("\n--- Q4: Sub-Category Profitability ---")
print(q4)

colors = ["#F44336" if p < 0 else "#4CAF50" for p in q4["Profit"]]
q4["Profit"].plot(kind="barh", color=colors, edgecolor="white", figsize=(8,7))
plt.title("Profit by Sub-Category", fontsize=14, fontweight="bold")
plt.xlabel("Total Profit ($)")
plt.axvline(0, color="black", linewidth=0.8)
plt.tight_layout()
plt.savefig("outputs/q4_subcategory_profit.png", dpi=150)
plt.clf()

# ── Q5: Which customer segment is most valuable? ────────────
q5 = df.groupby("Segment")[["Sales","Profit"]].sum()
q5["Profit Margin (%)"] = (q5["Profit"] / q5["Sales"] * 100).round(2)
print("\n--- Q5: Segment Performance ---")
print(q5)

q5["Profit"].plot(kind="pie", autopct="%1.1f%%",
                  colors=["#2196F3","#FF9800","#4CAF50"],
                  startangle=90, figsize=(6,6))
plt.title("Profit Share by Customer Segment", fontsize=14, fontweight="bold")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/q5_segment_profit_pie.png", dpi=150)
plt.clf()

# ── 5. EXPORT CLEAN DATA FOR POWER BI ───────────────────────
df.to_csv("outputs/superstore_clean.csv", index=False)
print("\n✅ Clean CSV exported to outputs/superstore_clean.csv")
print("✅ All 5 charts saved to outputs/")