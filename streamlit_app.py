import streamlit as st
import pandas as pd

# Set up page
st.set_page_config(page_title="GB UK SKU Pricing Intelligence Dashboard", layout="wide")
st.title("🇬🇧 UK SKU Pricing Intelligence Dashboard")

# ---------- Initialise session state ----------
if "uk_sku_df" not in st.session_state:
    st.session_state.uk_sku_df = pd.DataFrame([
        ["ASC1014", 289, 389, 20, 35.22, 0.18, 0.1, 10],
        ["ASC1216", 305, 406, 20, 42.99, 0.20, 1.99, 10],
    ], columns=[
        "SKU", "Length_mm", "Width_mm", "Depth_mm",
        "Export_Cost_ZAR", "Imported_Cost_ZAR",
        "Commission_%", "Markup_%"
    ])

if "uk_history" not in st.session_state:
    st.session_state.uk_history = []

# ---------- Sidebar Settings ----------
st.sidebar.header("UK Settings")
uk_rate = st.sidebar.number_input("Exchange Rate (ZAR → GBP)", value=st.session_state.get("uk_rate", 19.0), key="uk_rate")
uk_vat = st.sidebar.number_input("VAT % (e.g. 20 for 20%)", value=st.session_state.get("uk_vat", 20.0), key="uk_vat") / 100
uk_months = st.sidebar.number_input("Sell-Through Duration (Months)", 1, 24, st.session_state.get("uk_months", 6), key="uk_months")

st.sidebar.header("Monthly Costs")
uk_ads = st.sidebar.number_input("Advertising", value=st.session_state.get("uk_ads", 3000.0), key="uk_ads")
uk_bank = st.sidebar.number_input("Banking", value=st.session_state.get("uk_bank", 2000.0), key="uk_bank")
uk_ops = st.sidebar.number_input("Ops Cost", value=st.session_state.get("uk_ops", 4000.0), key="uk_ops")
uk_ware = st.sidebar.number_input("Warehousing", value=st.session_state.get("uk_ware", 10000.0), key="uk_ware")
uk_pack = st.sidebar.number_input("Packing", value=st.session_state.get("uk_pack", 6000.0), key="uk_pack")
uk_cour = st.sidebar.number_input("Courier", value=st.session_state.get("uk_cour", 7000.0), key="uk_cour")


monthly_total = uk_ads + uk_bank + uk_ops + uk_ware + uk_pack + uk_cour

# ---------- Recalculation Function ----------
def recalc_uk():
    df = st.session_state.uk_sku_df.copy()
    df["Volume_m3"] = (df["Length_mm"] * df["Width_mm"] * df["Depth_mm"]) / 1_000_000_000
    total_volume = df["Volume_m3"].sum()
    monthly_per_m3 = (monthly_total / total_volume) * uk_months

    df["UK_Landed"] = (df["Imported_Cost_ZAR"] / uk_rate) + (df["Volume_m3"] * monthly_per_m3)
    df["RRP_exVAT"] = df["UK_Landed"] * (1 + df["Commission_%"] / 100 + df["Markup_%"] / 100)
    df["RRP_incVAT"] = df["RRP_exVAT"] * (1 + uk_vat)
    df["RRP_exVAT"] = df["RRP_exVAT"].round(2)
    df["RRP_incVAT"] = df["RRP_incVAT"].round(2)
    return df.round(4)


# ---------- Buttons ----------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔁 Recalculate"):
        st.session_state.uk_history.append(st.session_state.uk_sku_df.copy())
        st.session_state.uk_sku_df = recalc_uk()
        st.success("Recalculated based on latest inputs.")

with col2:
    if st.button("💾 Save Changes"):
        st.success("Saved in memory! (Not to CSV)")

with col3:
    if st.button("↩️ Undo") and st.session_state.uk_history:
        st.session_state.uk_sku_df = st.session_state.uk_history.pop()
        st.success("Undone to previous state!")

# ---------- Editor ----------
st.subheader("📊 UK SKU Pricing")
non_editable = ["Volume_m3", "UK_Landed", "RRP_exVAT", "RRP_incVAT"]
for col in non_editable:
    if col not in st.session_state.uk_sku_df.columns:
        st.session_state.uk_sku_df[col] = 0.0

edited = st.data_editor(
    st.session_state.uk_sku_df,
    use_container_width=True,
    num_rows="dynamic",
    disabled=non_editable,
    hide_index=True
)

st.session_state.uk_sku_df.update(edited)
