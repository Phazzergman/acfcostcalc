
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ACF SKU Pricing Intelligence Dashboard", layout="wide")
st.title("📦 ACF SKU Pricing Intelligence Dashboard")

# --- Country toggles ---
country_toggles = {
    "UK": st.sidebar.checkbox("UK", value=True),
    "USA": st.sidebar.checkbox("USA"),
    "Germany": st.sidebar.checkbox("Germany")
}

# --- Editable Product Table ---
st.subheader("📦 Product Details (Editable)")
product_data = pd.DataFrame({
    "Category": ["Alpha", "Alpha", "Alpha", "Alpha", "Alpha"],
    "SKU": ["ASC68", "ASC1012", "ASC1014", "ASC1216", "ASC1418"],
    "Length_mm": [152, 255, 255, 305, 355],
    "Width_mm": [203, 305, 355, 406, 457],
    "Depth_mm": [20, 20, 20, 20, 20],
    "Factory_Cost_ZAR": [16.79, 31.86, 35.22, 42.99, 53.51],
    "Export_Cost_ZAR": [21.60, 40.97, 45.29, 55.28, 68.82],
    "Commission_%": [33, 33, 33, 33, 33],
})

# Calculate Volume
product_data["Volume_m³"] = (
    product_data["Length_mm"] * 
    product_data["Width_mm"] * 
    product_data["Depth_mm"]
) / 1e9

# Editable grid
product_data = st.data_editor(
    product_data,
    use_container_width=True,
    num_rows="dynamic",
    key="product_editor"
)

# --- Country-Specific Settings ---
def render_country_inputs(country_name):
    with st.sidebar.expander(f"{country_name} Settings", expanded=True):
        rate = st.number_input(f"{country_name} Exchange Rate (ZAR to Local)", value=19.5)
        vat = st.number_input(f"{country_name} VAT %", value=0.20)
        container_cost = st.number_input(f"{country_name} Container Cost (ZAR)", value=150000.0)
        container_volume = st.number_input(f"{country_name} Container Capacity (m³)", value=95.25)
        ads = st.number_input(f"{country_name} Advertising (Monthly)", value=3000.0)
        bank = st.number_input(f"{country_name} Banking (Monthly)", value=2000.0)
        ops = st.number_input(f"{country_name} Ops Cost (Monthly)", value=4000.0)
        ware = st.number_input(f"{country_name} Warehousing (Monthly)", value=6000.0)
        pack = st.number_input(f"{country_name} Packing per unit", value=1.0)
        courier = st.number_input(f"{country_name} Courier per unit", value=1.0)
        volume = st.number_input(f"{country_name} Monthly Units", value=1000.0)

        return {
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

country_settings = {}
for country, enabled in country_toggles.items():
    if enabled:
        country_settings[country] = render_country_inputs(country)

# Placeholder for dynamic pricing logic to be added
st.markdown("👈 Adjust settings to calculate RRP and landed costs per country...")
