import streamlit as st

st.set_page_config(page_title="ACF Multi-Country Pricing Calculator", layout="centered")
st.title("🌍 ACF SKU Pricing Tool – Multi-Country Container Planner")

st.markdown("""
This tool helps estimate country-specific RRP and margin based on your:
- SKU size & cost in ZAR
- Volume in m³
- IP commissions
- Container share
- Country-specific shipping, VAT and operational costs
""")

# --- Fixed SKU Info
st.header("📦 SKU Info (Fixed across all countries)")
sku = st.text_input("SKU Code", "SC1014")
length = st.number_input("Length (mm)", value=255)
width = st.number_input("Width (mm)", value=355)
depth = st.number_input("Depth (mm)", value=20)

volume_m3 = (length * width * depth) / 1_000_000_000
st.write(f"**Volume (m³):** `{volume_m3:.6f}`")

factory_cost_zar = st.number_input("Factory Cost (ZAR)", value=26.48)
export_cost_zar = st.number_input("Export Cost (ZAR)", value=35.22)
ip_commission_pct = st.number_input("IP Commission (%)", value=33.0)
max_discount_pct = st.number_input("Max Discount (%)", value=10.0)

zar_total = factory_cost_zar + export_cost_zar
zar_with_commission = zar_total * (1 + ip_commission_pct / 100)

st.divider()

# --- Country Configs
st.header("🌐 Country-Specific Cost Inputs")

countries = ["UK", "USA", "Germany"]
country_data = {}

for country in countries:
    st.subheader(f"🇨🇭 {country} Settings")
    with st.expander(f"{country} Inputs", expanded=True):
        exchange_rate = st.number_input(f"{country} Exchange Rate (ZAR → Local)", value=23.5, key=f"rate_{country}")
        vat_pct = st.number_input(f"{country} VAT %", value=20.0, key=f"vat_{country}")
        container_cost_zar = st.number_input(f"{country} Container Cost (ZAR)", value=156000.0, key=f"contcost_{country}")
        container_volume = st.number_input(f"{country} Total Container Capacity (m³)", value=59.25, key=f"contvol_{country}")

        # Monthly costs
        ads = st.number_input(f"{country} Advertising (Monthly)", value=3000.0, key=f"ads_{country}")
        banking = st.number_input(f"{country} Banking (Monthly)", value=250.0, key=f"bank_{country}")
        other = st.number_input(f"{country} Other Ops Cost (Monthly)", value=400.0, key=f"other_{country}")
        warehousing = st.number_input(f"{country} Warehousing (Monthly)", value=1000.0, key=f"ware_{country}")
        packing_rate = st.number_input(f"{country} Packing Labour per unit", value=1.0, key=f"pack_{country}")
        courier = st.number_input(f"{country} Courier per unit", value=7.5, key=f"cour_{country}")
        monthly_units = st.number_input(f"{country} Monthly Sales Volume", value=1000.0, key=f"monthly_{country}")

        # Cost Calculations
        container_share = (volume_m3 / container_volume) * container_cost_zar if container_volume else 0
        landed_zar = zar_with_commission + container_share
        landed_local = landed_zar / exchange_rate if exchange_rate else 0

        monthly_overheads = (ads + banking + other + warehousing)
        overhead_per_unit = monthly_overheads / monthly_units if monthly_units else 0

        total_cost_local = landed_local + overhead_per_unit + packing_rate + courier
        markup = 2.5
        rrp_ex_vat = total_cost_local * markup
        vat_amount = rrp_ex_vat * vat_pct / 100
        rrp_incl_vat = rrp_ex_vat + vat_amount

        profit = rrp_ex_vat - total_cost_local
        margin_pct = (profit / rrp_ex_vat) * 100 if rrp_ex_vat else 0

        st.markdown(f"**Final Cost (Local):** `{total_cost_local:.2f}`")
        st.markdown(f"**Suggested RRP ex VAT:** `{rrp_ex_vat:.2f}`")
        st.markdown(f"**Suggested RRP incl VAT:** `{rrp_incl_vat:.2f}`")
        st.markdown(f"**Profit per unit:** `{profit:.2f}` | **Margin %:** `{margin_pct:.1f}%`")

        country_data[country] = {
            "cost": total_cost_local,
            "rrp_ex_vat": rrp_ex_vat,
            "rrp_incl_vat": rrp_incl_vat,
            "profit": profit,
            "margin": margin_pct
        }
