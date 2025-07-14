import streamlit as st
import pandas as pd

# Set up page
st.set_page_config(page_title="GB UK SKU Pricing Intelligence Dashboard", layout="wide")
st.title("🇬🇧 UK SKU Pricing Intelligence Dashboard")

# ---------- Initialise session state ----------
default_data = pd.DataFrame([
    ["ASC1014", 289, 389, 20, 35.22, 100, 10, 10],
    ["ASC1216", 305, 406, 20, 42.99, 120, 1.99, 10],
], columns=[
    "SKU", "Length_mm", "Width_mm", "Depth_mm",
    "Export_Cost_ZAR", "Imported_Cost_ZAR",
    "Commission_%", "Markup_%"
])

if "uk_sku_df" not in st.session_state:
    st.session_state.uk_sku_df = default_data.copy()
elif st.session_state.uk_sku_df.empty:
    st.session_state.uk_sku_df = default_data.copy()

if "uk_history" not in st.session_state:
    st.session_state.uk_history = []

# ---------- Sidebar Settings ----------
st.sidebar.header("UK Settings")
st.sidebar.number_input("Exchange Rate (ZAR → GBP)", key="uk_rate", value=19.0)
st.sidebar.number_input("VAT % (e.g. 20 for 20%)", key="uk_vat", value=20.0)
st.sidebar.number_input("Sell-Through Duration (Months)", 1, 24, key="uk_months", value=6)

st.sidebar.header("Monthly Costs")
st.sidebar.number_input("Advertising", key="uk_ads", value=3000.0)
st.sidebar.number_input("Banking", key="uk_bank", value=2000.0)
st.sidebar.number_input("Ops Cost", key="uk_ops", value=4000.0)
st.sidebar.number_input("Warehousing", key="uk_ware", value=10000.0)
st.sidebar.number_input("Packing", key="uk_pack", value=6000.0)
st.sidebar.number_input("Courier", key="uk_cour", value=7000.0)

# 👉 Use from session
uk_rate = st.session_state.uk_rate
uk_vat = st.session_state.uk_vat / 100
uk_months = st.session_state.uk_months

uk_ads = st.session_state.uk_ads
uk_bank = st.session_state.uk_bank
uk_ops = st.session_state.uk_ops
uk_ware = st.session_state.uk_ware
uk_pack = st.session_state.uk_pack
uk_cour = st.session_state.uk_cour

# ---------- Recalculation Function ----------
def recalc_uk():
    df = st.session_state.uk_sku_df.copy()
    df["Volume_m3"] = (df["Length_mm"] * df["Width_mm"] * df["Depth_mm"]) / 1_000_000_000
    total_volume = df["Volume_m3"].sum()

    if total_volume == 0 or pd.isna(total_volume):
        st.error("Total volume is zero or invalid. Please check dimensions.")
        return df

    monthly_total = uk_ads + uk_bank + uk_ops + uk_ware + uk_pack + uk_cour
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

# Debug
st.write("✅ DEBUG: SKU Table", st.session_state.uk_sku_df)

edited = st.data_editor(
    st.session_state.uk_sku_df,
    use_container_width=True,
    num_rows="dynamic",
    disabled=non_editable,
    hide_index=True
)

if not edited.empty:
    st.session_state.uk_sku_df.update(edited)
