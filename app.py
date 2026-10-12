import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Food Safety Prediction",
    page_icon="🍱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
#q ==========================================

st.markdown("""
<style>

    .main {
        background-color: #f5f9fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .header-box {
        background: linear-gradient(135deg, #0f6b78, #168c9b);
        padding: 28px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 5px 18px rgba(0,0,0,0.10);
    }

    .header-box h1 {
        color: white;
        margin-bottom: 8px;
        font-size: 34px;
    }

    .header-box p {
        color: #e9f8fa;
        font-size: 16px;
        margin-bottom: 0;
    }

    .section-title {
        color: #0f6b78;
        font-size: 22px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .info-card {
        background-color: white;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #e1edf0;
        box-shadow: 0 3px 12px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }

    .result-card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #dcecef;
        box-shadow: 0 5px 18px rgba(0,0,0,0.08);
        text-align: center;
        margin-top: 25px;
    }

    .approved {
        color: #16803c;
        font-size: 30px;
        font-weight: 700;
    }

    .rejected {
        color: #d93025;
        font-size: 30px;
        font-weight: 700;
    }

    div.stButton > button {
        width: 100%;
        background-color: #0f6b78;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 17px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #168c9b;
        color: white;
    }

    [data-testid="stMetric"] {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #e1edf0;
    }

</style>
""", unsafe_allow_html=True)


# ==========================================
# LOAD MODEL
# ==========================================

with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("## 🍱 Food Safety")

    st.markdown("---")

    st.markdown("### 📌 About")

    st.write(
        "This application uses a Machine Learning model "
        "to predict whether a food product is likely to be "
        "Approved or Rejected based on its safety and quality "
        "parameters."
    )

    st.markdown("---")

    st.markdown("### 📊 Prediction Factors")

    st.write("• Product & Packaging Type")
    st.write("• Shelf Life")
    st.write("• Storage Conditions")
    st.write("• Moisture & Preservative Level")
    st.write("• pH Level")
    st.write("• Inspection Score")
    st.write("• Customer Rating")

    st.markdown("---")

    st.caption("Powered by Machine Learning")


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="header-box">

<h1>🍱 Food Safety Product Approval</h1>

<p>
Machine Learning Based Food Product Safety & Approval Prediction System
</p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# INPUT SECTION
# ==========================================

st.markdown(
    '<div class="section-title">📋 Enter Product Details</div>',
    unsafe_allow_html=True
)

st.info(
    "Enter the product and quality details below. "
    "The trained Machine Learning model will predict the approval status."
)


# ==========================================
# INPUTS - ROW 1
# ==========================================

col1, col2 = st.columns(2)

with col1:

    product_type = st.selectbox(
        "Product Type",
        [
            "Frozen Food",
            "Canned Food",
            "Snacks",
            "Dairy",
            "Beverages"
        ]
    )

with col2:

    packaging_type = st.selectbox(
        "Packaging Type",
        [
            "Paper",
            "Vacuum Pack",
            "Metal",
            "Plastic",
            "Glass"
        ]
    )


# ==========================================
# INPUTS - ROW 2
# ==========================================

col1, col2 = st.columns(2)

with col1:

    shelf_life_days = st.number_input(
        "Shelf Life (Days)",
        min_value=1,
        max_value=1000,
        value=100
    )

with col2:

    storage_temperature_C = st.number_input(
        "Storage Temperature (°C)",
        value=5.0
    )


# ==========================================
# INPUTS - ROW 3
# ==========================================

col1, col2 = st.columns(2)

with col1:

    humidity_level_percent = st.number_input(
        "Humidity Level (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

with col2:

    moisture_content = st.number_input(
        "Moisture Content",
        min_value=0.0,
        value=10.0
    )


# ==========================================
# INPUTS - ROW 4
# ==========================================

col1, col2 = st.columns(2)

with col1:

    preservative_level = st.number_input(
        "Preservative Level",
        min_value=0.0,
        value=5.0
    )

with col2:

    pH_level = st.number_input(
        "pH Level",
        min_value=0.0,
        max_value=14.0,
        value=7.0
    )


# ==========================================
# INPUTS - ROW 5
# ==========================================

col1, col2 = st.columns(2)

with col1:

    inspection_score = st.number_input(
        "Inspection Score (0-100)",
        min_value=0,
        max_value=100,
        value=75
    )

with col2:

    customer_rating = st.number_input(
        "Customer Rating (1-5)",
        min_value=1,
        max_value=5,
        value=4
    )


# ==========================================
# PREDICTION BUTTON
# ==========================================

st.markdown("")

predict_button = st.button(
    "🔍 Predict Product Approval"
)


# ==========================================
# PREDICTION
# ==========================================

if predict_button:

    input_data = pd.DataFrame({
        "product_type": [product_type],
        "packaging_type": [packaging_type],
        "shelf_life_days": [shelf_life_days],
        "storage_temperature_C": [storage_temperature_C],
        "humidity_level_percent": [humidity_level_percent],
        "moisture_content": [moisture_content],
        "preservative_level": [preservative_level],
        "pH_level": [pH_level],
        "inspection_score_0_100": [inspection_score],
        "customer_rating_1_5": [customer_rating]
    })

    # ======================================
    # PREDICTION
    # ======================================

    prediction = model.predict(input_data)[0]

    # ======================================
    # PROBABILITY
    # ======================================

    probability = model.predict_proba(input_data)[0]

    max_probability = max(probability)


    # ======================================
    # RESULT
    # ======================================

    st.markdown(
        '<div class="section-title">📊 Prediction Result</div>',
        unsafe_allow_html=True
    )

    if prediction == "Approved":

        st.success("✅ Product Approved")
        st.write("The Product is predicted to meet the" "required approval criteria")
    else:
            st.error("Product Rejected")
            st.write("The Product is predicted not to meet the" "required approval criteria")    
        
           


    # ======================================
    # METRICS
    # ======================================

    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Prediction",
            prediction
        )

    with col2:

        st.metric(
            "Confidence",
            f"{max_probability * 100:.2f}%"
        )

    with col3:

        st.metric(
            "Inspection Score",
            f"{inspection_score}/100"
        )


    # ======================================
    # CONFIDENCE BAR
    # ======================================

    st.markdown("### 🎯 Prediction Confidence")

    st.progress(float(max_probability))

    st.caption(
        f"Model confidence: {max_probability * 100:.2f}%"
    )


    # ======================================
    # INPUT SUMMARY
    # ======================================

    st.markdown("### 📋 Product Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:

        st.write(f"**Product Type:** {product_type}")
        st.write(f"**Packaging:** {packaging_type}")
        st.write(f"**Shelf Life:** {shelf_life_days} days")
        st.write(f"**Temperature:** {storage_temperature_C} °C")
        st.write(f"**Humidity:** {humidity_level_percent} %")

    with summary_col2:

        st.write(f"**Moisture:** {moisture_content}")
        st.write(f"**Preservative:** {preservative_level}")
        st.write(f"**pH Level:** {pH_level}")
        st.write(f"**Customer Rating:** {customer_rating}/5")
        st.write(f"**Inspection Score:** {inspection_score}/100")