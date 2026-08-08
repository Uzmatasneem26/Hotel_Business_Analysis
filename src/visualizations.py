import os

import matplotlib.pyplot as plt
import seaborn as sns


# Create output folder
CHART_PATH = "outputs/charts"

os.makedirs(CHART_PATH, exist_ok=True)


def plot_hotel_booking_share(hotel_bookings):
    """
    Create a bar chart showing booking share
    between hotel types.
    """

    plt.figure(figsize=(8, 5))

    ax = sns.barplot(
        data=hotel_bookings,
        x="hotel",
        y="percentage"
    )

    plt.title("Booking Share by Hotel Type")
    plt.xlabel("Hotel Type")
    plt.ylabel("Booking Share (%)")

    # Add percentage labels
    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.1f%%"
        )

    plt.tight_layout()

    plt.savefig(
        f"{CHART_PATH}/hotel_booking_share.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()


def plot_monthly_bookings(monthly_bookings):
    """
    Create a line chart showing monthly bookings
    for City Hotel and Resort Hotel.
    """

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=monthly_bookings,
        x="arrival_date_month",
        y="bookings",
        hue="hotel",
        marker="o"
    )

    plt.title("Monthly Hotel Bookings by Hotel Type")
    plt.xlabel("Arrival Month")
    plt.ylabel("Number of Bookings")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        f"{CHART_PATH}/monthly_hotel_bookings.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

def plot_cancellation_rate_by_hotel(cancellation_rate):
    """
    Plot cancellation rate by hotel type.
    """

    plt.figure(figsize=(8, 5))

    ax = sns.barplot(
        data=cancellation_rate,
        x="hotel",
        y="cancellation_rate"
    )

    plt.title("Cancellation Rate by Hotel Type")
    plt.xlabel("Hotel Type")
    plt.ylabel("Cancellation Rate (%)")

    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.1f%%"
        )

    plt.tight_layout()

    plt.savefig(
        f"{CHART_PATH}/cancellation_rate_by_hotel.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()


def plot_cancellation_by_stay_duration(stay_analysis):
    """
    Plot cancellation rate by stay-duration group.
    """

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=stay_analysis,
        x="stay_duration_group",
        y="cancellation_rate",
        hue="hotel",
        marker="o"
    )

    plt.title(
        "Cancellation Rate by Stay Duration"
    )

    plt.xlabel("Stay Duration")
    plt.ylabel("Cancellation Rate (%)")

    plt.xticks(rotation=30)

    plt.legend(
        title="Hotel Type"
    )

    plt.tight_layout()

    plt.savefig(
        f"{CHART_PATH}/cancellation_by_stay_duration.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

def plot_cancellation_by_lead_time(lead_analysis):
    """
    Plot cancellation rate by lead-time group.
    """

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=lead_analysis,
        x="lead_time_group",
        y="cancellation_rate",
        hue="hotel",
        marker="o"
    )

    plt.title(
        "Cancellation Rate by Lead Time"
    )

    plt.xlabel(
        "Lead Time Before Arrival"
    )

    plt.ylabel(
        "Cancellation Rate (%)"
    )

    plt.xticks(rotation=30)

    plt.legend(
        title="Hotel Type"
    )

    plt.tight_layout()

    plt.savefig(
        f"{CHART_PATH}/cancellation_by_lead_time.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()