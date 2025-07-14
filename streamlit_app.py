import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(page_title="🇬🇧 UK SKU Pricing Dashboard", layout="wide")
st.title("🇬🇧 UK SKU Pricing Intelligence Dashboard")

# Sidebar Inputs – UK Only
st.sidebar.header("UK Settings")
exchange_rate = st.sidebar.number_input("Exchange Rate (ZAR → GBP)", value=19.0)
vat_rate = st.sidebar.number_input("VAT %", value=0.20)
duration_months = st.sidebar.number_input("Sell-Through Duration (Months)", min_value=1, max_value=24, value=6)

st.sidebar.header("Monthly Costs")
monthly_costs = {
    "Advertising": st.sidebar.number_input("Advertising", value=3000.0),
    "Banking": st.sidebar.number_input("Banking", value=2000.0),
    "Ops Cost": st.sidebar.number_input("Ops Cost", value=4000.0),
    "Warehousing": st.sidebar.number_input("Warehousing", value=10000.0),
    "Packing": st.sidebar.number_input("Packing", value=6000.0),
    "Courier": st.sidebar.number_input("Courier", value=7000.0),
}
total_monthly_costs = sum(monthly_costs.values())

# Define SKU input columns
base_columns = [
    "SKU", "Length_mm", "Width_mm", "Depth_mm",
    "Export_Cost_ZAR", "Imported_Cost_ZAR", "Commission_%", "Markup_%"
]

# Initial session setup
if "uk_sku_df" not in st.session_state:
    st.session_state.uk_sku_df = pd.DataFrame([
        ["ASC1014", 289, 389, 20, 35.22, 0.18, 0.1, 10],
        ["ASC1216", 305, 406, 20, 42.99, 0.20, 1.99, 10]
    ], columns=base_columns)

if "uk_history" not in st.session_state:
    st.session_state.uk_history = []

# Recalc function
def recalculate_uk():
    df = st.session_state.uk_sku_df.copy()
    df["Volume_m3"] = (df["Length_mm"] * df["Width_mm"] * df["Depth_mm"]) / 1_000_000_000
    cost_load = (total_monthly_costs / df["Volume_m3"].sum()) * df["Volume_m3"] * duration_months
    df["UK_Landed"] = ((df["Export_Cost_ZAR"] + df["Imported_Cost_ZAR"]) / exchange_rate + cost_load).round(3)
    df["RRP_exVAT"] = df["UK_Landed"] * (1 + df["Commission_%"]) * (1 + df["Markup_%"] / 100)
    df["RRP_incVAT"] = df["RRP_exVAT"] * (1 + vat_rate)
    return df

# Display Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("💾 Save Changes"):
        st.session_state.uk_sku_df[base_columns] = st.session_state.uk_edited_df[base_columns]
        st.success("Changes saved to session memory!")

with col2:
    if st.button("🔁 Recalculate"):
        st.session_state.uk_history.append(st.session_state.uk_sku_df.copy())
        st.session_state.uk_edited_df = recalculate_uk()
        st.experimental_rerun()

# Show Table
st.subheader("📊 UK SKU Pricing")
if "uk_edited_df" not in st.session_state:
    st.session_state.uk_edited_df = recalculate_uk()

edited_df = st.data_editor(
    st.session_state.uk_edited_df,
    use_container_width=True,
    num_rows="dynamic",
    hide_index=True,
    disabled=["Volume_m3", "UK_Landed", "RRP_exVAT", "RRP_incVAT"]
)

# Update preview live while editing
st.session_state.uk_edited_df = edited_df
