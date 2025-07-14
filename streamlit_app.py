import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="📦 ACF SKU Pricing Intelligence Dashboard", layout="wide")
st.title("📦 ACF SKU Pricing Intelligence Dashboard")

# Buttons in main page
col1, col2, col3 = st.columns(3)
with col1:
    recalc_button = st.button("Recalculate")
with col2:
    save_button = st.button("Save Changes")
with col3:
    undo_button = st.button("Undo")

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
    "Category", "SKU", "Length_mm", "Width_mm", "Depth_mm",
    "Factory_Cost_ZAR", "Export_Cost_ZAR", "Commission_%"
]

# File for persistence
file_path = "sku_data.csv"

# Load from file or initial
if "sku_df" not in st.session_state:
    try:
        st.session_state.sku_df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.session_state.sku_df = pd.DataFrame([
            ["Alpha", "ASC608", 152, 203, 20, 16.79, 21.60, 33],
            ["Alpha", "ASC1012", 255, 305, 20, 31.86, 40.97, 33],
            ["Alpha", "ASC1014", 255, 355, 20, 35.22, 45.29, 33],
            ["Alpha", "ASC1216", 305, 406, 20, 42.99, 55.28, 33],
            ["Alpha", "ASC1418", 355, 457, 20, 53.51, 68.82, 33],
            ["Alpha", "ASC1620", 406, 501, 20, 62.34, 80.17, 33],
            ["Alpha", "ASC1824", 457, 610, 20, 73.20, 94.15, 33],
            ["Alpha", "ASC2024", 501, 610, 20, 78.14, 100.49, 33],
            ["Alpha", "ASC2430", 610, 762, 20, 99.56, 128.04, 33],
        ], columns=base_columns)
    st.session_state.history = []  # For undo

# Define recalc function
def recalculate():
    df = st.session_state.sku_df.copy()
    df["Volume_m³"] = (df["Length_mm"] * df["Width_mm"] * df["Depth_mm"]) / 1_000_000_000
    for country in countries:
        if country_toggle[country] and country in country_settings:
            rate = country_settings[country]["rate"]
            vat = country_settings[country]["vat"]
            monthly = country_settings[country]["monthly_costs"]
            vol_total = country_settings[country]["container_volume"]
            cont_cost = country_settings[country]["container_cost"]

            cost_load = (monthly / vol_total) * df["Volume_m³"] * duration_months
            shipping_ZAR = cont_cost * df["Volume_m³"] / vol_total
            total_ZAR = df["Factory_Cost_ZAR"] + df["Export_Cost_ZAR"] + shipping_ZAR
            landed = (total_ZAR / rate) + cost_load
            commission_factor = 1 + (df["Commission_%"] / 100)
            rrp_exvat = landed * commission_factor
            rrp_incvat = rrp_exvat * (1 + vat)
            df[f"{country} Landed"] = landed.round(2)
            df[f"{country} RRP exVAT"] = rrp_exvat.round(2)
            df[f"{country} RRP incVAT"] = rrp_incvat.round(2)
    st.session_state.sku_df = df

# Recalc always after settings (to handle toggle changes)
recalculate()

# Handle buttons
if recalc_button:
    st.session_state.history.append(st.session_state.sku_df[base_columns].copy())
    if len(st.session_state.history) > 5:
        st.session_state.history.pop(0)
    recalculate()

if save_button:
    st.session_state.sku_df[base_columns].to_csv(file_path, index=False)
    st.success("Changes saved to sku_data.csv!")

if undo_button and st.session_state.history:
    st.session_state.sku_df[base_columns] = st.session_state.history.pop()
    recalculate()
    st.success("Undone to previous state!")

# Selected countries
selected_countries = [c for c in countries if country_toggle[c]]

# Displayed columns
displayed_columns = base_columns + ["Volume_m³"] + sum([[f"{c} Landed", f"{c} RRP exVAT", f"{c} RRP incVAT"] for c in selected_countries if f"{c} Landed" in st.session_state.sku_df.columns], [])

# Displayed DF
displayed_df = st.session_state.sku_df[displayed_columns].copy()

# Editor
edited_df = st.data_editor(
    displayed_df,
    use_container_width=True,
    num_rows="dynamic",
    disabled=["Volume_m³"] + sum([[f"{c} Landed", f"{c} RRP exVAT", f"{c} RRP incVAT"] for c in selected_countries], []),
    hide_index=True
)

# Persist edits
st.session_state.sku_df[base_columns] = edited_df[base_columns]

# CSS for color coding
st.markdown("""
<style>
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p {
  font-weight: bold;
}
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="UK Landed"], 
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="UK RRP exVAT"], 
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="UK RRP incVAT"] {
  color: blue;
}
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="USA Landed"], 
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="USA RRP exVAT"], 
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="USA RRP incVAT"] {
  color: red;
}
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="Germany Landed"], 
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="Germany RRP exVAT"], 
div.stDataFrame div[data-testid="stHorizontalBlock"] > div > div > div > p[title="Germany RRP incVAT"] {
  color: green;
}
</style>
""", unsafe_allow_html=True)
