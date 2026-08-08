import pandas as pd


def hotel_booking_share(df):
    """
    Calculate the number and percentage of bookings
    for each hotel type.
    """

    hotel_bookings = (
        df["hotel"]
        .value_counts()
        .reset_index()
    )

    hotel_bookings.columns = [
        "hotel",
        "bookings"
    ]

    hotel_bookings["percentage"] = (
        hotel_bookings["bookings"]
        / hotel_bookings["bookings"].sum()
        * 100
    )

    return hotel_bookings


def monthly_booking_analysis(df):
    """
    Calculate monthly bookings for each hotel type.
    """

    monthly_bookings = (
        df.groupby(
            ["arrival_date_month", "hotel"],
            observed=False
        )
        .size()
        .reset_index(name="bookings")
    )

    return monthly_bookings


def get_monthly_summary(monthly_bookings):
    """
    Identify busiest and quietest months for each hotel type.
    """

    summary = {}

    for hotel in monthly_bookings["hotel"].unique():

        hotel_data = monthly_bookings[
            monthly_bookings["hotel"] == hotel
        ]

        busiest = hotel_data.loc[
            hotel_data["bookings"].idxmax()
        ]

        quietest = hotel_data.loc[
            hotel_data["bookings"].idxmin()
        ]

        summary[hotel] = {
            "busiest_month": busiest["arrival_date_month"],
            "busiest_bookings": busiest["bookings"],
            "quietest_month": quietest["arrival_date_month"],
            "quietest_bookings": quietest["bookings"]
        }

    return summary

def generate_hotel_insights(hotel_bookings, monthly_summary):
    """
    Generate key business insights from hotel booking analysis.
    """

    top_hotel = hotel_bookings.iloc[0]

    print("\n" + "=" * 60)
    print("BUSINESS INSIGHTS — HOTEL BOOKING ANALYSIS")
    print("=" * 60)

    print(
        f"\n1. {top_hotel['hotel']} is the most frequently booked "
        f"hotel type, accounting for "
        f"{top_hotel['percentage']:.2f}% of bookings."
    )

    for hotel, information in monthly_summary.items():

        print(
            f"\n2. {hotel}:"
        )

        print(
            f"   - Busiest month: "
            f"{information['busiest_month']} "
            f"({information['busiest_bookings']:,} bookings)"
        )

        print(
            f"   - Quietest month: "
            f"{information['quietest_month']} "
            f"({information['quietest_bookings']:,} bookings)"
        )

    print(
        "\n3. October is the busiest month for both hotel types, "
        "while March is the quietest month for both."
    )

    print(
        "\n4. The booking pattern indicates clear seasonality "
        "in hotel demand."
    )

def cancellation_rate_by_hotel(df):
    """
    Calculate cancellation rate for each hotel type.
    """

    cancellation_rate = (
        df.groupby("hotel")["is_canceled"]
        .mean()
        .reset_index()
    )

    cancellation_rate["cancellation_rate"] = (
        cancellation_rate["is_canceled"] * 100
    )

    cancellation_rate = cancellation_rate.drop(
        columns=["is_canceled"]
    )

    return cancellation_rate


def cancellation_rate_by_stay_duration(df):
    """
    Calculate cancellation rate by meaningful
    stay-duration groups.
    """

    df = df.copy()

    # Define stay-duration groups
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
        "1-3 nights",
        "4-7 nights",
        "8-14 nights",
        "15-21 nights",
        "22-30 nights",
        "31+ nights"
    ]

    df["stay_duration_group"] = pd.cut(
        df["total_stay_nights"],
        bins=bins,
        labels=labels
    )

    # Calculate bookings and cancellations
    stay_analysis = (
        df.groupby(
            ["hotel", "stay_duration_group"],
            observed=False
        )
        .agg(
            bookings=("is_canceled", "size"),
            cancellations=("is_canceled", "sum")
        )
        .reset_index()
    )

    # Calculate cancellation rate
    stay_analysis["cancellation_rate"] = (
        stay_analysis["cancellations"]
        / stay_analysis["bookings"]
        * 100
    )

    return stay_analysis

def cancellation_rate_by_lead_time(df):
    """
    Calculate cancellation rate by lead-time groups.

    Lead time = number of days between booking
    and the arrival date.
    """

    df = df.copy()

    # Define lead-time groups
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
        "0-7 days",
        "8-30 days",
        "31-60 days",
        "61-90 days",
        "91-180 days",
        "181-365 days",
        "365+ days"
    ]

    df["lead_time_group"] = pd.cut(
        df["lead_time"],
        bins=bins,
        labels=labels
    )

    # Calculate bookings and cancellations
    lead_analysis = (
        df.groupby(
            ["hotel", "lead_time_group"],
            observed=False
        )
        .agg(
            bookings=("is_canceled", "size"),
            cancellations=("is_canceled", "sum")
        )
        .reset_index()
    )

    # Calculate cancellation rate
    lead_analysis["cancellation_rate"] = (
        lead_analysis["cancellations"]
        / lead_analysis["bookings"]
        * 100
    )

    return lead_analysis