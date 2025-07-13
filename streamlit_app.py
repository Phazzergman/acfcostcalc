
import streamlit as st
import pandas as pd
import numpy as np

# --- App setup
st.set_page_config(page_title="ACF Multi-Country Pricing Grid", layout="wide")
st.title("📦 ACF SKU Pricing Intelligence Dashboard")

# --- Country toggle
country_toggles = {}
countries = ["UK", "USA", "Germany"]
with st.sidebar:
    st.header("Toggle Countries")
    for country in countries:
        country_toggles[country] = st.checkbox(f"{country}", value=True)

# --- Country-specific inputs
country_settings = {}
for country in countries:
    if not country_toggles[country]:
        continue
    with st.sidebar.expander(f"{country} Settings", expanded=True):
        rate = st.number_input(f"{country} Exchange Rate (ZAR to Local)", value=19.5, key=f"rate_{country}")
        vat = st.number_input(f"{country} VAT %", value=0.2, key=f"vat_{country}")
        container_cost = st.number_input(f"{country} Container Cost (ZAR)", value=150000.0, key=f"contcost_{country}")
        container_volume = st.number_input(f"{country} Container Capacity (m³)", value=95.25, key=f"contvol_{country}")
        ads = st.number_input(f"{country} Advertising (Monthly)", value=3000.0, key=f"ads_{country}")
        bank = st.number_input(f"{country} Banking (Monthly)", value=2000.0, key=f"bank_{country}")
        ops = st.number_input(f"{country} Ops Cost (Monthly)", value=4000.0, key=f"ops_{country}")
        ware = st.number_input(f"{country} Warehousing (Monthly)", value=10000.0, key=f"ware_{country}")
        pack = st.number_input(f"{country} Packing per unit", value=1.00, key=f"pack_{country}")
        courier = st.number_input(f"{country} Courier per unit", value=7.50, key=f"cour_{country}")
        volume = st.number_input(f"{country} Monthly Units", value=1000.0, key=f"vol_{country}")

    country_settings[country] = {
        "rate": rate,
        "vat": vat,
        "container_cost": container_cost,
        "container_volume": container_volume,
        "ads": ads,
        "bank": bank,
        "ops": ops,
        "ware": ware,
        "pack": pack,
        "courier": courier,
        "volume": volume,
    }

# --- SKU table toggle
st.sidebar.markdown("---")
use_custom_skus = st.sidebar.checkbox("Use Custom SKU Table", value=True)

# --- SKU Base Data
if use_custom_skus:
    default_data = {
        "SKU": ["ASC68", "ASC1012", "ASC1014", "ASC1216", "ASC1418", "ASC1620", "ASC1824", "ASC2024", "ASC2430",
                "ASC150", "ASC200", "ASC250", "ASC300", "ASC400", "ASC500",
                "ASCA5", "ASCA4", "ASCA3", "ASCA2", "ASCA1"],
        "Length_mm": [152, 255, 255, 305, 355, 406, 457, 501, 610, 150, 200, 250, 300, 400, 500, 148, 210, 297, 420, 594],
        "Width_mm": [203, 305, 355, 406, 457, 501, 610, 610, 762, 150, 200, 250, 300, 400, 500, 210, 297, 420, 594, 841],
        "Depth_mm": [20]*20,
        "Factory_Cost_ZAR": [16.79, 31.86, 35.22, 42.99, 53.51, 62.34, 73.20, 78.14, 99.56,
                             15.81, 21.50, 28.45, 34.81, 45.64, 64.18, 16.92, 28.05, 43.31, 71.76, 106.62],
        "Export_Cost_ZAR": [21.60, 40.97, 45.29, 55.28, 68.82, 80.17, 94.15, 100.49, 128.04,
                            20.34, 27.65, 36.59, 44.77, 58.70, 82.54, 21.76, 36.08, 55.70, 92.28, 137.13],
    }
    df = pd.DataFrame(default_data)
else:
    st.stop()

# --- Volume Calculation
df["Volume_m³"] = (df["Length_mm"] * df["Width_mm"] * df["Depth_mm"]) / 1e9

# --- Pricing Calculations
for country in countries:
    if not country_toggles[country]:
        continue
    cs = country_settings[country]
    landed = (df["Export_Cost_ZAR"] + cs["courier"] + cs["pack"] +
              (cs["container_cost"] / cs["container_volume"]) * df["Volume_m³"] +
              (cs["ads"] + cs["bank"] + cs["ops"] + cs["ware"]) / cs["volume"])
    rrp_exvat = landed * cs["rate"]
    rrp_incvat = rrp_exvat * (1 + cs["vat"])
    df[f"{country} Landed"] = landed.round(2)
    df[f"{country} RRP exVAT"] = rrp_exvat.round(2)
    df[f"{country} RRP incVAT"] = rrp_incvat.round(2)

# --- Display Table
st.dataframe(df, use_container_width=True, hide_index=True)
