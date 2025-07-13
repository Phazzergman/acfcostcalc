
import streamlit as st
import pandas as pd
import numpy as np

# App config
st.set_page_config(page_title="ACF Pricing Tool v4", layout="wide")
st.title("💸 ACF Pricing Intelligence Dashboard v4")

# Country-specific cost input toggles
st.sidebar.header("🌍 Toggle Country Visibility")
countries = {
    "UK": {"visible": st.sidebar.toggle("Show UK", value=True)},
    "USA": {"visible": st.sidebar.toggle("Show USA", value=True)},
    "Germany": {"visible": st.sidebar.toggle("Show Germany", value=True)}
}

# Global duration for container sell-through
duration = st.sidebar.number_input("Expected container sell-through duration (months)", min_value=1, max_value=24, value=6)



        countries[country].update({
            "rate": rate, "vat": vat, "container_cost": container_cost,
            "container_volume": container_volume, "ads": ads, "bank": bank,
            "ops": ops, "ware": ware, "pack": pack, "courier": courier, "volume": volume
        })

# Sample SKU Data - Extended with volume moved next to Depth
sku_data = pd.DataFrame({
    "Category": ["Alpha"] * 5,
    "SKU": ["A-01", "A-02", "A-03", "A-04", "A-05"],
    "Length (mm)": [312, 485, 259, 385, 376],
    "Width (mm)": [598, 245, 582, 212, 323],
    "Depth (mm)": [20] * 5,
    "Volume m³": [0.0037, 0.0024, 0.0033, 0.0016, 0.0024],
    "Factory ZAR": [47.28, 27.29, 56.24, 40.48, 34.88],
    "Export ZAR": [36.3, 48.93, 21.35, 47.49, 47.12],
    "Commission %": [33] * 5
})

# Calculate estimated landed cost and RRP for each country
for country in countries:
    if countries[country]["visible"]:
        r = countries[country]
        sku_data[f"{country} Landed"] = sku_data["Export ZAR"] * r["rate"] / 20  # crude example
        monthly_cost_per_unit = (
            (r["ads"] + r["bank"] + r["ops"] + r["ware"]) * duration / r["volume"]
        )
        sku_data[f"{country} RRP exVAT"] = sku_data[f"{country} Landed"] + r["pack"] + r["courier"] + monthly_cost_per_unit
        sku_data[f"{country} RRP incVAT"] = sku_data[f"{country} RRP exVAT"] * (1 + r["vat"])

# Display SKU data in wide view
st.dataframe(sku_data, use_container_width=True)
