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
            ads = st.number_input(f"{country} Advertising (Monthly)", value=3000.0, key=f"ads_{country}")
            bank = st.number_input(f"{country} Banking (Monthly)", value=2000.0, key=f"bank_{country}")
            ops = st.number_input(f"{country} Ops Cost (Monthly)", value=4000.0, key=f"ops_{country}")
            ware = st.number_input(f"{country} Warehousing (Monthly)", value=10000.0, key=f"ware_{country}")
            pack = st.number_input(f"{country} Packing (Monthly)", value=6000.0, key=f"pack_{country}")
            cour = st.number_input(f"{country} Courier (Monthly)", value=7000.0, key=f"cour_{country}")

        country_settings[country] = {
            "rate": rate,
            "vat": vat,
            "monthly_costs": ads + bank + ops + ware + pack + cour
        }

# Base columns (no Category)
base_columns = [
    "SKU", "Length_mm", "Width_mm", "Depth_mm",
    "Export_Cost_ZAR", "Imported_Cost_ZAR", "Commission_%"
]

# Local file persistence
file_path = "sku_data.csv"

# Load or start fresh
if "sku_df" not in st.session_state:
    try:
        st.session_state.sku_df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.session_state.sku_df = pd.DataFrame([
            ["ASC608", 152, 203, 20, 16.79, 0.0, 33],
            ["ASC1012", 255, 305, 20, 31.86, 0.0, 33],
            ["ASC1014", 255, 355, 20, 35.22, 0.18, 33],
            ["ASC1216", 305, 406, 20, 42.99, 0.20, 33],
            ["ASC1418", 355, 457, 20, 53.51, 0.0, 33],
            ["ASC1620", 406, 501, 20, 62.34, 0.0, 33],
            ["ASC1824", 457, 610, 20, 73.20, 0.0, 33],
            ["ASC2024", 501, 610, 20, 78.14, 0.0, 33],
            ["ASC2430", 610, 762, 20, 99.56, 0.0, 33],
        ], columns=base_columns)
    st.session_state.history = []

# Recalculate function
def recalculate():
    df = st.session_state.sku_df.copy()
    df["Volume_m³"] = (df["Length_mm"] * df["Width_mm"] * df["Depth_mm"]) / 1_000_000_000

    for country in countries:
        if country_toggle[country] and country in country_settings:
            rate = country_settings[country]["rate"]
            vat = country_settings[country]["vat"]
            total_monthly_cost = country_settings[country]["monthly_costs"]

            total_imported_cost_sum = df["Imported_Cost_ZAR"].sum()
            value_share = df["Imported_Cost_ZAR"] / total_imported_cost_sum if total_imported_cost_sum != 0 else 0
            sku_monthly_cost = value_share * total_monthly_cost * duration_months

            total_ZAR = df["Export_Cost_ZAR"] + df["Imported_Cost_ZAR"]
            landed = (total_ZAR / rate) + sku_monthly_cost

            rrp_exvat = landed * (1 + df["Commission_%"] / 100)
            rrp_incvat = rrp_exvat * (1 + vat)

            df[f"{country} Landed"] = landed.round(2)
            df[f"{country} RRP exVAT"] = rrp_exvat.round(2)
            df[f"{country} RRP incVAT"] = rrp_incvat.round(2)

    st.session_state.sku_df = df

# Always recalc on load
recalculate()

# Button actions
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

# Country selection and final display
selected_countries = [c for c in countries if country_toggle[c]]
displayed_columns = base_columns + ["Volume_m³"] + sum([
    [f"{c} Landed", f"{c} RRP exVAT", f"{c} RRP incVAT"]
    for c in selected_countries
    if f"{c} Landed" in st.session_state.sku_df.columns
], [])

# Show editable table
edited_df = st.data_editor(
    st.session_state.sku_df[displayed_columns],
    use_container_width=True,
    num_rows="dynamic",
    disabled=["Volume_m³"] + [
        f"{c} Landed" for c in selected_countries
    ] + [
        f"{c} RRP exVAT" for c in selected_countries
    ] + [
        f"{c} RRP incVAT" for c in selected_countries
    ],
    hide_index=True
)

# Save changes live
st.session_state.sku_df[base_columns] = edited_df[base_columns]
