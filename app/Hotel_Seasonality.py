import os

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Hotel & Seasonality",
    page_icon="🏨",
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

    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
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

st.title("🏨 Hotel & Seasonality Analysis")

st.markdown(
    """
    This page analyzes hotel booking demand across hotel types
    and months to identify booking patterns, peak periods,
    and low-demand periods.
    """
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Analysis Filters")

hotel_options = ["All"] + sorted(
    df["hotel"].dropna().unique()
)

selected_hotel = st.sidebar.selectbox(
    "Hotel Type",
    hotel_options
)


if selected_hotel == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["hotel"] == selected_hotel
    ].copy()


# --------------------------------------------------
# HOTEL BOOKING SHARE
# --------------------------------------------------

st.subheader("📊 Booking Share by Hotel Type")

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


col1, col2 = st.columns([2, 1])


with col1:

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


with col2:

    st.markdown("### Booking Summary")

    for _, row in booking_share.iterrows():

        st.metric(
            row["hotel"],
            f"{row['bookings']:,}",
            f"{row['percentage']:.1f}%"
        )


st.divider()


# --------------------------------------------------
# MONTHLY BOOKINGS
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
    figsize=(13, 6)
)

sns.lineplot(
    data=monthly_bookings,
    x="arrival_date_month",
    y="bookings",
    hue="hotel",
    marker="o",
    linewidth=2,
    ax=ax
)

ax.set_title(
    "Monthly Bookings by Hotel Type"
)

ax.set_xlabel("Arrival Month")

ax.set_ylabel(
    "Number of Bookings"
)

plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


st.divider()


# --------------------------------------------------
# BUSIEST / QUIETEST MONTH
# --------------------------------------------------

st.subheader("📈 Peak and Low-Demand Periods")


summary_data = []

for hotel in filtered_df["hotel"].unique():

    hotel_monthly = monthly_bookings[
        monthly_bookings["hotel"] == hotel
    ]

    busiest = hotel_monthly.loc[
        hotel_monthly["bookings"].idxmax()
    ]

    quietest = hotel_monthly.loc[
        hotel_monthly["bookings"].idxmin()
    ]

    summary_data.append(
        {
            "Hotel": hotel,
            "Busiest Month":
                busiest["arrival_date_month"],
            "Busiest Bookings":
                int(busiest["bookings"]),
            "Quietest Month":
                quietest["arrival_date_month"],
            "Quietest Bookings":
                int(quietest["bookings"])
        }
    )


summary_df = pd.DataFrame(summary_data)


st.dataframe(
    summary_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------

st.subheader("💡 Business Insights")


if selected_hotel == "All":

    st.success(
        """
        **Key findings**

        • City Hotel accounts for approximately **61%** of
        cleaned bookings, making it the more frequently booked
        hotel type.

        • **October** is the busiest month for both City Hotel
        and Resort Hotel.

        • **March** is the quietest month for both hotel types.

        • The monthly pattern indicates clear seasonality
        in hotel booking demand.
        """
    )

else:

    hotel_monthly = monthly_bookings[
        monthly_bookings["hotel"] == selected_hotel
    ]

    busiest = hotel_monthly.loc[
        hotel_monthly["bookings"].idxmax()
    ]

    quietest = hotel_monthly.loc[
        hotel_monthly["bookings"].idxmin()
    ]

    st.info(
        f"""
        **{selected_hotel}**

        • Busiest month: **{busiest['arrival_date_month']}**
        with **{int(busiest['bookings']):,} bookings**.

        • Quietest month: **{quietest['arrival_date_month']}**
        with **{int(quietest['bookings']):,} bookings**.

        • The difference between peak and low-demand periods
        indicates seasonal variation in booking demand.
        """
    )


# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

st.subheader("🎯 Operational Implications")

st.markdown(
    """
    **During high-demand periods**

    - Plan staffing and housekeeping capacity in advance.
    - Optimize room availability and inventory.
    - Consider demand-based pricing strategies.

    **During low-demand periods**

    - Consider targeted promotional campaigns.
    - Encourage advance bookings with suitable offers.
    - Explore weekend or seasonal packages to improve demand.
    """
)