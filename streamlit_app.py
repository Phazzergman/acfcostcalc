import streamlit as st
import pandas as pd

st.set_page_config(page_title="ACF Master Price Calculator", layout="centered")
st.title("🎯 ACF Canvas SKU Pricing Tool")

st.markdown("""
Use this tool to simulate **country-specific pricing**, based on:
- SKU volume in **m³**
- Monthly costs (ads, fulfilment, banking, etc.)
- Manual RRP suggestions based on volume + country logic

This version is **prototype-ready** with placeholder inputs set to 1 for now.
""")

# --- Fixed Product Inputs (Per SKU)
st.header("📦 SKU Details (Fixed)")
sku = st.text_input("SKU Code", "SC1014")
length = st.number_input("Length (mm)", value=255)
width = st.number_input("Width (mm)", value=355)
depth = st.number_input("Depth (mm)", value=20)

volume_m3 = (length * width * depth) / 1_000_000_000  # Convert mm³ to m³
st.write(f"**Volume (m³)**: `{volume_m3:.6f}`")

factory_cost_zar = st.number_input("ZAR Factory Cost per unit", value=1.0)
export_cost_zar = st.number_input("ZAR Export Cost per unit", value=1.0)
ip_commission_pct = st.number_input("IP Commission %", value=1.0)

# --- Fixed Country Settings
st.header("🌍 Country Cost Factors (Fixed per Country)")
col1, col2, col3 = st.columns(3)
with col1:
    country = st.selectbox("Destination Country", ["UK", "USA", "Germany"])
with col2:
    exchange_rate = st.number_input("Exchange Rate (ZAR → Local)", value=1.0)
with col3:
    vat_pct = st.number_input("VAT %", value=1.0)

# Placeholder monthly cost values per country (will evolve later)
st.subheader("📊 Monthly Country-Level Cost Drivers")
advertising_monthly = st.number_input("Advertising Budget (Monthly)", value=1.0)
banking_fees = st.number_input("Banking Cost (Monthly)", value=1.0)
other_fees = st.number_input("Other Ops Cost (Monthly)", value=1.0)
warehouse_cost = st.number_input("Warehousing (Monthly)", value=1.0)
packing_cost = st.number_input("Packing Labour (Monthly)", value=1.0)
courier_cost = st.number_input("Courier Cost per Unit", value=1.0)

# --- Per Unit Calculations
st.header("💰 Price Engine")
units_per_month = st.number_input("Expected Monthly Units Sold", value=1)

# ZAR total cost
total_cost_zar = factory_cost_zar + export_cost_zar
commissioned_zar = total_cost_zar * (1 + ip_commission_pct / 100)
converted_local_cost = commissioned_zar / exchange_rate

# Shared overhead allocation
total_monthly_overheads = advertising_monthly + banking_fees + other_fees + warehouse_cost + packing_cost
per_unit_overhead = total_monthly_overheads / units_per_month if units_per_month else 0

# Final cost per unit
landed_total_cost = converted_local_cost + per_unit_overhead + courier_cost

# Suggested RRP based on volume + markup
markup_factor = 2.5  # Initial placeholder
suggested_rrp_ex_vat = landed_total_cost * markup_factor
vat_amount = suggested_rrp_ex_vat * (vat_pct / 100)
suggested_rrp_incl_vat = suggested_rrp_ex_vat + vat_amount

# --- Output Summary
st.subheader("💡 Suggested Price Summary")
st.write(f"**Cost per Unit (Local)**: `{landed_total_cost:.2f}`")
st.write(f"**Suggested RRP (Excl. VAT)**: `{suggested_rrp_ex_vat:.2f}`")
st.write(f"**Suggested RRP (Incl. VAT)**: `{suggested_rrp_incl_vat:.2f}`")

if markup_factor < 2:
    st.warning("⚠️ Markup too low – consider raising your prices.")
elif markup_factor >= 2.5:
    st.success("✅ Strong markup for sustainable margin.")
