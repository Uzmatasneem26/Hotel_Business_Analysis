import os

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Hotel Overview",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# LOAD CLEANED DATA
# --------------------------------------------------

DATA_PATH = os.path.join(
    "data",
    "hotel_bookings_cleaned.csv"
)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    # Restore month ordering
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    df["arrival_date_month"] = pd.Categorical(
        df["arrival_date_month"],
        categories=months,
        ordered=True
    )

    return df


df = load_data()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Hotel Business Overview")

st.markdown(
    """
    Explore hotel booking patterns, hotel popularity,
    and cancellation behaviour using the cleaned dataset.
    """
)

st.divider()


# --------------------------------------------------
# SIDEBAR FILTER
# --------------------------------------------------

st.sidebar.header("Filters")

hotel_options = ["All"] + sorted(
    df["hotel"].dropna().unique().tolist()
)

selected_hotel = st.sidebar.selectbox(
    "Select Hotel Type",
    hotel_options
)


if selected_hotel != "All":
    filtered_df = df[
        df["hotel"] == selected_hotel
    ].copy()
else:
    filtered_df = df.copy()


# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

total_bookings = len(filtered_df)

city_bookings = len(
    filtered_df[
        filtered_df["hotel"] == "City Hotel"
    ]
)

resort_bookings = len(
    filtered_df[
        filtered_df["hotel"] == "Resort Hotel"
    ]
)

cancellation_rate = (
    filtered_df["is_canceled"].mean() * 100
)


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Bookings",
        f"{total_bookings:,}"
    )

with col2:
    st.metric(
        "City Hotel",
        f"{city_bookings:,}"
    )

with col3:
    st.metric(
        "Resort Hotel",
        f"{resort_bookings:,}"
    )

with col4:
    st.metric(
        "Cancellation Rate",
        f"{cancellation_rate:.1f}%"
    )


st.divider()


# --------------------------------------------------
# BOOKING SHARE
# --------------------------------------------------

st.subheader("🏨 Booking Share by Hotel Type")

booking_share = (
    filtered_df["hotel"]
    .value_counts()
    .reset_index()
)

booking_share.columns = [
    "hotel",
    "bookings"
]

booking_share["percentage"] = (
    booking_share["bookings"]
    / booking_share["bookings"].sum()
    * 100
)


fig, ax = plt.subplots(
    figsize=(8, 5)
)

sns.barplot(
    data=booking_share,
    x="hotel",
    y="percentage",
    ax=ax
)

ax.set_title(
    "Booking Share by Hotel Type"
)

ax.set_xlabel("Hotel Type")

ax.set_ylabel(
    "Booking Share (%)"
)

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.1f%%"
    )

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


# --------------------------------------------------
# MONTHLY BOOKING TREND
# --------------------------------------------------

st.subheader("📅 Monthly Booking Trend")

monthly_bookings = (
    filtered_df
    .groupby(
        ["arrival_date_month", "hotel"],
        observed=False
    )
    .size()
    .reset_index(
        name="bookings"
    )
)


fig, ax = plt.subplots(
    figsize=(12, 5)
)

sns.lineplot(
    data=monthly_bookings,
    x="arrival_date_month",
    y="bookings",
    hue="hotel",
    marker="o",
    ax=ax
)

ax.set_title(
    "Monthly Hotel Bookings"
)

ax.set_xlabel("Month")

ax.set_ylabel(
    "Number of Bookings"
)

plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


# --------------------------------------------------
# CANCELLATION OVERVIEW
# --------------------------------------------------

st.subheader("❌ Cancellation Overview")

cancellation_data = (
    filtered_df["is_canceled"]
    .value_counts()
    .rename(
        index={
            0: "Not Cancelled",
            1: "Cancelled"
        }
    )
    .reset_index()
)

cancellation_data.columns = [
    "status",
    "bookings"
]


fig, ax = plt.subplots(
    figsize=(8, 5)
)

sns.barplot(
    data=cancellation_data,
    x="status",
    y="bookings",
    ax=ax
)

ax.set_title(
    "Cancelled vs Non-Cancelled Bookings"
)

ax.set_xlabel("Reservation Status")

ax.set_ylabel(
    "Number of Bookings"
)

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%d"
    )

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


# --------------------------------------------------
# BUSINESS INSIGHT
# --------------------------------------------------

st.divider()

st.subheader("💡 Key Insight")

if selected_hotel == "All":

    st.info(
        f"""
        **City Hotel** accounts for approximately **61%**
        of cleaned bookings, making it the more frequently
        booked hotel type.

        The overall cancellation rate is approximately
        **{cancellation_rate:.1f}%**.
        """
    )

else:

    st.info(
        f"""
        For **{selected_hotel}**, the current filtered dataset
        contains **{total_bookings:,} bookings** with an overall
        cancellation rate of **{cancellation_rate:.1f}%**.
        """
    )