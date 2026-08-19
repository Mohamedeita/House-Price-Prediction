import streamlit as st
import pandas as pd
import joblib


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("house_price_model.pkl")


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* =====================================================
   BACKGROUND
   ===================================================== */

.stApp {

    background-image:

        linear-gradient(
            rgba(5, 10, 20, 0.82),
            rgba(5, 10, 20, 0.90)
        ),

        url(house_background.jpg);

    background-size: cover;

    background-position: center;

    background-attachment: fixed;

    min-height: 100vh;
}


/* =====================================================
   HIDE STREAMLIT UI
   ===================================================== */

/* Hide footer */

footer {
    visibility: hidden;
}


/* Hide top menu */

#MainMenu {
    visibility: hidden;
}


/* Hide header */

header {
    visibility: hidden;
}


/* Hide deploy button */

[data-testid="stDeployButton"] {
    display: none;
}


/* Hide toolbar */

[data-testid="stToolbar"] {
    visibility: hidden;
}


/* Hide decoration */

[data-testid="stDecoration"] {
    display: none;
}


/* =====================================================
   MAIN CONTAINER
   ===================================================== */

.block-container {

    max-width: 1200px;

    padding-top: 3rem;

    padding-bottom: 3rem;
}


/* =====================================================
   TITLE
   ===================================================== */

h1 {

    color: #f8fafc !important;

    font-size: 46px !important;

    font-weight: 750 !important;

    letter-spacing: -1px;

    margin-bottom: 5px;
}


/* =====================================================
   SECTION TITLES
   ===================================================== */

h2 {

    color: #f1f5f9 !important;

    font-size: 24px !important;

    font-weight: 650 !important;

    margin-top: 30px;
}


/* =====================================================
   TEXT
   ===================================================== */

p {

    color: #cbd5e1;

}


/* =====================================================
   INPUT LABELS
   ===================================================== */

label {

    color: #cbd5e1 !important;

    font-weight: 500 !important;
}


/* =====================================================
   SELECT BOX
   ===================================================== */

div[data-baseweb="select"] > div {

    background-color: rgba(15, 23, 42, 0.92) !important;

    border: 1px solid rgba(148, 163, 184, 0.25) !important;

    border-radius: 10px !important;
}


/* Select text */

div[data-baseweb="select"] span {

    color: #f8fafc !important;
}


/* =====================================================
   NUMBER INPUT
   ===================================================== */

div[data-testid="stNumberInput"] input {

    background-color: rgba(15, 23, 42, 0.92) !important;

    color: #f8fafc !important;

    border: 1px solid rgba(148, 163, 184, 0.25) !important;

    border-radius: 10px !important;
}


/* =====================================================
   INPUT FOCUS
   ===================================================== */

div[data-baseweb="select"] > div:focus-within {

    border-color: #38bdf8 !important;

    box-shadow:
        0 0 0 1px #38bdf8 !important;
}


/* =====================================================
   PREDICTION BUTTON
   ===================================================== */

.stButton {

    margin-top: 30px;
}


.stButton > button {

    width: 100%;

    height: 58px;

    border-radius: 14px;

    border: none;

    background:

        linear-gradient(
            135deg,
            #2563eb,
            #0891b2
        );

    color: white;

    font-size: 18px;

    font-weight: 650;

    transition: all 0.25s ease;
}


.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:

        0 12px 30px
        rgba(37, 99, 235, 0.30);
}


/* =====================================================
   SUCCESS MESSAGE
   ===================================================== */

div[data-testid="stAlert"] {

    border-radius: 12px;

    background-color:
        rgba(16, 185, 129, 0.12);
}


/* =====================================================
   PRICE CARD
   ===================================================== */

div[data-testid="stMetric"] {

    background:

        rgba(15, 23, 42, 0.92);

    border:

        1px solid
        rgba(56, 189, 248, 0.25);

    border-radius: 18px;

    padding: 25px;

    margin-top: 20px;

    box-shadow:

        0 15px 35px
        rgba(0, 0, 0, 0.25);
}


/* Price label */

div[data-testid="stMetricLabel"] {

    color: #94a3b8 !important;
}


/* Price value */

div[data-testid="stMetricValue"] {

    color: #f8fafc !important;

    font-size: 38px !important;

    font-weight: 750 !important;
}


/* =====================================================
   DIVIDER
   ===================================================== */

hr {

    border-color:
        rgba(148, 163, 184, 0.18) !important;

    margin-top: 45px;

}


/* =====================================================
   LINK BUTTON
   ===================================================== */

.stLinkButton > a {

    border-radius: 10px !important;

    background:
        rgba(30, 41, 59, 0.90) !important;

    border:
        1px solid
        rgba(148, 163, 184, 0.20) !important;

    color: #e2e8f0 !important;

    font-weight: 600 !important;

}


.stLinkButton > a:hover {

    border-color: #38bdf8 !important;

    color: #38bdf8 !important;

}


