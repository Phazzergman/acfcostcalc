import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="ACF Pricing Grid", layout="wide")
st.title("📊 ACF Multi-SKU / Multi-Country Pricing Dashboard")

st.markdown("""
This view replicates your Excel layout:
- **Rows** = SKUs (grouped by category)
- **Columns** = Size + country-specific costs
- Fixed size/volume data on the left, scrollable pricing logic on the right
""")

# ---- Sample SKU Grid Setup ----
categories = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet"]
skus = []

for cat in categories:
    for i in range(1, 21):
        skus.append({
            "Category": cat,
            "SKU": f"{cat[:1]}-{i:02d}",
            "Length (mm)": np.random.randint(200, 600),
            "Width (mm)": np.random.randint(200, 600),
            "Depth (mm)": 20,
            "Factory ZAR": round(np.random.uniform(20, 60), 2),
            "Export ZAR": round(np.random.uniform(20, 50), 2),
            "Commission %": 33.0
        })

sku_df = pd.DataFrame(skus)
sku_df["Volume m³"] = (sku_df["Length (mm)"] * sku_df["Width (mm)"] * sku_df["Depth (mm)"]) / 1_000_000_000

# --- Country Settings (can be edited later via sidebar)
countries = ["UK", "USA", "Germany"]
country_factors = {
    "UK":     {"Rate": 23.5, "VAT": 20, "Cont_ZAR": 156000, "Cont_m3": 59.25},
    "USA":    {"Rate": 18.7, "VAT": 0,  "Cont_ZAR": 156000, "Cont_m3": 59.25},
    "Germany":{"Rate": 20.1, "VAT": 19, "Cont_ZAR": 156000, "Cont_m3": 59.25}
}

# --- Cost Calculations Per Country
for country, settings in country_factors.items():
    rate = settings["Rate"]
    vat = settings["VAT"]
    cont_cost = settings["Cont_ZAR"]
    cont_vol = settings["Cont_m3"]

    container_share = (sku_df["Volume m³"] / cont_vol) * cont_cost
    zar_total = sku_df["Factory ZAR"] + sku_df["Export ZAR"]
    commissioned = zar_total * (1 + sku_df["Commission %"] / 100)
    landed_zar = commissioned + container_share
    landed_local = landed_zar / rate
    rrp_ex_vat = landed_local * 2.5
    rrp_incl_vat = rrp_ex_vat * (1 + vat / 100)

    sku_df[f"{country} Landed"] = landed_local.round(2)
    sku_df[f"{country} RRP exVAT"] = rrp_ex_vat.round(2)
    sku_df[f"{country} RRP incVAT"] = rrp_incl_vat.round(2)

# --- Display the final wide dataframe
st.dataframe(sku_df, use_container_width=True)

st.caption("Scroll right → to compare per-country pricing across all SKUs")
