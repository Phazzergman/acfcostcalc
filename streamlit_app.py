import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="📦 ACF SKU Pricing Intelligence Dashboard", layout="wide")
st.title("📦 ACF SKU Pricing Intelligence Dashboard")

# Country toggle
st.sidebar.header("Toggle Countries")
countries = ["UK", "USA", "Germany"]
country_toggle = {country: st.sidebar.checkbox(country, value=(country == "UK")) for country in countries}

# Sell-Through Duration (months)
duration_months = st.sidebar.number_input("Sell-Through Duration (Months)", min_value=1, max_value=24, value=6)

# Country-specific costs
country_settings = {}
for country in countries:
    if country_toggle[country]:
        with st.sidebar.expander(f"{country} Settings", expanded=True):
            rate = st.number_input(f"{country} Exchange Rate (ZAR → Local)", value=19.5, key=f"rate_{country}")
            vat = st.number_input(f"{country} VAT %", value=0.20, key=f"vat_{country}")
            cont_cost = st.number_input(f"{country} Container Cost (ZAR)", value=150000.0, key=f"contcost_{country}")
            cont_vol = st.number_input(f"{country} Container Volume (m³)", value=95.25, key=f"contvol_{country}")
            ads = st.number_input(f"{country} Advertising (Monthly)", value=3000.0, key=f"ads_{country}")
            bank = st.number_input(f"{country} Banking (Monthly)", value=2000.0, key=f"bank_{country}")
            ops = st.number_input(f"{country} Ops Cost (Monthly)", value=4000.0, key=f"ops_{country}")
            ware = st.number_input(f"{country} Warehousing (Monthly)", value=10000.0, key=f"ware_{country}")
            pack = st.number_input(f"{country} Packing (Monthly)", value=6000.0, key=f"pack_{country}")
            cour = st.number_input(f"{country} Courier (Monthly)", value=7000.0, key=f"cour_{country}")

        country_settings[country] = {
            "rate": rate,
            "vat": vat,
            "container_cost": cont_cost,
            "container_volume": cont_vol,
            "monthly_costs": ads + bank + ops + ware + pack + cour
        }

# Base SKU data
sku_columns = [
    "Category", "SKU", "Length_mm", "Width_mm", "Depth_mm",
    "Factory_Cost_ZAR", "Export_Cost_ZAR", "Commission_%"
]
sku_data = [
    ["Alpha", "ASC68", 152, 203, 20, 16.79, 21.60, 33],
    ["Alpha", "ASC1012", 255, 305, 20, 31.86, 40.97, 33],
    ["Alpha", "ASC1014", 255, 355, 20, 35.22, 45.29, 33],
    ["Alpha", "ASC1216", 305, 406, 20, 42.99, 55.28, 33],
    ["Alpha", "ASC1418", 355, 457, 20, 53.51, 68.82, 33],
    ["Alpha", "ASC1620", 406, 501, 20, 62.34, 80.17, 33],
    ["Alpha", "ASC1824", 457, 610, 20, 73.20, 94.15, 33],
    ["Alpha", "ASC2024", 501, 610, 20, 78.14, 100.49, 33],
    ["Alpha", "ASC2430", 610, 762, 20, 99.56, 128.04, 33],
]

# Load into editable frame
sku_df = pd.DataFrame(sku_data, columns=sku_columns)
sku_df = st.data_editor(sku_df, num_rows="dynamic", use_container_width=True)

# Auto-calculate Volume_m³
sku_df["Volume_m³"] = (sku_df["Length_mm"] * sku_df["Width_mm"] * sku_df["Depth_mm"]) / 1_000_000_000

# Calculate per-country pricing
for country in countries:
    if country_toggle[country]:
        rate = country_settings[country]["rate"]
        vat = country_settings[country]["vat"]
        monthly = country_settings[country]["monthly_costs"]
        total_volume = country_settings[country]["container_volume"]

        # Monthly cost allocation per SKU
        cost_load = (monthly / total_volume) * sku_df["Volume_m³"] * duration_months
        commission_factor = 1 + (sku_df["Commission_%"] / 100)

        landed = sku_df["Export_Cost_ZAR"] + cost_load
        rrp_exvat = landed * commission_factor
        rrp_incvat = rrp_exvat * (1 + vat)

        sku_df[f"{country} Landed"] = landed.round(2)
        sku_df[f"{country} RRP exVAT"] = rrp_exvat.round(2)
        sku_df[f"{country} RRP incVAT"] = rrp_incvat.round(2)

# Show final table with locked volume + dynamic pricing outputs
st.data_editor(
    sku_df,
    use_container_width=True,
    disabled=["Volume_m³"] + 
             [f"{country} Landed" for country in countries if country_toggle[country]] +
             [f"{country} RRP exVAT" for country in countries if country_toggle[country]] +
             [f"{country} RRP incVAT" for country in countries if country_toggle[country]]
)

