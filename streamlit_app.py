import pandas as pd

# --- INPUT DATA ---
data = [
    {"SKU": "SKU001", "Export Cost": 2.50, "Volume": 0.0012},
    {"SKU": "SKU002", "Export Cost": 5.80, "Volume": 0.0021},
    # Add more as needed...
]

df = pd.DataFrame(data)

# --- SETTINGS ---
exchange_rate_buffer_pct = 0.20
vat_rate = 0.00  # Currently 0% for now
commission_pct = 0.05  # e.g. 5%
markup_pct = 0.50       # e.g. 50%

# --- CALCULATIONS ---
df["UK Landed Cost"] = df["Export Cost"] * (1 + exchange_rate_buffer_pct)
df["Commission"] = df["UK Landed Cost"] * commission_pct
df["Cost + Commission"] = df["UK Landed Cost"] + df["Commission"]
df["Retail (pre-VAT)"] = df["Cost + Commission"] * (1 + markup_pct)
df["Retail (incl. VAT)"] = df["Retail (pre-VAT)"] * (1 + vat_rate)

# --- ROUNDING ---
df = df.round(2)

# --- OUTPUT ---
import ace_tools as tools; tools.display_dataframe_to_user(name="SKU Pricing Preview (UK)", dataframe=df)
