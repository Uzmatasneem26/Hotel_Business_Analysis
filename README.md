# 🏨 Hotel Business Analysis Using Data Visualization

## 📌 Project Overview

Hotel businesses generate large amounts of booking data, but making effective decisions about occupancy, cancellations, seasonality, and customer booking behavior can be challenging.

This project analyzes hotel booking data to identify important patterns in booking demand and cancellation behavior. The analysis compares **City Hotel** and **Resort Hotel** and provides data-driven business recommendations for improving occupancy forecasting, operational planning, and cancellation management.

The project includes a **Streamlit dashboard** that allows users to explore the analysis interactively.

---

## 💼 Business Problem

The hotel industry receives a large volume of reservations across different customer segments, booking channels, stay durations, and time periods. However, hotels may face challenges in accurately understanding booking demand and predicting which reservations are likely to be cancelled.

High cancellation rates can lead to:

- Unexpected changes in occupancy levels
- Difficulty in forecasting future room demand
- Revenue uncertainty
- Inefficient staffing and resource planning
- Challenges in managing room inventory

Hotels also experience seasonal variations in booking demand, while cancellation behavior can differ based on factors such as **hotel type, stay duration, and booking lead time**.

Therefore, there is a need for a **data-driven approach** to analyze historical hotel booking data, identify patterns in demand and cancellations, and generate actionable insights that can support better business decision-making.

This project addresses the problem by analyzing historical hotel booking data and developing a Streamlit-based interactive dashboard to help understand:

- Which hotel type receives more bookings?
- Which months experience the highest and lowest demand?
- How does stay duration relate to cancellation behavior?
- Does booking lead time influence cancellation rates?
- What strategies can hotels use to improve occupancy forecasting and manage cancellation risk?

The ultimate goal is to transform historical booking data into **actionable business insights for occupancy planning, cancellation management, operational planning, and revenue-related decision-making**.

## 🎯 Business Objective

The objective of this project is to analyze hotel booking data and answer key business questions related to:

- Hotel booking demand
- Seasonal booking patterns
- Cancellation behavior
- Stay duration
- Booking lead time
- Differences between City Hotel and Resort Hotel
- Business recommendations for hotel management

---

## ❓ Key Business Questions

### 1. Which hotel type has higher booking demand?

Compare booking volumes between:

- City Hotel
- Resort Hotel

### 2. Does booking demand vary by month?

Identify:

- Busiest months
- Quietest months
- Seasonal booking patterns

### 3. Do longer stays have higher cancellation rates?

Analyze cancellation behavior across different stay-duration groups.

### 4. Does booking lead time affect cancellation?

Examine whether reservations made further in advance have a higher probability of cancellation.

### 5. What business actions can hotels take?

Translate the analytical findings into practical recommendations for:

- Occupancy forecasting
- Cancellation management
- Revenue planning
- Operational planning

---

## 📊 Dataset

The project uses hotel booking data containing **119,390 records and 29 columns** before cleaning.

The dataset includes information such as:

- Hotel type
- Cancellation status
- Lead time
- Arrival year
- Arrival month
- Stay duration
- Number of guests
- Meal type
- Market segment
- Distribution channel
- Customer type
- Average Daily Rate (ADR)
- Special requests
- Reservation status

---

## 🧹 Data Cleaning

The dataset was cleaned using Python and Pandas.

The cleaning process included:

- Handling missing values
- Removing duplicate records
- Replacing undefined meal values
- Removing negative ADR records
- Removing zero-guest bookings
- Creating total stay duration
- Converting arrival month into an ordered category
- Validating the cleaned dataset

### Final Dataset

After cleaning:

- **85,963 records**
- **30 columns**
- No remaining missing values

### Hotel Distribution

| Hotel Type | Bookings | Booking Share |
|---|---:|---:|
| City Hotel | 52,422 | 60.98% |
| Resort Hotel | 33,541 | 39.02% |

---

## 📈 Analysis Performed

### 1. Hotel Booking Demand

The analysis compares the number of bookings received by City Hotel and Resort Hotel.

