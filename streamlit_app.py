import streamlit as st
import pandas as pd

st.set_page_config(page_title="ACF UK Pricing Estimator", layout="wide")

st.title("ACF UK Pricing & Profitability Estimator")

# Sidebar Inputs
st.sidebar.header("Global Inputs")

exchange_rate = st.sidebar.number_input("Exchange Rate (ZAR to GBP)", value=1.20)
commission_percent = st.sidebar.number_input("Commission % (UK entity)", value=20.0)
markup_percent = st.sidebar.number_input("Markup %", value=50.0)
vat_percent = st.sidebar.number_input("VAT %", value=20.0)

# Buttons
col1, col2, col3 = st.columns([1, 1, 1])
recalculate = col1.button("Recalculate")
save = col2.button("Save Changes")
undo = col3.button("Undo")

# Simulated SKU input table (replace with your own table logic)
st.subheader("Container SKUs and Costs")

data = {
    "SKU": ["ABC123", "DEF456", "GHI789"],
    "Length_mm": [200, 300, 400],
    "Width_mm": [300, 400, 500],
    "Depth_mm": [20, 20, 20],
    "Factory Cost (£)": [3.50, 4.00, 4.50],
    "Shipping (£)": [0.67, 0.85, 1.00],
}

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(data)

if "df_backup" not in st.session_state:
    st.session_state.df_backup = None

# Local working df
df = st.session_state.df.copy()

# Recalculate logic
if recalculate:
    st.session_state.df_backup = df.copy()

    df["Volume_m³"] = (df["Length_mm"] * df["Width_mm"] * df["Depth_mm"]) / 1e9
    df["Landed Cost (£)"] = df["Factory Cost (£)"] + df["Shipping (£)"]
    df["Commission (£)"] = df["Landed Cost (£)"] * (commission_percent / 100)
    df["Post-Commission (£)"] = df["Landed Cost (£)"] + df["Commission (£)"]
    df["Pre-VAT Price (£)"] = df["Post-Commission (£)"] * (1 + markup_percent / 100)
    df["VAT (£)"] = df["Pre-VAT Price (£)"] * (vat_percent / 100)
    df["RRP incl VAT (£)"] = df["Pre-VAT Price (£)"] + df["VAT (£)"]
    df["Profit per Unit (£)"] = df["RRP incl VAT (£)"] - df["Post-Commission (£)"]

    st.session_state.df = df.copy()

# Undo logic
if undo and st.session_state.df_backup is not None:
    st.session_state.df = st.session_state.df_backup.copy()

# Reload for display
df = st.session_state.df.copy()

# Display table
st.markdown("### 📦 SKU Pricing Table")
st.dataframe(df.style.format({
    "Factory Cost (£)": "£{:.2f}",
    "Shipping (£)": "£{:.2f}",
    "Landed Cost (£)": "£{:.2f}",
    "Commission (£)": "£{:.2f}",
    "Post-Commission (£)": "£{:.2f}",
    "Pre-VAT Price (£)": "£{:.2f}",
    "VAT (£)": "£{:.2f}",
    "RRP incl VAT (£)": "£{:.2f}",
    "Profit per Unit (£)": "£{:.2f}",
    "Volume_m³": "{:.6f}",
}), use_container_width=True)

# Summary
st.markdown("### 🧾 Summary")
if "Profit per Unit (£)" in df.columns:
    total_profit = df["Profit per Unit (£)"].sum()
    avg_profit = df["Profit per Unit (£)"].mean()
    st.success(f"Average Profit per SKU: £{avg_profit:.2f}")
    st.info(f"Total Combined Profit: £{total_profit:.2f}")
else:
    st.warning("Please click 'Recalculate' to generate pricing data.")
