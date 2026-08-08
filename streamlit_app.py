import streamlit as st


st.set_page_config(
    page_title="Hotel Business Analysis",
    page_icon="🏨",
    layout="wide"
)


pages = {
    "Dashboard": [
        st.Page(
            "app/home.py",
            title="Home",
            icon="🏠",
            default=True
        ),
        st.Page(
            "app/overview.py",
            title="Overview",
            icon="📊"
        ),
        st.Page(
            "app/Hotel_Seasonality.py",
            title="Hotel & Seasonality",
            icon="🏨"
        ),
        st.Page(
            "app/Stay_Cancellation.py",
            title="Stay & Cancellation",
            icon="🛏️"
        ),
        st.Page(
            "app/Lead_Time_Cancellation.py",
            title="Lead Time & Cancellation",
            icon="📅"
        ),
        st.Page(
            "app/Recommendations.py",
            title="Recommendations",
            icon="🎯"
        )
    ]
}


pg = st.navigation(pages)

pg.run()