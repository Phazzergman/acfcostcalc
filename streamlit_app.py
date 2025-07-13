import streamlit as st

st.set_page_config(page_title="ACF SKU Profit Calculator", layout="centered")

st.title("🎨 SC1014 Profit & Pricing Calculator")

st.markdown("Use this tool to estimate pricing, margins, and costs for **SKU: SC1014** across different countries.")

# --- Inputs
st.header("📦 Basic Info")
length = 255
width = 355
depth = 20
area_cm3 = (length * width * depth) / 1000
st.write(f"**Auto Area (cm³)**: `{area_cm3}`")

# --- Manual Inputs
st.subheader("💸 ZAR Cost Inputs")
factory_cost = st.number_input("ZAR Factory Cost per unit", min_value=0.0, value=0.0)
export_cost = st.number_input("ZAR Export Cost per unit", min_value=0.0, value=0.0)
ip_commission_pct = st.number_input("IP Commission (%)", min_value=0.0, value=0.0)

st.subheader("🌍 Destination & Conversion")
country = st.selectbox("Destination Country", ["UK", "USA", "Germany"])
exchange_rate = st.number_input(f"Manual Exchange Rate (ZAR → {country} Currency)", min_value=0.01, value=23.5)
vat_pct = st.number_input(f"{country} VAT (%)", min_value=0.0, value=20.0)

st.subheader("🚛 Shipping & Container")
packing_size_m3 = st.number_input("Container Packing Size (m³)", min_value=0.0, value=0.10)
container_cost_zar = st.number_input("Total Container Cost (ZAR)", min_value=0.0, value=156000.0)

st.subheader("💼 Other Costs")
advertising = st.number_input("Advertising Budget per unit (Local)", min_value=0.0, value=0.0)
banking = st.number_input("Banking Cost per unit (Local)", min_value=0.0, value=0.0)
other = st.number_input("Other Cost per unit (Local)", min_value=0.0, value=0.0)

st.subheader("🏭 3PL & Fulfilment")
warehousing = st.number_input("Warehousing per unit (Local)", min_value=0.0, value=0.0)
packing = st.number_input("Packing Rate per unit (Local)", min_value=0.0, value=0.0)
courier = st.number_input("Courier per unit (Local)", min_value=0.0, value=0.0)

# --- Calculations
zar_total = factory_cost + export_cost
zar_per_unit_commissioned = zar_total * (1 + ip_commission_pct / 100)

container_cost_per_unit = (container_cost_zar * packing_size_m3)  # crude logic to refine later
landed_cost_zar = zar_per_unit_commissioned + container_cost_per_unit
landed_cost_local = landed_cost_zar / exchange_rate

fulfilment_total = advertising + banking + other + warehousing + packing + courier
full_cost_per_unit = landed_cost_local + fulfilment_total

# --- Output
st.header("📊 Pricing Breakdown")
st.write(f"**Landed Cost per Unit (Local)**: `{landed_cost_local:.2f}`")
st.write(f"**Total Cost incl. Ads, 3PL etc. (Local)**: `{full_cost_per_unit:.2f}`")

rrp_ex_vat = st.number_input("Target RRP (Ex VAT)", min_value=0.0, value=27.0)
vat_amount = rrp_ex_vat * vat_pct / 100
rrp_incl_vat = rrp_ex_vat + vat_amount
profit = rrp_ex_vat - full_cost_per_unit
margin = (profit / rrp_ex_vat * 100) if rrp_ex_vat else 0

st.subheader("💰 Financial Summary")
st.write(f"**Target RRP Incl. VAT**: `{rrp_incl_vat:.2f}`")
st.write(f"**Gross Profit per Unit**: `{profit:.2f}`")
st.write(f"**Gross Margin %**: `{margin:.2f}%`")

if profit < 0:
    st.error("⚠️ You're selling at a loss! Recalculate.")
elif margin < 30:
    st.warning("⚠️ Margin is low. Consider adjusting price or costs.")
else:
    st.success("✅ Looks profitable.")

st.caption("Built for internal use. All values are manual inputs.")
