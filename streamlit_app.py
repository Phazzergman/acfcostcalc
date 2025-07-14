import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="ACF SKU Pricing Intelligence Dashboard", layout="wide")

# Session state initialization
if "df_backup" not in st.session_state:
    st.session_state.df_backup = None

# Sidebar - Global UK Settings
st.sidebar.title("UK Settings")
st.session_state.uk_exchange_rate = st.sidebar.number_input("Exchange Rate (ZAR ➝ GBP)", value=19.0)
st.session_state.uk_vat = st.sidebar.number_input("VAT %", value=20.0) / 100
st.session_state.uk_commission = st.sidebar.number_input("Commission %", value=33.0) / 100
st.session_state.uk_markup = st.sidebar.number_input("Markup %", value=50.0) / 100

# Initialize Data
data = {
    "SKU": ["ASC608", "ASC1012", "ASC1014", "ASC1216", "ASC1418", "ASC1620", "ASC1824", "ASC2024", "ASC2430"],
    "Factory_Cost_ZAR": [16.79, 31.86, 35.22, 42.99, 53.51, 62.34, 73.2, 78.14, 99.56],
    "Export_Cost_ZAR": [255, 355, 402, 495, 621, 749, 940, 1009, 1284],
}

df = pd.DataFrame(data)

# Buttons
col1, col2, col3 = st.columns([1, 1, 1])
recalculate = col1.button("Recalculate")
save = col2.button("Save Changes")
undo = col3.button("Undo")

# Backup before recalculation
if recalculate:
    st.session_state.df_backup = df.copy()

    exchange_rate = st.session_state.uk_exchange_rate
    vat_rate = st.session_state.uk_vat
    commission_rate = st.session_state.uk_commission
    markup_rate = st.session_state.uk_markup

    for i, row in df.iterrows():
        cost_gbp = row["Export_Cost_ZAR"] / exchange_rate
        cost_with_commission = cost_gbp * (1 + commission_rate)
        rrp_ex_vat = cost_with_commission * (1 + markup_rate)
        rrp_inc_vat = rrp_ex_vat * (1 + vat_rate)
        profit = rrp_inc_vat - cost_with_commission

        df.at[i, "UK Landed"] = round(cost_with_commission, 2)
        df.at[i, "UK RRP exVAT"] = round(rrp_ex_vat, 2)
        df.at[i, "UK RRP incVAT"] = round(rrp_inc_vat, 2)
        df.at[i, "Profit per Unit"] = round(profit, 2)

# Undo changes
if undo and st.session_state.df_backup is not None:
    df = st.session_state.df_backup.copy()

# Display table
st.title("📦 ACF SKU Pricing Intelligence Dashboard")
st.dataframe(df, use_container_width=True)
