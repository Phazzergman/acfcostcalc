import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="ACF SKU Pricing Intelligence Dashboard", layout="wide")

# Session state initialization
if "df_backup" not in st.session_state:
    st.session_state.df_backup = None

# Sidebar - Toggle Countries and Global Settings
st.sidebar.title("Toggle Countries")
country_selected = st.sidebar.checkbox("UK", value=True)
st.sidebar.markdown("---")

sell_through_months = st.sidebar.number_input("Sell-Through Duration (Months)", min_value=1, value=6)

# UK Settings
st.sidebar.subheader("UK Settings")
st.session_state.uk_exchange_rate = st.sidebar.number_input("UK Exchange Rate (ZAR ➔ Local)", value=19.0)
st.session_state.uk_vat = st.sidebar.number_input("UK VAT %", value=0.20)
uk_container_cost = st.sidebar.number_input("UK Container Cost (ZAR)", value=150000.0)
uk_container_volume = st.sidebar.number_input("UK Container Volume (m³)", value=95.25)

# Monthly Costs
st.session_state.uk_advertising = st.sidebar.number_input("UK Advertising (Monthly)", value=3000.0)
st.session_state.uk_banking = st.sidebar.number_input("UK Banking (Monthly)", value=2000.0)
st.session_state.uk_ops = st.sidebar.number_input("UK Ops Cost (Monthly)", value=4000.0)
st.session_state.uk_warehousing = st.sidebar.number_input("UK Warehousing (Monthly)", value=10000.0)
st.session_state.uk_packing = st.sidebar.number_input("UK Packing (Monthly)", value=6000.0)
st.session_state.uk_courier = st.sidebar.number_input("UK Courier (Monthly)", value=7000.0)

# Initialize Data
data = {
    "SKU": ["ASC608", "ASC1012", "ASC1014", "ASC1216", "ASC1418", "ASC1620", "ASC1824", "ASC2024", "ASC2430"],
    "Length_mm": [200, 255, 255, 305, 355, 406, 457, 501, 610],
    "Width_mm": [1000, 305, 355, 406, 457, 501, 610, 610, 762],
    "Depth_mm": [1000, 20, 20, 20, 20, 20, 20, 20, 20],
    "Factory_Cost_ZAR": [16.79, 31.86, 35.22, 42.99, 53.51, 62.34, 73.2, 78.14, 99.56],
    "Export_Cost_ZAR": [255, 355, 402, 495, 621, 749, 940, 1009, 1284],
    "Commission_%": [33] * 9,
    "Volume_m³": [0.2, 0.0016, 0.0018, 0.0025, 0.0032, 0.0041, 0.0056, 0.0061, 0.0093],
}

df = pd.DataFrame(data)

# Button interactions
col1, col2, col3 = st.columns([1, 1, 1])
recalculate = col1.button("Recalculate")
save = col2.button("Save Changes")
undo = col3.button("Undo")

# Backup before recalculation
if recalculate:
    st.session_state.df_backup = df.copy()

    # Constants
    exchange_rate = st.session_state.uk_exchange_rate
    vat_rate = st.session_state.uk_vat
    commission_rate = 0.33
    markup_rate = 0.50
    monthly_costs = (
        st.session_state.uk_advertising +
        st.session_state.uk_banking +
        st.session_state.uk_ops +
        st.session_state.uk_warehousing +
        st.session_state.uk_packing +
        st.session_state.uk_courier
    )
    monthly_cost_per_m3 = monthly_costs / sell_through_months

    # Calculations
    for i, row in df.iterrows():
        volume_m3 = row["Volume_m³"]
        export_cost_zar = row["Export_Cost_ZAR"]
        export_cost_gbp = export_cost_zar / exchange_rate
        cost_with_commission = export_cost_gbp * (1 + commission_rate)
        operational_cost = monthly_cost_per_m3 * volume_m3
        landed_total_cost = cost_with_commission + operational_cost
        rrp_ex_vat = landed_total_cost * (1 + markup_rate)
        rrp_incl_vat = rrp_ex_vat * (1 + vat_rate)

        df.at[i, "UK Landed"] = round(landed_total_cost, 2)
        df.at[i, "UK RRP exVAT"] = round(rrp_ex_vat, 2)
        df.at[i, "UK RRP incVAT"] = round(rrp_incl_vat, 2)

# Undo changes
if undo and st.session_state.df_backup is not None:
    df = st.session_state.df_backup.copy()

# Display table
st.title("📦 ACF SKU Pricing Intelligence Dashboard")
st.dataframe(df, use_container_width=True)
