# Executive Summary: Superstore Sales Performance Analysis

**Prepared by:** [Marc Leveille]
**Date:** August 2026
**Data Period:** 2014–2017

## Overview

This analysis examined three years of retail transaction data (9,994 orders) to
identify revenue drivers, regional profitability gaps, seasonal demand patterns, and
underperforming product lines. The goal was to surface actionable insights for
pricing, inventory, and regional strategy decisions.

## Key Findings

**1. Revenue and profit do not always align by category.**
Technology generates the highest revenue (~$836K), but the West region produces
the highest overall profit (~$108K), even though it is not necessarily the top
Technology market. This suggests operational efficiency or discounting practices
vary meaningfully by region.

**2. Three sub-categories are actively losing money.**
Tables, Bookcases, and Supplies each show negative total profit despite
generating real sales volume. Tables alone represents a loss of over $17K.
This points to a pricing or discounting problem rather than a demand problem,
since the products are selling but at a loss.

**3. Sales are highly seasonal, peaking sharply in November.**
Monthly sales show a consistent seasonal spike each November, more than
double the typical monthly baseline. This has direct implications for
inventory planning and staffing ahead of Q4.

**4. Consumer segment drives volume; Corporate segment is more efficient.**
The Consumer segment generates the most total profit, but the Corporate
segment has a higher profit margin (13.0% vs. 11.6%), indicating more
efficient order economics per transaction.

## Recommendations

- **Audit discount policy on Tables, Bookcases, and Supplies** to investigate
  whether pricing or excessive discounting is driving negative margins.
- **Increase Q4 inventory and staffing** in anticipation of the November
  demand spike.
- **Study West region operations** as a potential best practice model for
  improving profitability in other regions.
- **Explore expanding Corporate segment outreach**, given its stronger
  margin performance relative to Consumer.

## Methodology

Data was cleaned and analyzed using Python (Pandas) to answer five core
business questions, then visualized in an interactive Power BI dashboard
featuring KPI tracking, category and regional breakdowns, and drill down
filters by Region, Category, Segment, and date range.