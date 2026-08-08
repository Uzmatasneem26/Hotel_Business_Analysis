import os

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Stay Duration & Cancellation",
    page_icon="🛏️",
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

    return df


df = load_data()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🛏️ Stay Duration & Cancellation Analysis")

st.markdown(
    """
    This analysis examines whether the length of a guest's
    stay is associated with the likelihood of cancellation.
    """
)

st.divider()


# --------------------------------------------------
# SIDEBAR FILTER
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
# CREATE STAY DURATION GROUPS
# --------------------------------------------------

bins = [
    -1,
    0,
    3,
    7,
    14,
    21,
    30,
    float("inf")
]

labels = [
    "0 nights",
    "1–3 nights",
    "4–7 nights",
    "8–14 nights",
    "15–21 nights",
    "22–30 nights",
    "31+ nights"
]

filtered_df["stay_duration_group"] = pd.cut(
    filtered_df["total_stay_nights"],
    bins=bins,
    labels=labels
)


# --------------------------------------------------
# CANCELLATION RATE
# --------------------------------------------------

stay_cancellation = (
    filtered_df
    .groupby(
        ["stay_duration_group", "hotel"],
        observed=False
    )["is_canceled"]
    .mean()
    .reset_index()
)

stay_cancellation["cancellation_rate"] = (
    stay_cancellation["is_canceled"] * 100
)


# --------------------------------------------------
# OVERALL CANCELLATION RATE
# --------------------------------------------------

overall_rate = (
    filtered_df["is_canceled"].mean() * 100
)


# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Total Bookings",
        f"{len(filtered_df):,}"
    )

with col2:

    st.metric(
        "Overall Cancellation Rate",
        f"{overall_rate:.1f}%"
    )

with col3:

    average_stay = filtered_df[
        "total_stay_nights"
    ].mean()

    st.metric(
        "Average Stay",
        f"{average_stay:.1f} nights"
    )


st.divider()


# --------------------------------------------------
# CANCELLATION RATE BY STAY DURATION
# --------------------------------------------------

st.subheader(
    "📊 Cancellation Rate by Stay Duration"
)


fig, ax = plt.subplots(
    figsize=(13, 6)
)

sns.barplot(
    data=stay_cancellation,
    x="stay_duration_group",
    y="cancellation_rate",
    hue="hotel",
    ax=ax
)

ax.set_title(
    "Cancellation Rate by Stay Duration"
)

ax.set_xlabel(
    "Stay Duration"
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
# CANCELLATION RATE TABLE
# --------------------------------------------------

st.subheader(
    "📋 Cancellation Rate Details"
)

display_df = stay_cancellation[
    [
        "stay_duration_group",
        "hotel",
        "cancellation_rate"
    ]
].copy()

display_df["cancellation_rate"] = (
    display_df["cancellation_rate"]
    .round(2)
)

display_df.columns = [
    "Stay Duration",
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
# HOTEL COMPARISON
# --------------------------------------------------

st.subheader(
    "🏨 City Hotel vs Resort Hotel"
)


hotel_cancellation = (
    filtered_df
    .groupby("hotel")["is_canceled"]
    .mean()
    .mul(100)
    .reset_index()
)

hotel_cancellation.columns = [
    "Hotel Type",
    "Cancellation Rate"
]


fig, ax = plt.subplots(
    figsize=(8, 5)
)

sns.barplot(
    data=hotel_cancellation,
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
# FIND HIGHEST / LOWEST CANCELLATION GROUPS
# --------------------------------------------------

st.subheader(
    "🔎 Highest and Lowest Cancellation Groups"
)


valid_groups = stay_cancellation.dropna(
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

            Stay duration:
            **{highest['stay_duration_group']}**

            Cancellation rate:
            **{highest['cancellation_rate']:.1f}%**
            """
        )

    with col2:

        st.success(
            f"""
            **Lowest cancellation rate**

            Hotel: **{lowest['hotel']}**

            Stay duration:
            **{lowest['stay_duration_group']}**

            Cancellation rate:
            **{lowest['cancellation_rate']:.1f}%**
            """
        )


st.divider()


# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------

st.subheader("💡 Business Insights")

st.info(
    """
    **Key findings**

    • Cancellation behaviour varies across different
    stay-duration groups.

    • City Hotel generally shows higher cancellation
    rates than Resort Hotel.

    • Longer stays should be monitored carefully because
    some longer-duration segments show elevated
    cancellation rates.

    • The relationship is not perfectly linear, so hotels
    should avoid assuming that every longer stay has a
    higher cancellation probability.
    """
)


# --------------------------------------------------
# BUSINESS RECOMMENDATIONS
# --------------------------------------------------

st.subheader("🎯 Business Recommendations")

st.markdown(
    """
    **1. Monitor longer-duration reservations**

    Reservations involving longer stays can represent
    significant expected room revenue. High-risk segments
    should therefore be monitored more closely.

    **2. Consider differentiated cancellation policies**

    Hotels can evaluate deposits, flexible rates, and
    non-refundable options for selected booking segments.

    **3. Improve occupancy forecasting**

    Cancellation patterns should be incorporated into
    expected occupancy rather than treating every booking
    as guaranteed demand.

    **4. Compare City and Resort Hotel behaviour**

    Since cancellation behaviour differs between hotel types,
    a single cancellation strategy may not be appropriate
    for both properties.
    """
)