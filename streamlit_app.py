import streamlit as st
import pandas as pd
import copy

st.set_page_config(layout="wide")

st.title("GB UK SKU Pricing Intelligence Dashboard")

# --- SIDEBAR SETTINGS ---
st.sidebar.header("UK Settings")
exchange_rate = st.sidebar.number_input("Exchange Rate (ZAR → GBP)", value=24.00)
vat_pct = st.sidebar.number_input("VAT %", value=0.00) / 100
sell_through_months = st.sidebar.number_input("Sell-Through Duration (Months)", value=6)

st.sidebar.header("Monthly Costs")
monthly_costs = {
    "Advertising": st.sidebar.number_input("Advertising", value=0.00),
    "Banking": st.sidebar.number_input("Banking", value=0.00),
    "Ops Cost": st.sidebar.number_input("Ops Cost", value=0.00),
    "Warehousing": st.sidebar.number_input("Warehousing", value=0.00),
    "Packing": st.sidebar.number_input("Packing", value=0.00),
    "Courier": st.sidebar.number_input("Courier", value=0.00),
}

# --- INITIAL DATA ---
initial_data = pd.DataFrame([
    {
        "SKU": "ASC1014",
        "Length_mm": 289,
        "Width_mm": 389,
        "Depth_mm": 20,
        "Export_Cost_ZAR": 100.00,
        "Imported_Cost_ZAR": 120.00,
        "Commission_%": 0.10,
        "Markup_%": 1.00,
        "Volume_m3": 0.0022,
    },
    {
        "SKU": "ASC1216",
        "Length_mm": 305,
        "Width_mm": 406,
        "Depth_mm": 20,
        "Export_Cost_ZAR": 42.99,
        "Imported_Cost_ZAR": 0.00,
        "Commission_%": 0.20,
        "Markup_%": 10.00,
        "Volume_m3": 0.0025,
    }
])

# --- SESSION STATE ---
if "data" not in st.session_state:
    st.session_state["data"] = initial_data.copy()
    st.session_state["backup"] = copy.deepcopy(initial_data)

# --- BUTTONS ---
col1, col2, col3 = st.columns([2, 1, 1])
if col2.button("Save Changes"):
    st.session_state["backup"] = st.session_state["data"].copy()

if col3.button("Undo"):
    st.session_state["data"] = st.session_state["backup"].copy()

# --- RECALCULATE ---
if col1.button("Recalculate"):
    df = st.session_state["data"]

    # Correct exchange logic: GBP = ZAR * (1 / exchange_rate)
    gbp_per_zar = 1 / exchange_rate
    df["UK_Landed"] = df["Export_Cost_ZAR"] * gbp_per_zar

    # Commission (in GBP)
    df["Commission_GBP"] = df["UK_Landed"] * df["Commission_%"]

    # Retail ex VAT
    df["RRP_exVAT"] = (df["UK_Landed"] + df["Commission_GBP"]) * (1 + df["Markup_%"])

    # Retail incl VAT
    df["RRP_incVAT"] = df["RRP_exVAT"] * (1 + vat_pct)

    # Optional: Round values for display
    df[["UK_Landed", "Commission_GBP", "RRP_exVAT", "RRP_incVAT"]] = df[
        ["UK_Landed", "Commission_GBP", "RRP_exVAT", "RRP_incVAT"]
    ].round(4)

    st.session_state["data"] = df
    st.success("Recalculated based on latest inputs.")

# --- DISPLAY TABLE ---
st.subheader("📊 UK SKU Pricing")
edited_df = st.data_editor(
    st.session_state["data"],
    num_rows="dynamic",
    use_container_width=True
)

st.session_state["data"] = edited_df