**Key finding:**

City Hotel accounts for approximately **61%** of the cleaned bookings, while Resort Hotel accounts for approximately **39%**.

---

### 2. Monthly Booking Seasonality

Monthly booking patterns were analyzed for both hotel types.

**Key findings:**

- **October** is the busiest month for both hotel types.
- **March** is the quietest month for both hotel types.

This indicates a clear seasonal pattern in hotel demand.

---

### 3. Stay Duration & Cancellation

Cancellation rates were analyzed across different stay-duration groups:

- 0 nights
- 1–3 nights
- 4–7 nights
- 8–14 nights
- 15–21 nights
- 22–30 nights
- 31+ nights

The analysis also compares City Hotel and Resort Hotel.

**Key finding:**

Cancellation behavior varies across stay-duration groups, with City Hotel generally showing higher cancellation rates than Resort Hotel.

---

### 4. Lead Time & Cancellation

Bookings were grouped according to the number of days between booking and arrival:

- 0–7 days
- 8–30 days
- 31–60 days
- 61–90 days
- 91–180 days
- 181–365 days
- 365+ days

**Key finding:**

Cancellation rates generally increase with longer lead times up to the 181–365 day range. The 365+ day segment does not continue the same pattern, indicating that the relationship is not strictly linear.

---

## 💡 Key Business Insights

### 🏨 Hotel Type

City Hotel has a larger share of the observed bookings and generally experiences higher cancellation rates than Resort Hotel.

### 📅 Seasonality

October represents the highest booking demand, while March represents the lowest demand for both hotel types.

### 🛏️ Stay Duration

Cancellation behavior differs across stay-duration segments, suggesting that stay length can be useful when assessing cancellation risk.

### 📈 Lead Time

Advance bookings can have higher cancellation risk, particularly in longer lead-time segments.

---

## 🎯 Business Recommendations

### 1. Improve Cancellation-Aware Occupancy Forecasting

Hotels should not treat every reservation as guaranteed demand.

Historical cancellation patterns should be incorporated into occupancy forecasts to produce more realistic estimates of future room demand.

### 2. Monitor Long Lead-Time Reservations

Reservations made several months before arrival should receive additional monitoring because some long-lead-time segments show elevated cancellation rates.

### 3. Optimize Peak-Season Operations

Since October has the highest booking volume, hotels can prepare additional:

- Staffing
- Housekeeping capacity
- Room inventory
- Operational resources

for high-demand periods.

### 4. Use Hotel-Specific Strategies

City Hotel and Resort Hotel show different booking and cancellation patterns.

Therefore, cancellation-management and promotional strategies should be adapted to each hotel type instead of applying one strategy to both.

### 5. Use Differentiated Cancellation Policies

Hotels can evaluate:

- Flexible rates
- Non-refundable rates
- Deposits
- Confirmation reminders
- Targeted cancellation policies

for appropriate booking segments.

---

## ⭐ Highest-Impact Recommendation

### Cancellation-Aware Occupancy Forecasting

The most important recommendation from this analysis is to incorporate **historical cancellation behavior into future occupancy planning**.

Instead of treating every reservation as guaranteed demand, hotels should estimate expected cancellations when forecasting future occupancy and revenue.

This can help management make better decisions about:

- Room inventory
- Pricing
- Staffing
- Capacity planning
- Revenue expectations

---

## 🛠️ Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Dashboard

- Streamlit

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```text
Hotel_Business_Analysis/
│
├── app/
│   ├── home.py
│   ├── overview.py
│   ├── Hotel_Seasonality.py
│   ├── Stay_Cancellation.py
│   ├── Lead_Time_Cancellation.py
│   └── Recommendations.py
│
├── data/
│   ├── hotel_bookings_data.csv
│   └── hotel_bookings_cleaned.csv
│
├── src/
│   ├── data_cleaning.py
│   ├── hotel_analysis.py
│   ├── cancellation_analysis.py
│   └── visualizations.py
│
├── outputs/
│   └── charts/
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md