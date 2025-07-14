import streamlit as st

st.title("ACF UK Pricing & Profitability Estimator")

st.header("1. Base Costs")
factory_cost = st.number_input("Factory cost per unit (in £):", value=4.17)
shipping_cost = st.number_input("Shipping cost per unit (in £):", value=0.00)
landed_cost = factory_cost + shipping_cost
st.write(f"**Landed Cost (per unit):** £{landed_cost:.2f}")

st.header("2. Commission")
commission_percent = st.slider("Commission % (UK-based entity)", 0, 100, 20)
commission_value = landed_cost * (commission_percent / 100)
post_commission_cost = landed_cost + commission_value
st.write(f"**Cost after Commission:** £{post_commission_cost:.2f}")

st.header("3. Markup & Retail")
markup_percent = st.slider("Markup %", 0, 300, 50)
pre_vat_price = post_commission_cost * (1 + markup_percent / 100)
st.write(f"**Price Before VAT:** £{pre_vat_price:.2f}")

vat_percent = st.slider("VAT %", 0, 30, 20)
vat_value = pre_vat_price * (vat_percent / 100)
final_price = pre_vat_price + vat_value
st.write(f"**Final Price (incl. VAT):** £{final_price:.2f}")

st.header("4. Optional Monthly Costs")
st.caption("These will be divided by units sold and added to monthly per-unit cost.")
monthly_warehouse_cost = st.number_input("Monthly Warehousing (£):", value=0.0)
monthly_handling_cost = st.number_input("Monthly Postage/Handling (£):", value=0.0)
monthly_ad_cost = st.number_input("Monthly Advertising Spend (£):", value=0.0)
units_sold_monthly = st.number_input("Estimated Monthly Units Sold:", value=1000)

if units_sold_monthly > 0:
    warehouse_per_unit = monthly_warehouse_cost / units_sold_monthly
    handling_per_unit = monthly_handling_cost / units_sold_monthly
    ad_per_unit = monthly_ad_cost / units_sold_monthly
    total_monthly_addon = warehouse_per_unit + handling_per_unit + ad_per_unit

    st.write(f"**Add-on per unit from monthly ops:** £{total_monthly_addon:.2f}")
    adjusted_profit = final_price - post_commission_cost - total_monthly_addon
    st.success(f"**Estimated Profit per Unit:** £{adjusted_profit:.2f}")
else:
    st.warning("Please input estimated units sold to calculate operational cost impact.")

st.header("5. Exchange Rate (if needed)")
use_forex = st.checkbox("Apply exchange rate?")
if use_forex:
    forex_rate = st.number_input("Exchange Rate (e.g. 1.20 for ZAR → GBP):", value=1.0)
    local_price = final_price * forex_rate
    st.write(f"**Local Price Equivalent:** {local_price:.2f} (based on rate)")
