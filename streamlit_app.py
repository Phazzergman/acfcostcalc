import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="📦 ACF SKU Pricing Intelligence Dashboard", layout="wide")
st.title("📦 ACF SKU Pricing Intelligence Dashboard")

# Sidebar country toggle
st.sidebar.header("Toggle Countries")
countries = ["UK", "USA", "Germany"]
country_toggle = {c: st.sidebar.checkbox(c, value=(c == "UK")) for c in countries}

# Sell-through duration
duration_months = st.sidebar.number_input("Sell-Through Duration (Months)", min_value=1, max_value=24, value=6)

# Country-specific settings
country_settings = {}
for country in countries:
    if country_toggle[country]:
        with st.sidebar.expander(f"{country} Settings", expanded=True):
            rate = st.number_input(f"{country} Exchange Rate (ZAR → Local)", value=19.0, key=f"rate_{country}")
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

# Base columns
base_columns = [
    "Category", "SKU",
