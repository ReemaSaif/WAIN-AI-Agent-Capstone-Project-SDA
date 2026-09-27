import streamlit as st
from agent.wain_agent import run_wain
import urllib.parse

# PAGE CONFIGURATION

st.set_page_config(
    page_title="WAIN | AI Place Recommendation Assistant",
    page_icon="🤖",
    layout="centered"
)


# CUSTOM CSS

st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 2rem;
    }

    /* WAIN Title */
    .wain-title {
        font-size: 6rem;
        font-weight: 700;
        color: #165823;
        margin: 0;
        position: relative;
        top: -5px;
    }

    /* Subtitle */
    .wain-subtitle {
        text-align: center;
        font-size: 1.4rem;
        margin-top: 0.3rem;
        margin-bottom: 1.5rem;
        color: #065911;
        font-weight: 600;
        font-style: italic;
    }

    /* Intro text */
    .intro-text {
        text-align: center;
        font-size: 1.4rem;
        margin-bottom: 2rem;
        color: #065911;
        font-weight: 600;
        font-style: italic;
    }

    /* Section titles */
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #065911;
    }

    /* Outer chat container */
    [data-testid="stChatInput"] {
        border: 2px solid #065911 !important;
        border-radius: 20px !important;
        box-shadow: 0 4px 12px rgba(16, 97, 15, 0.12) !important;
        transition: all 0.3s ease;
    }

    /* Remove styling from inner containers */
    [data-testid="stChatInput"] > div {
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
    }

    /* Remove textarea border */
    [data-testid="stChatInput"] textarea {
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
    }

    /* Subtle focus effect */
    [data-testid="stChatInput"]:focus-within {
        border-color: #065911 !important;
        box-shadow: 0 2px 8px rgba(16, 97, 15, 0.12) !important;
    }
    
    /* Nice focus effect */
    [data-testid="stChatInput"]:focus-within {
    box-shadow: 0 0 0 4px rgba(16, 97, 15, 0.15) !important;
  }

   /* Chat input buttons */
    [data-testid="stChatInput"] button {
    color: white !important;
    background-color: #065911 !important;
    border: none !important;
}

   /* Button container */
    [data-testid="stChatInput"] button > div {
    background-color: #065911 !important;
}
    </style>
    """,
    unsafe_allow_html=True
)


# HEADER

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    logo_col, title_col = st.columns(
        [1, 3],
        vertical_alignment="center",
    )

    # Logo on the left
    with logo_col:
        st.image("logo.png", width=140)

    # Title on the right
    with title_col:
        st.markdown(
            '<div class="wain-title">WAIN</div>',
            unsafe_allow_html=True
        )


# SUBTITLE

st.markdown(
    '<div class="wain-subtitle">'
    'Your AI Assistant for Exploring Riyadh'
    '</div>',
    unsafe_allow_html=True
)


# INTRO TEXT

st.markdown(
    '<div class="intro-text">'
    '<strong>Find. Choose. Explore.</strong>'
    '</div>',
    unsafe_allow_html=True
)


# CHAT INPUT

user_question = st.chat_input("Looking for somewhere to go? Tell me what you like...")


# PROCESS USER MESSAGE

if user_question:

    with st.chat_message("user"):
        st.markdown(user_question)


    # Run WAIN
    with st.spinner( "WAIN is exploring Riyadh for you...."):

        try:
            result = run_wain(user_question)

            # Save only the structured results
            st.session_state["results"] = result["results"]
            st.session_state["last_question"] = user_question

        except Exception as e:
            st.error("Something went wrong while generating your recommendations. Please try again.")
            st.exception(e)


# DISPLAY RECOMMENDATION CARDS

if "results" in st.session_state:

    results = st.session_state.get(
        "results",
        []
    )

    if results:

        st.markdown(
            '<div class="section-title">'
            'Places You Might Like'
            '</div>',
            unsafe_allow_html=True
        )


        # LOOP THROUGH RECOMMENDATIONS

        for index, place in enumerate(
            results,
            start=1
        ):

            # Extract place information

            place_name = place[1]

            location = (
                place[4]
                if place[4]
                else "Not specified"
            )

            rating = (
                place[5]
                if place[5] is not None
                else "N/A"
            )

            cost = (
                place[6]
                if place[6] is not None
                else "N/A"
            )

            duration = (
                place[8]
                if place[8] is not None
                else "N/A"
            )

            activity_type = (
                place[9]
                if place[9]
                else "Not specified"
            )

            opening_hours = (
                place[10]
                if place[10]
                else "Not specified"
            )


            # RECOMMENDATION CARD

            with st.container(border=True):

                title_col, map_col = st.columns(
                    [3.5, 1.5]
                )

                # Place name
                with title_col:
                    st.subheader(
                        f"{index}. {place_name}"
                    )


                # Google Maps

                query = (
                    f"{place_name}, "
                    f"{location}, "
                    f"Riyadh, Saudi Arabia"
                )

                map_url = (
                    "https://www.google.com/maps/search/?api=1&query="
                    + urllib.parse.quote(query)
                )


                # Maps button
                with map_col:

                    st.link_button(
                        " 🗺️ Open Google Maps",
                        map_url,
                        use_container_width=True
                    )


                # PLACE INFORMATION

                col1, col2 = st.columns(2)

                # Left column
                with col1:
                    st.write(
                        f"📍 **Location:** {location}"
                    )

                    st.write(
                        f"⭐ **Rating:** {rating}"
                    )

                # Right column
                with col2:
                    st.write(
                        f"💰 **Estimated Cost:** "
                        f"{cost} SAR"
                    )

                    st.write(
                        f"⏳ **Duration:** "
                        f"{duration} hours"
                    )

                # Activity
                st.write(
                    f"🎯 **Activity:** "
                    f"{activity_type}"
                )

                # Opening Hours
                st.write(
                    f"⏰ **Opening Hours:** "
                    f"{opening_hours}"
                )

