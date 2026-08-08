import pandas as pd


def load_data(file_path):
    """Load the hotel booking dataset."""
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """Clean and prepare the hotel booking dataset."""

    df = df.copy()

    print("=" * 60)
    print("STARTING DATA CLEANING")
    print("=" * 60)

    # --------------------------------------------------
    # 1. Missing values
    # --------------------------------------------------

    # Missing children values are treated as zero children
    df["children"] = df["children"].fillna(0)

    # Missing company/agent means no company/agent was recorded
    df["company"] = df["company"].fillna(0)
    df["agent"] = df["agent"].fillna(0)

    # Missing city is labelled as Unknown
    df["city"] = df["city"].fillna("Unknown")

    print("\nMissing values handled.")

    # --------------------------------------------------
    # 2. Remove duplicate rows
    # --------------------------------------------------

    duplicate_count = df.duplicated().sum()

    df = df.drop_duplicates().reset_index(drop=True)

    print(f"Duplicate rows removed: {duplicate_count}")

    # --------------------------------------------------
    # 3. Handle Undefined meal values
    # --------------------------------------------------

    undefined_meals = (df["meal"] == "Undefined").sum()

    df["meal"] = df["meal"].replace(
        "Undefined",
        "No Meal"
    )

    print(f"Undefined meal values changed: {undefined_meals}")

    # --------------------------------------------------
    # 4. Remove negative ADR
    # --------------------------------------------------

    negative_adr_count = (df["adr"] < 0).sum()

    df = df[df["adr"] >= 0].copy()

    print(f"Negative ADR rows removed: {negative_adr_count}")

    # --------------------------------------------------
    # 5. Remove bookings with zero guests
    # --------------------------------------------------

    zero_guest_mask = (
        (df["adults"] == 0) &
        (df["children"] == 0) &
        (df["babies"] == 0)
    )

    zero_guest_count = zero_guest_mask.sum()

    df = df[~zero_guest_mask].copy()

    print(f"Zero-guest bookings removed: {zero_guest_count}")

    # --------------------------------------------------
    # 6. Create total stay duration
    # --------------------------------------------------

    df["total_stay_nights"] = (
        df["stays_in_weekend_nights"] +
        df["stays_in_weekdays_nights"]
    )

    print("\nTotal stay duration column created.")

    # --------------------------------------------------
    # 7. Create arrival date
    # --------------------------------------------------

    month_order = [
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
        categories=month_order,
        ordered=True
    )

    print("Arrival month converted to ordered category.")

    # --------------------------------------------------
    # Final information
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("CLEANING COMPLETED")
    print("=" * 60)

    print(f"Final rows    : {df.shape[0]}")
    print(f"Final columns : {df.shape[1]}")

    # Save cleaned dataset
    cleaned_path = "data/hotel_bookings_cleaned.csv"

    df.to_csv(cleaned_path, index=False)

    print(f"\nCleaned dataset saved to: {cleaned_path}")

    return df
    

