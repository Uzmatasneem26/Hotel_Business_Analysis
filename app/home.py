import streamlit as st


st.title("🏨 Hotel Business Analysis")

st.subheader(
    "Understanding Booking & Cancellation Behaviour"
)

st.markdown(
    """
    This interactive dashboard analyzes hotel booking data
    to understand customer booking patterns, seasonality,
    stay duration, and cancellation behaviour.
    """
)


st.divider()


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Dataset",
        "Hotel Bookings"
    )

with col2:
    st.metric(
        "Original Records",
        "119,390"
    )

with col3:
    st.metric(
        "Clean Records",
        "85,963"
    )


st.divider()


st.subheader("Business Questions")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        ### 🏨 Hotel Popularity

        Which hotel type receives the most bookings
        and how does demand change throughout the year?
        """
    )

with col2:
    st.markdown(
        """
        ### 🛏️ Stay Duration

        Does the length of a guest's stay affect
        the likelihood of cancellation?
        """
    )

with col3:
    st.markdown(
        """
        ### 📅 Lead Time

        Do bookings made further in advance have
        a higher cancellation rate?
        """
    )


st.divider()

st.info(
    "Use the navigation menu on the left to explore "
    "the analysis and business recommendations."
)