/* =====================================================
   FOOTER TEXT
   ===================================================== */

[data-testid="stCaptionContainer"] p {

    color: #64748b !important;

}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HEADER
# =====================================================

st.title("House Price Prediction")

st.write(
    "Machine Learning powered house price estimation."
)

st.caption(
    "Enter the property details below to generate a prediction."
)


# =====================================================
# PROPERTY INFORMATION
# =====================================================

st.header("Property Information")


col1, col2, col3 = st.columns(3)


# =====================================================
# COLUMN 1
# =====================================================

with col1:

    location = st.selectbox(
        "Location",
        [
            "new-delhi",
            "bangalore",
            "kolkata",
            "gurgaon",
            "ahmedabad"
        ]
    )


    status = st.selectbox(
        "Property Status",
        [
            "Ready to Move",
            "Under Construction"
        ]
    )


    transaction = st.selectbox(
        "Transaction",
        [
            "Resale",
            "New Property"
        ]
    )


# =====================================================
# COLUMN 2
# =====================================================

with col2:

    furnishing = st.selectbox(
        "Furnishing",
        [
            "Semi-Furnished",
            "Unfurnished",
            "Furnished"
        ]
    )


    facing = st.selectbox(
        "Facing",
        [
            "North",
            "South",
            "East",
            "West"
        ]
    )


    ownership = st.selectbox(
        "Ownership",
        [
            "Freehold",
            "Leasehold"
        ]
    )


# =====================================================
# COLUMN 3
# =====================================================

with col3:

    bathroom = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=20,
        value=2
    )


    balcony = st.number_input(
        "Balcony",
        min_value=0,
        max_value=10,
        value=1
    )


    carpet_area = st.number_input(
        "Carpet Area (sqft)",
        min_value=100.0,
        value=1000.0,
        step=50.0
    )


# =====================================================
# PROPERTY DETAILS
# =====================================================

st.header("Property Details")


col1, col2, col3 = st.columns(3)


# =====================================================
# COLUMN 1
# =====================================================

with col1:

    super_area = st.number_input(
        "Super Area (sqft)",
        min_value=100.0,
        value=1200.0,
        step=50.0
    )


    car_parking = st.number_input(
        "Car Parking",
        min_value=0,
        max_value=10,
        value=1
    )


# =====================================================
# COLUMN 2
# =====================================================

with col2:

    current_floor = st.number_input(
        "Current Floor",
        min_value=0,
        max_value=100,
        value=2
    )


    total_floors = st.number_input(
        "Total Floors",
        min_value=1,
        max_value=100,
        value=5
    )


# =====================================================
# COLUMN 3
# =====================================================

with col3:

    has_main_road = st.selectbox(
        "Main Road",
        [0, 1]
    )


    has_garden_park = st.selectbox(
        "Garden / Park",
        [0, 1]
    )


    has_pool = st.selectbox(
        "Swimming Pool",
        [0, 1]
    )


# =====================================================
# ADDITIONAL INFORMATION
# =====================================================

st.header("Additional Information")


society_frequency = st.number_input(
    "Society Frequency",
    min_value=0.0,
    value=1.0,
    step=1.0
)


# =====================================================
# PREDICTION
# =====================================================

if st.button(
    "Predict House Price",
    use_container_width=True
):


    # Create input DataFrame

    input_data = pd.DataFrame({

        "location": [location],

        "Status": [status],

        "Transaction": [transaction],

        "Furnishing": [furnishing],

        "facing": [facing],

        "Ownership": [ownership],

        "Bathroom": [bathroom],

        "Balcony": [balcony],

        "Carpet_Area_sqft": [carpet_area],

        "Super_Area_sqft": [super_area],

        "Car_Parking_Count": [car_parking],

        "Current_Floor": [current_floor],

        "Total_Floors": [total_floors],

        "Has_Main_Road": [has_main_road],

        "Has_Garden_Park": [has_garden_park],

        "Has_Pool": [has_pool],

        "Society_Frequency": [society_frequency]
    })


    # =================================================
    # MODEL PREDICTION
    # =================================================

    prediction_inr = model.predict(
        input_data
    )[0]


    # =================================================
    # INR TO USD
    # =================================================

    exchange_rate = 90

    prediction_usd = (
        prediction_inr / exchange_rate
    )


    # =================================================
    # RESULT
    # =================================================

    st.success(
        "Prediction completed successfully!"
    )


    st.metric(
        label="Estimated House Price",
        value=f"$ {prediction_usd:,.0f}"
    )


# =====================================================
# FOOTER
# =====================================================

st.divider()


st.caption(
    "House Price Prediction • Machine Learning Project"
)


st.write(
    "Created by Mohamed Eita"
)


st.link_button(
    "LinkedIn Profile",
    "https://www.linkedin.com/in/mohamed-eita-581187371"
)