
from src.data_cleaning import load_data, clean_data

from src.hotel_analysis import (
    hotel_booking_share,
    monthly_booking_analysis,
    get_monthly_summary,
    generate_hotel_insights,
    cancellation_rate_by_hotel,
    cancellation_rate_by_stay_duration,
    cancellation_rate_by_lead_time
)

from src.visualizations import (
    plot_hotel_booking_share,
    plot_monthly_bookings,
    plot_cancellation_rate_by_hotel,
    plot_cancellation_by_stay_duration,
    plot_cancellation_by_lead_time
)

# --------------------------------------------------
# PROJECT CONFIGURATION
# --------------------------------------------------

DATA_PATH = "data/hotel_bookings_data.csv"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = load_data(DATA_PATH)

print("=" * 60)
print("HOTEL BUSINESS ANALYSIS")
print("=" * 60)

print("\nDataset loaded successfully!")

print(f"Original rows    : {df.shape[0]}")
print(f"Original columns : {df.shape[1]}")


# --------------------------------------------------
# DATA CLEANING
# --------------------------------------------------

df = clean_data(df)


# --------------------------------------------------
# CHECK CLEANED DATA
# --------------------------------------------------

print("\n" + "=" * 60)
print("CLEANED DATA PREVIEW")
print("=" * 60)

print(df.head())

print("\nMissing values after cleaning:")

missing_values = df.isnull().sum()

missing_values = missing_values[
    missing_values > 0
].sort_values(ascending=False)

print(missing_values)

print("\nHotel types after cleaning:")
print(df["hotel"].value_counts())

print("\nCancellation status after cleaning:")
print(df["is_canceled"].value_counts())

# --------------------------------------------------
# HOTEL TYPE ANALYSIS
# --------------------------------------------------

print("\n" + "=" * 60)
print("HOTEL TYPE BOOKING ANALYSIS")
print("=" * 60)

hotel_bookings = hotel_booking_share(df)

print("\nBooking share by hotel type:")
print(hotel_bookings.to_string(index=False))


# --------------------------------------------------
# MONTHLY BOOKING ANALYSIS
# --------------------------------------------------

monthly_bookings = monthly_booking_analysis(df)

print("\n" + "=" * 60)
print("MONTHLY BOOKING ANALYSIS")
print("=" * 60)

print(
    monthly_bookings.to_string(index=False)
)


# --------------------------------------------------
# MONTHLY SUMMARY
# --------------------------------------------------

monthly_summary = get_monthly_summary(
    monthly_bookings
)

generate_hotel_insights(
    hotel_bookings,
    monthly_summary
)

print("\n" + "=" * 60)
print("BUSIEST AND QUIETEST MONTHS")
print("=" * 60)

for hotel, information in monthly_summary.items():

    print(f"\n{hotel}")

    print(
        f"Busiest month: "
        f"{information['busiest_month']} "
        f"({information['busiest_bookings']} bookings)"
    )

    print(
        f"Quietest month: "
        f"{information['quietest_month']} "
        f"({information['quietest_bookings']} bookings)"
    )


# --------------------------------------------------
# CREATE VISUALIZATIONS
# --------------------------------------------------

plot_hotel_booking_share(
    hotel_bookings
)

plot_monthly_bookings(
    monthly_bookings
)

# --------------------------------------------------
# CANCELLATION ANALYSIS
# --------------------------------------------------

print("\n" + "=" * 60)
print("CANCELLATION RATE BY HOTEL TYPE")
print("=" * 60)

cancellation_rate = cancellation_rate_by_hotel(df)

print(
    cancellation_rate.to_string(index=False)
)


# --------------------------------------------------
# STAY DURATION ANALYSIS
# --------------------------------------------------

print("\n" + "=" * 60)
print("CANCELLATION RATE BY STAY DURATION")
print("=" * 60)

stay_analysis = cancellation_rate_by_stay_duration(df)

print("\nStay duration sample sizes:")

print(
    stay_analysis[
        [
            "hotel",
            "stay_duration_group",
            "bookings",
            "cancellations",
            "cancellation_rate"
        ]
    ].to_string(index=False)
)

print(
    stay_analysis.to_string(index=False)
)


# --------------------------------------------------
# CANCELLATION VISUALIZATIONS
# --------------------------------------------------

plot_cancellation_rate_by_hotel(
    cancellation_rate
)

plot_cancellation_by_stay_duration(
    stay_analysis
)

# --------------------------------------------------
# ANALYSIS 3: LEAD TIME VS CANCELLATION
# --------------------------------------------------

print("\n" + "=" * 60)
print("CANCELLATION RATE BY LEAD TIME")
print("=" * 60)

lead_analysis = cancellation_rate_by_lead_time(df)

print(
    lead_analysis[
        [
            "hotel",
            "lead_time_group",
            "bookings",
            "cancellations",
            "cancellation_rate"
        ]
    ].to_string(index=False)
)


# --------------------------------------------------
# LEAD TIME VISUALIZATION
# --------------------------------------------------

plot_cancellation_by_lead_time(
    lead_analysis
)