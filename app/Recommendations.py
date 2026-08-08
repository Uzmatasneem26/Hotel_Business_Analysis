import streamlit as st


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Recommendations",
    page_icon="🎯",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎯 Business Insights & Recommendations")

st.markdown(
    """
    This section summarizes the major findings from the
    hotel booking analysis and translates them into
    practical business recommendations.
    """
)

st.divider()


# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------

st.header("📌 Executive Summary")

st.markdown(
    """
    The analysis of hotel booking data reveals clear
    differences in booking demand and cancellation behaviour
    between City Hotel and Resort Hotel.

    Booking demand also varies considerably by month,
    indicating seasonal patterns that can influence staffing,
    room pricing, inventory planning, and promotional activity.

    Cancellation behaviour is also influenced by stay duration
    and lead time, meaning that hotels should consider the
    probability of cancellation when forecasting future
    occupancy.
    """
)


# --------------------------------------------------
# KEY FINDINGS
# --------------------------------------------------

st.header("🔎 Key Findings")

col1, col2 = st.columns(2)


with col1:

    st.subheader("🏨 Hotel Type")

    st.markdown(
        """
        - City Hotel accounts for approximately **61%**
          of cleaned bookings.
        - Resort Hotel accounts for approximately **39%**.
        - City Hotel therefore represents the larger share
          of observed booking demand.
        """
    )


    st.subheader("📅 Seasonality")

    st.markdown(
        """
        - **October** is the busiest month for both hotel
          types.
        - **March** is the quietest month for both hotel
          types.
        - This indicates a clear seasonal pattern in demand.
        """ 
    )


with col2:

    st.subheader("🛏️ Stay Duration")

    st.markdown(
        """
        - Cancellation behaviour varies across stay-duration
          groups.
        - City Hotel generally shows higher cancellation
          rates than Resort Hotel.
        - Longer-stay segments should be monitored carefully.
        """
    )


    st.subheader("📈 Lead Time")

    st.markdown(
        """
        - Cancellation rates generally increase with longer
          booking lead times up to the 181–365 day range.
        - City Hotel generally has higher cancellation rates.
        - The 365+ day segment does not continue the same
          upward pattern, so the relationship is not strictly
          linear.
        """
    )


st.divider()


# --------------------------------------------------
# RECOMMENDATION 1
# --------------------------------------------------

st.header("1️⃣ Optimize Peak-Season Operations")

st.markdown(
    """
    ### Finding

    October has the highest booking volume for both City Hotel
    and Resort Hotel.

    ### Recommendation

    Hotels should prepare additional operational capacity
    before high-demand periods.

    This can include:

    - Adjusting staffing levels.
    - Planning housekeeping capacity.
    - Optimizing room inventory.
    - Preparing sufficient operational resources.
    - Reviewing room pricing during peak demand.
    """
)

st.success(
    "Expected impact: Better capacity planning and improved "
    "revenue opportunities during high-demand periods."
)


# --------------------------------------------------
# RECOMMENDATION 2
# --------------------------------------------------

st.header("2️⃣ Manage Long-Lead-Time Bookings")

st.markdown(
    """
    ### Finding

    Bookings made far in advance generally show higher
    cancellation rates, particularly within the
    181–365 day range.

    ### Recommendation

    Hotels should monitor advance bookings more closely
    instead of treating all future reservations as equally
    reliable.

    Possible actions include:

    - Sending confirmation reminders.
    - Monitoring high-risk reservations.
    - Offering suitable non-refundable rate options.
    - Evaluating deposit requirements.
    - Including expected cancellations in occupancy forecasts.
    """
)

st.warning(
    "Expected impact: More accurate future occupancy forecasts "
    "and reduced exposure to unexpected cancellations."
)


# --------------------------------------------------
# RECOMMENDATION 3
# --------------------------------------------------

st.header("3️⃣ Manage Cancellation Risk by Stay Duration")

st.markdown(
    """
    ### Finding

    Cancellation behaviour differs across stay-duration
    segments and between City Hotel and Resort Hotel.

    ### Recommendation

    Hotels should monitor higher-risk stay-duration segments
    and avoid applying one cancellation policy to every
    customer.

    Possible actions include:

    - Segment-specific cancellation policies.
    - Flexible and non-refundable rate options.
    - Deposits for selected booking segments.
    - Monitoring expected revenue at risk.
    """
)

st.info(
    "Expected impact: Better cancellation-risk management "
    "while maintaining flexibility for customers."
)


# --------------------------------------------------
# RECOMMENDATION 4
# --------------------------------------------------

st.header("4️⃣ Use Hotel-Specific Strategies")

st.markdown(
    """
    City Hotel and Resort Hotel have different booking
    volumes and cancellation patterns.

    Therefore, management should avoid using exactly the same
    strategy for both properties.

    **City Hotel**

    - Higher booking volume.
    - Generally higher cancellation rates.
    - Requires stronger cancellation-risk monitoring.

    **Resort Hotel**

    - Lower overall booking volume.
    - Different seasonal and cancellation behaviour.
    - Can use targeted promotions during lower-demand periods.
    """
)


st.divider()


# --------------------------------------------------
# HIGHEST IMPACT RECOMMENDATION
# --------------------------------------------------

st.header("⭐ Highest-Impact Recommendation")

st.success(
    """
    ### Improve cancellation-aware occupancy forecasting

    The most important recommendation is to incorporate
    historical cancellation behaviour into future occupancy
    planning.

    Hotels should not treat every advance reservation as
    guaranteed demand. Instead, expected cancellations should
    be considered when estimating future occupancy and
    revenue.

    This is particularly important for bookings made far in
    advance, where cancellation risk is generally higher.
    """
)


# --------------------------------------------------
# BUSINESS IMPACT
# --------------------------------------------------

st.header("📊 Expected Business Impact")

impact_data = {
    "Area": [
        "Revenue Management",
        "Occupancy Forecasting",
        "Operations",
        "Cancellation Management",
        "Customer Strategy"
    ],
    "Potential Improvement": [
        "Better pricing decisions during peak periods",
        "More realistic future occupancy estimates",
        "Better staffing and resource planning",
        "Reduced exposure to high-risk reservations",
        "More targeted booking policies"
    ]
}

import pandas as pd

impact_df = pd.DataFrame(impact_data)

st.dataframe(
    impact_df,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# FINAL CONCLUSION
# --------------------------------------------------

st.divider()

st.header("🏁 Final Conclusion")

st.markdown(
    """
    The analysis demonstrates that hotel demand and
    cancellation behaviour are not uniform across all
    reservations.

    Hotel type, seasonality, stay duration, and lead time
    provide useful information for understanding booking
    behaviour.

    By combining these insights with cancellation-aware
    forecasting and hotel-specific strategies, management can
    make better decisions about pricing, capacity planning,
    inventory, and cancellation policies.
    """
)