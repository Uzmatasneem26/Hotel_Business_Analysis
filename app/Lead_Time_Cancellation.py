import os

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Lead Time & Cancellation",
    page_icon="📅",
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
    return pd.read_csv(DATA_PATH)


df = load_data()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📅 Lead Time & Cancellation Analysis")

st.markdown(
    """
    This analysis examines whether bookings made further
    in advance have a higher cancellation rate.
    """
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Analysis Filters")

hotel_options = ["All"] + sorted(
    df["hotel"].dropna().unique().tolist()
)

selected_hotel = st.sidebar.selectbox(
    "Select Hotel Type",
    hotel_options
)

if selected_hotel == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["hotel"] == selected_hotel
    ].copy()


# --------------------------------------------------
# LEAD TIME GROUPS
# --------------------------------------------------

bins = [
    -1,
    7,
    30,
    60,
    90,
    180,
    365,
    float("inf")
]

labels = [
    "0–7 days",
    "8–30 days",
    "31–60 days",
    "61–90 days",
    "91–180 days",
    "181–365 days",
    "365+ days"
]

filtered_df["lead_time_group"] = pd.cut(
    filtered_df["lead_time"],
    bins=bins,
    labels=labels
)


# --------------------------------------------------
# CANCELLATION RATE
# --------------------------------------------------

lead_cancellation = (
    filtered_df
    .groupby(
        ["lead_time_group", "hotel"],
        observed=False
    )["is_canceled"]
    .mean()
    .reset_index()
)

lead_cancellation["cancellation_rate"] = (
    lead_cancellation["is_canceled"] * 100
)


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

overall_rate = (
    filtered_df["is_canceled"].mean() * 100
)

average_lead_time = (
    filtered_df["lead_time"].mean()
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Bookings",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Cancellation Rate",
        f"{overall_rate:.1f}%"
    )

with col3:
    st.metric(
        "Average Lead Time",
        f"{average_lead_time:.0f} days"
    )


st.divider()


# --------------------------------------------------
# MAIN CHART
# --------------------------------------------------

st.subheader(
    "📈 Lead Time vs Cancellation Rate"
)


fig, ax = plt.subplots(
    figsize=(13, 6)
)

sns.lineplot(
    data=lead_cancellation,
    x="lead_time_group",
    y="cancellation_rate",
    hue="hotel",
    marker="o",
    linewidth=2,
    ax=ax
)

ax.set_title(
    "Cancellation Rate by Lead Time"
)

ax.set_xlabel(
    "Lead Time Before Arrival"
)

ax.set_ylabel(
    "Cancellation Rate (%)"
)

ax.legend(
    title="Hotel Type"
)

plt.xticks(rotation=30)

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


st.divider()


# --------------------------------------------------
# DATA TABLE
# --------------------------------------------------

st.subheader(
    "📋 Lead Time Cancellation Rates"
)

display_df = lead_cancellation[
    [
        "lead_time_group",
        "hotel",
        "cancellation_rate"
    ]
].copy()

display_df["cancellation_rate"] = (
    display_df["cancellation_rate"]
    .round(2)
)

display_df.columns = [
    "Lead Time",
    "Hotel Type",
    "Cancellation Rate (%)"
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


# --------------------------------------------------
# HIGHEST / LOWEST CANCELLATION
# --------------------------------------------------

st.subheader(
    "🔎 Highest and Lowest Cancellation Groups"
)

valid_groups = lead_cancellation.dropna(
    subset=["cancellation_rate"]
)

if not valid_groups.empty:

    highest = valid_groups.loc[
        valid_groups["cancellation_rate"].idxmax()
    ]

    lowest = valid_groups.loc[
        valid_groups["cancellation_rate"].idxmin()
    ]

    col1, col2 = st.columns(2)

    with col1:

        st.warning(
            f"""
            **Highest cancellation rate**

            Hotel: **{highest['hotel']}**

            Lead time: **{highest['lead_time_group']}**

            Cancellation rate:
            **{highest['cancellation_rate']:.1f}%**
            """
        )

    with col2:

        st.success(
            f"""
            **Lowest cancellation rate**

            Hotel: **{lowest['hotel']}**

            Lead time: **{lowest['lead_time_group']}**

            Cancellation rate:
            **{lowest['cancellation_rate']:.1f}%**
            """
        )


st.divider()


# --------------------------------------------------
# HOTEL COMPARISON
# --------------------------------------------------

st.subheader(
    "🏨 City Hotel vs Resort Hotel"
)

hotel_rates = (
    filtered_df
    .groupby("hotel")["is_canceled"]
    .mean()
    .mul(100)
    .reset_index()
)

hotel_rates.columns = [
    "Hotel Type",
    "Cancellation Rate"
]


fig, ax = plt.subplots(
    figsize=(8, 5)
)

sns.barplot(
    data=hotel_rates,
    x="Hotel Type",
    y="Cancellation Rate",
    ax=ax
)

ax.set_title(
    "Overall Cancellation Rate by Hotel Type"
)

ax.set_ylabel(
    "Cancellation Rate (%)"
)

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.1f%%"
    )

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


st.divider()


# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------

st.subheader("💡 Business Insights")

st.info(
    """
    **Key findings**

    • Cancellation rates generally increase as lead time
    increases across the shorter and medium booking windows.

    • City Hotel generally has higher cancellation rates
    than Resort Hotel.

    • The 181–365 day segment shows particularly high
    cancellation levels.

    • The 365+ day segment does not continue the same
    upward pattern, so the relationship is not strictly
    linear.
    """
)


# --------------------------------------------------
# BUSINESS RECOMMENDATIONS
# --------------------------------------------------

st.subheader("🎯 Business Recommendations")

st.markdown(
    """
    **1. Monitor long-lead-time reservations**

    Reservations made several months before arrival should
    be monitored because they can carry greater cancellation
    risk.

    **2. Improve occupancy forecasting**

    Future occupancy forecasts should account for expected
    cancellations rather than treating every advance booking
    as guaranteed demand.

    **3. Use appropriate booking policies**

    Hotels can evaluate deposits, non-refundable rates,
    flexible rates, or reminder campaigns for selected
    high-risk booking segments.

    **4. Differentiate strategies by hotel type**

    Since City Hotel and Resort Hotel show different
    cancellation behaviour, cancellation-management
    strategies should be tailored to each property.
    """
)