
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ACF Multi-Country Pricing Grid", layout="wide")

st.title("🧠 ACF SKU Pricing Intelligence Dashboard")

# Country visibility toggles
show_uk = st.sidebar.checkbox("Show UK Settings", value=True)
show_usa = st.sidebar.checkbox("Show USA Settings", value=True)
show_germany = st.sidebar.checkbox("Show Germany Settings", value=True)

country_inputs = {}

if show_uk:
    with st.sidebar.expander("🇬🇧 UK Settings"):
        country_inputs["UK"] = {
            "rate": st.number_input("UK Exchange Rate", value=24.0),
            "vat": st.number_input("UK VAT %", value=20.0),
            "container_cost": st.number_input("UK Container Cost (ZAR)", value=150000),
            "container_volume": st.number_input("UK Container Capacity (m³)", value=95.2),
            "ads": st.number_input("UK Advertising (Monthly)", value=2000),
            "bank": st.number_input("UK Banking (Monthly)", value=2000),
            "ops": st.number_input("UK Ops Cost (Monthly)", value=4000),
            "warehouse": st.number_input("UK Warehousing (Monthly)", value=10000),
            "pack": st.number_input("UK Packing per unit", value=1.0),
            "courier": st.number_input("UK Courier per unit", value=7.99),
            "volume": st.number_input("UK Monthly Units", value=10000),
        }

if show_usa:
    with st.sidebar.expander("🇺🇸 USA Settings"):
        country_inputs["USA"] = {
            "rate": st.number_input("USA Exchange Rate", value=18.0),
            "vat": st.number_input("USA VAT %", value=0.0),
            "container_cost": st.number_input("USA Container Cost (ZAR)", value=150000),
            "container_volume": st.number_input("USA Container Capacity (m³)", value=95.2),
            "ads": st.number_input("USA Advertising (Monthly)", value=2000),
            "bank": st.number_input("USA Banking (Monthly)", value=2000),
            "ops": st.number_input("USA Ops Cost (Monthly)", value=4000),
            "warehouse": st.number_input("USA Warehousing (Monthly)", value=10000),
            "pack": st.number_input("USA Packing per unit", value=1.0),
            "courier": st.number_input("USA Courier per unit", value=8.99),
            "volume": st.number_input("USA Monthly Units", value=10000),
        }

if show_germany:
    with st.sidebar.expander("🇩🇪 Germany Settings"):
        country_inputs["Germany"] = {
            "rate": st.number_input("Germany Exchange Rate", value=19.0),
            "vat": st.number_input("Germany VAT %", value=19.0),
            "container_cost": st.number_input("Germany Container Cost (ZAR)", value=150000),
            "container_volume": st.number_input("Germany Container Capacity (m³)", value=95.2),
            "ads": st.number_input("Germany Advertising (Monthly)", value=2000),
            "bank": st.number_input("Germany Banking (Monthly)", value=2000),
            "ops": st.number_input("Germany Ops Cost (Monthly)", value=4000),
            "warehouse": st.number_input("Germany Warehousing (Monthly)", value=10000),
            "pack": st.number_input("Germany Packing per unit", value=1.0),
            "courier": st.number_input("Germany Courier per unit", value=9.99),
            "volume": st.number_input("Germany Monthly Units", value=10000),
        }

# Sample data
sku_data = {
    "Category": ["Alpha"] * 5,
    "SKU": [f"A-{i+1:02}" for i in range(5)],
    "Length (mm)": [312, 485, 259, 385, 376],
    "Width (mm)": [598, 245, 582, 212, 323],
    "Depth (mm)": [20] * 5,
    "Factory ZAR": [47.28, 27.29, 56.24, 40.48, 34.88],
    "Export ZAR": [36.3, 48.93, 21.35, 47.49, 47.12],
    "Commission %": [33] * 5,
}

df = pd.DataFrame(sku_data)

# Pricing columns
for country, inputs in country_inputs.items():
    rate = inputs["rate"]
    vat = inputs["vat"]
    landed = df["Factory ZAR"] * rate / 100
    rrp_exvat = landed * 2.5
    rrp_incvat = rrp_exvat * (1 + vat / 100)
    df[f"{country} Landed"] = landed.round(2)
    df[f"{country} RRP exVAT"] = rrp_exvat.round(2)
    df[f"{country} RRP incVAT"] = rrp_incvat.round(2)

st.dataframe(df, use_container_width=True)
