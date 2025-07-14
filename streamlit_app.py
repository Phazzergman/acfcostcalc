import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="🇬🇧 UK SKU Pricing View", layout="wide")
st.title("🇬🇧 UK SKU Pricing Intelligence Dashboard")

# ---- Editable base data for UK ----
columns = [
    "SKU", "Length_mm", "Width_mm", "Depth_mm",
    "Export_Cost_ZAR", "Imported_Cost_ZAR", "Commission_%", "Markup_%"
]

# Session-persisted DataFrame
if "uk_sku_df" not in st.session_state:
    st.session_state.uk_sku_df = pd.DataFrame([
        ["ASC1014", 289, 389, 20, 35.22, 0.18, 0.10, 10.0],
        ["ASC1216", 305, 406, 20, 42.99, 0.20, 1.99, 10.0],
    ], columns=columns)

# Sidebar inputs
st.sidebar.header("UK Settings")
exchange_rate = st.sidebar.number_input("Exchange Rate (ZAR → GBP)", value=19.0)
vat_percent = st.sidebar.number_input("VAT %", value=0.20)
duration_months = st.sidebar.number_input("Sell-Through Duration (Months)", min_value=1, max_value=24, value=6)

st.sidebar.markdown("---")
st.sidebar.subheader("Monthly Costs")
ads = st.sidebar.number_input("Advertising", value=3000.0)
bank = st.sidebar.number_input("Banking", value=2000.0)
ops = st.sidebar.number_input("Ops Cost", value=4000.0)
ware = st.sidebar.number_input("Warehousing", value=10000.0)
pack = st.sidebar.number_input("Packing", value=6000.0)
cour = st.sidebar.number_input("Courier", value=7000.0)

# Total monthly cost
total_monthly_cost = ads + bank + ops + ware + pack + cour

# Editable SKU table
editable_df = st.data_editor(
    st.session_state.uk_sku_df,
    use_container_width=True,
    num_rows="dynamic",
    hide_index=True
)

# Calculate volume
editable_df["Volume_m3"] = (
    editable_df["Length_mm"] * editable_df["Width_mm"] * editable_df["Depth_mm"] / 1_000_000_000
)

# Monthly cost allocation by volume share
total_volume = editable_df["Volume_m3"].sum()
editable_df["Allocated_Monthly_Cost"] = (
    editable_df["Volume_m3"] / total_volume * total_monthly_cost * duration_months
)

# UK Landed (imported cost + commission + allocated cost)
editable_df["UK_Landed"] = (
    (editable_df["Imported_Cost_ZAR"] / exchange_rate) +
    editable_df["Commission_%"] +
    editable_df["Allocated_Monthly_Cost"]
)

# RRP Calculations
editable_df["RRP_exVAT"] = editable_df["UK_Landed"] * (1 + editable_df["Markup_%"] / 100)
editable_df["RRP_incVAT"] = editable_df["RRP_exVAT"] * (1 + vat_percent)

# Display final results
st.subheader("💷 UK SKU Pricing")
st.dataframe(
    editable_df[[
        "SKU", "Length_mm", "Width_mm", "Depth_mm", "Export_Cost_ZAR", "Imported_Cost_ZAR",
        "Commission_%", "Markup_%", "Volume_m3", "UK_Landed", "RRP_exVAT", "RRP_incVAT"
    ]].round(4),
    use_container_width=True
)

# Save back to session state
st.session_state.uk_sku_df = editable_df
