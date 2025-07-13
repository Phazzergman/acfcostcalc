import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

st.set_page_config(page_title="ACF Multi-Country Pricing Grid", layout="wide")
st.title("🧮 ACF SKU Pricing Intelligence Dashboard")

# --- Country settings input block
st.sidebar.header("🌐 Country-Specific Cost Inputs")
countries = ["UK", "USA", "Germany"]
country_settings = {}

for country in countries:
    with st.sidebar.expander(f"{country} Settings", expanded=True):
        rate = st.number_input(f"{country} Exchange Rate (ZAR → Local)", value=23.5, key=f"rate_{country}")
        vat = st.number_input(f"{country} VAT %", value=20.0, key=f"vat_{country}")
        container_cost = st.number_input(f"{country} Container Cost (ZAR)", value=156000.0, key=f"contcost_{country}")
        container_volume = st.number_input(f"{country} Container Capacity (m³)", value=59.25, key=f"contvol_{country}")
        ads = st.number_input(f"{country} Advertising (Monthly)", value=3000.0, key=f"ads_{country}")
        bank = st.number_input(f"{country} Banking (Monthly)", value=250.0, key=f"bank_{country}")
        other = st.number_input(f"{country} Ops Cost (Monthly)", value=400.0, key=f"ops_{country}")
        ware = st.number_input(f"{country} Warehousing (Monthly)", value=1000.0, key=f"ware_{country}")
        pack = st.number_input(f"{country} Packing per unit", value=1.0, key=f"pack_{country}")
        courier = st.number_input(f"{country} Courier per unit", value=7.5, key=f"cour_{country}")
        volume = st.number_input(f"{country} Monthly Units", value=1000.0, key=f"vol_{country}")
        
        country_settings[country] = {
            "rate": rate,
            "vat": vat,
            "container_cost": container_cost,
            "container_volume": container_volume,
            "ads": ads,
            "bank": bank,
            "other": other,
            "ware": ware,
            "pack": pack,
            "courier": courier,
            "volume": volume
        }

# --- SKU base data
categories = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet"]
sku_data = []

for cat in categories:
    for i in range(1, 21):
        sku = f"{cat[0]}-{i:02d}"
        l, w, d = np.random.randint(200, 600), np.random.randint(200, 600), 20
        f_cost = round(np.random.uniform(20, 60), 2)
        e_cost = round(np.random.uniform(20, 50), 2)
        comm = 33.0
        volume = round((l * w * d) / 1_000_000_000, 6)
        row = {
            "Category": cat,
            "SKU": sku,
            "Length (mm)": l,
            "Width (mm)": w,
            "Depth (mm)": d,
            "Factory ZAR": f_cost,
            "Export ZAR": e_cost,
            "Commission %": comm,
            "Volume m³": volume
        }
        for c in countries:
            share = (volume / country_settings[c]['container_volume']) * country_settings[c]['container_cost']
            total_zar = f_cost + e_cost
            with_comm = total_zar * (1 + comm / 100)
            landed_zar = with_comm + share
            landed_local = landed_zar / country_settings[c]['rate']
            overheads = sum([country_settings[c][k] for k in ['ads', 'bank', 'other', 'ware']])
            overhead_unit = overheads / country_settings[c]['volume']
            final_cost = landed_local + overhead_unit + country_settings[c]['pack'] + country_settings[c]['courier']
            rrp_ex = final_cost * 2.5
            vat_amt = rrp_ex * country_settings[c]['vat'] / 100
            rrp_inc = rrp_ex + vat_amt
            row[f"{c} Landed"] = round(final_cost, 2)
            row[f"{c} RRP exVAT"] = round(rrp_ex, 2)
            row[f"{c} RRP incVAT"] = round(rrp_inc, 2)
        sku_data.append(row)

sku_df = pd.DataFrame(sku_data)

# --- Editable table with AgGrid
st.subheader("📋 All SKUs – Live Pricing Grid")
gb = GridOptionsBuilder.from_dataframe(sku_df)
gb.configure_pagination(enabled=True)
gb.configure_default_column(editable=False, groupable=True)
gb.configure_columns(["Factory ZAR", "Export ZAR", "Commission %"], editable=True)
ag_grid = AgGrid(sku_df, gridOptions=gb.build(), enable_enterprise_modules=False, height=700, fit_columns_on_grid_load=True)

# --- Download CSV
st.download_button("📥 Download as CSV", data=sku_df.to_csv(index=False), file_name="acf_pricing_grid.csv")
