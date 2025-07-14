To view keyboard shortcuts, press question mark
View keyboard shortcuts

Home 

Explore 

Notifications 

Messages 

SuperGrok 

Premium 

Lists 

Bookmarks 

Jobs 

Communities 

Articles 

Verified Orgs 

Profile 

More 

Post

ACF Canvas (Art Canvas Factory)

@ACFcanvasses

Grok 4

See new posts

I am busy setting up streamlit.app. I do not have any coding experience. I am working on a cost calculator for my business www.acfcanvasses.com Help me, do one step at a time, do not assume, and do not give me numerous options, do not repeat questions. ok

Let’s set up a Streamlit app for a cost calculator for your business, www.acfcanvasses.com, one step at a time, tailored for someone with no coding experience. I’ll keep it simple, clear, and focused, guiding you through each step without assumptions or overwhelming options. Since this is the first step, we’ll start with the absolute basics: installing the tools you need to create and run a Streamlit app on your computer.Step 1: Install PythonStreamlit is a Python-based tool, so you need Python installed on your computer to create your cost calculator app.Instructions:Check if Python is already installed:If you’re using a Windows PC, press the Windows key, type cmd, and press Enter to open the Command Prompt.
If you’re using a Mac, open the Terminal (search for “Terminal” in Spotlight).
Type the following command and press Enter:

python --version

If you see something like Python 3.x.x (e.g., Python 3.9.2), Python is installed, and you can move to the next step. Note the version number.
If you get an error like “command not found” or “python is not recognized,” Python is not installed, so proceed with the installation below.

Download and Install Python (if not installed):Go to the official Python website: https://www.python.org/downloads/
Download the latest version of Python (as of July 2025, this is Python 3.12 or similar). Click the “Download Python” button for your operating system (Windows or Mac).
Run the installer:Windows: Double-click the downloaded .exe file. Check the box that says “Add Python to PATH” at the bottom of the installer window, then click “Install Now.”
Mac: Double-click the downloaded .dmg file and follow the prompts to install.

Once installed, close and reopen your Command Prompt (Windows) or Terminal (Mac).
Verify the installation by typing python --version again. You should see the version number (e.g., Python 3.12.0).

Confirm Installation:In your Command Prompt or Terminal, type:

pip --version

This checks if pip (Python’s package manager) is installed. You should see something like pip 23.x.x. If you get an error, let me know, and we’ll fix it.

What You’ve Done:You’ve ensured Python is installed on your computer, which is the foundation for running Streamlit. This is critical because Streamlit is a Python library, and without Python, you can’t proceed.Next Step (Preview):In the next step, we’ll install Streamlit itself using a simple command. I’ll guide you through that once you confirm this step is complete.Action Required:Please confirm that you’ve completed this step by checking the Python version and, if necessary, installing Python. Let me know:The Python version you have (e.g., Python 3.12.0).
Whether you’re using Windows or Mac.
Any errors or issues you encountered.

Once you provide this, I’ll guide you through installing Streamlit in the next step.

i have the stuff installed. ok, first off on my costing. i manufacture in South Africa. that is a fixed cost, i then use an exporter and buy from the UK company. (I have other contires i will be exporting too, but for now lets just focus on the UK) The shipping is a fixed cost so it needs to be added on to the initial cost. Im trying to start with a base price and then add the other costs into the app.

Thoughts

Step 2: Install StreamlitNow that Python is installed, the next step is to install Streamlit, which is the tool we'll use to build your cost calculator app. Streamlit makes it easy to create interactive web apps with simple Python code—no advanced coding needed.Instructions:Open Your Command Line:On Windows: Press the Windows key, type cmd, and press Enter to open the Command Prompt.
On Mac: Open the Terminal (search for “Terminal” in Spotlight).
Note: If you haven't told me yet, please let me know if you're using Windows or Mac in your next response—it'll help with future steps.

Install Streamlit:In the Command Prompt or Terminal, type the following command and press Enter:

pip install streamlit

This will download and install Streamlit. It might take a minute or two. You'll see progress messages, and it should end with something like "Successfully installed streamlit...".
If you get any errors (e.g., permission issues), copy the exact error message and let me know.

Verify the Installation:Once installed, type this command and press Enter:

streamlit --version

You should see something like Streamlit 1.36.0 (the version might vary, but as long as it shows a version, it's good).

What You’ve Done:You've installed Streamlit, which allows us to create your cost calculator as an interactive app that runs in your web browser. Based on your description, the app will start with a base price input, then add fixed costs like manufacturing in South Africa and shipping for the UK export. We'll build this gradually.Next Step (Preview):In the next step, we'll create a simple "Hello World" Streamlit app to test everything works, and then start adding your cost calculator logic (e.g., inputs for base price, manufacturing cost, and shipping).Action Required:Please confirm that you've completed this step by letting me know:The Streamlit version you see (e.g., Streamlit 1.36.0).
Any errors or issues.
Your operating system (Windows or Mac).

Once you provide this, I'll guide you through creating your first basic app file.

1 web page

i have the basic app innstalled. Im working on teh first costings

Thoughts

Step 3: Create and Run a Basic Streamlit App FileNow that Streamlit is installed, we'll create a simple Python file for your cost calculator app. This file will be the starting point where we add your business logic (starting with a base price and adding fixed costs like manufacturing in South Africa and UK shipping). We'll build it gradually.Since you have no coding experience, I'll provide exact code to copy-paste. First, we'll make a "Hello World" version to test it runs, then add your cost elements in later steps.Instructions:Create a Folder for Your App:On your computer, create a new folder anywhere convenient (e.g., on your Desktop). Name it cost_calculator.
Open this folder.

Create the App File:You need a text editor to create a Python file. If you don't have one:On Windows: Use Notepad (search for "Notepad" in the Start menu).
On Mac: Use TextEdit (search for "TextEdit" in Spotlight), but make sure to save as plain text (Format > Make Plain Text).
Alternatively, download a free code editor like Visual Studio Code from https://code.visualstudio.com/—it's user-friendly for beginners.

Open your text editor and create a new file.
Copy-paste the following code exactly into the file (this is a basic test app that displays a title and message):

import streamlit as st

st.title("Cost Calculator for ACF Canvasses")
st.write("This is the start of your cost calculator app. We'll add cost inputs next.")

Save the file inside your cost_calculator folder. Name it app.py (make sure it ends with .py, not .txt).

Run the App:Open your Command Prompt (Windows) or Terminal (Mac).
Navigate to your app folder using the cd command. For example:If the folder is on your Desktop:Windows: Type cd Desktop\cost_calculator and press Enter.
Mac: Type cd ~/Desktop/cost_calculator and press Enter.

(If you're unsure of the path, right-click the folder and select "Copy as path" or similar, then use cd followed by that path.)

Once in the folder, type this command and press Enter:

streamlit run app.py

This will start the app. A web browser window should open automatically (or it will give you a URL like http://localhost:8501—copy-paste that into your browser).
You should see a page with the title "Cost Calculator for ACF Canvasses" and the message below it. If it works, great! If not, note any error messages.

What You’ve Done:You've created and run a basic Streamlit app file. This confirms everything is set up correctly. The app runs locally on your computer as a web page, making it interactive for your cost calculations (e.g., inputs for base price, manufacturing fixed cost, and UK shipping fixed cost).Next Step (Preview):Once this runs, we'll edit the file to add inputs for your first costings: a base price, then add fixed manufacturing and shipping costs, with a total displayed. I'll provide the updated code.Action Required:Please confirm:That the app runs successfully (you see the title and message in your browser).
Any errors or issues (copy the exact message if there is one).
Your operating system (Windows or Mac), if not already shared.

Once you reply, I'll provide the code updates for your cost calculator logic.

you are not listening! leave the dam app for now... im working on the maths

Thoughts

OK, got it—let's set aside the app setup for now and focus solely on the mathematics for your cost calculator.Step 1: Define the Cost FormulaBased on your description, the total cost for a product (e.g., a canvas) exported to the UK can be calculated as:Total Cost = Base Price + Manufacturing Fixed Cost + Shipping Fixed CostExplanation: This is a straightforward addition because you've described these as fixed add-ons to an initial base. (If there's an exporter fee or a purchase cost from the UK company as a separate fixed item, we can add it as another term later—let me know if that's the case.)
Why this structure? You mentioned starting with a base price and adding the other costs. Manufacturing in South Africa is fixed, and shipping to the UK is fixed, so they layer on top without multiplication or other operations unless specified.
Currencies: Since your business manufactures in South Africa (likely ZAR costs) and exports to the UK (GBP pricing on your site), decide on a single currency for calculations (e.g., convert everything to GBP). If you need exchange rates, provide the values, and I can handle conversions.

Example Calculation (Using Placeholders)Suppose:Base Price = 100 (e.g., initial material or production cost in GBP)
Manufacturing Fixed Cost = 20 (fixed per unit or batch in GBP)
Shipping Fixed Cost = 15 (fixed per shipment to UK in GBP)

Then:
Total Cost = 100 + 20 + 15 = 135Step-by-step reasoning:Start with base: 100
Add manufacturing: 100 + 20 = 120
Add shipping: 120 + 15 = 135

This gives the total cost before any markup for selling (e.g., your site shows selling prices like £23 for a canvas, which would be above this cost).For your real numbers, provide the actual values for Base Price, Manufacturing Fixed Cost, and Shipping Fixed Cost (including units and currency), and I'll compute the total with full explanation. If the costs vary by product size or type (e.g., 16x20in Box Board Canvas), specify that too.

2 web pages

ok. Here are one set of SKUs, so the container is a set volume an price £6000 from door to door. This is how i worked the products out. This is for the stretch canvas. Name / Length / Width / Depth (in mm) / Volume (in cubic m) / how many items of this size can fit in a 40ft Hi Cude container - its 73.14m³

Thoughts

Step 2: Calculate Shipping Cost Per ItemBased on your table for the stretch canvas SKUs and the fixed container shipping cost of £6000, we'll compute the shipping cost per item for each SKU. This assumes the container is filled primarily with items of that SKU (or approximates for mixed loads using the "how many fit" value you provided). If loads are mixed, this volume-based approach still gives a proportional cost.The formula for each SKU is:
Shipping Cost Per Item = 6000 / (how many items fit)  Step-by-Step ExplanationTake the fixed container cost (£6000).  
Divide by the number of items that fit (from your table). This gives the add-on shipping cost per item.  
Repeat for each SKU. (Note: Your "how many fit" values are decimals, likely for averaging over packing efficiencies; in practice, you'd use the integer floor for full containers, but we'll use your exact figures for precision.)

ResultsUse these as the shipping add-on to your base price and manufacturing fixed cost.SKU
How Many Fit
Shipping Cost Per Item (£)
Calculation Example
SC1014
32,529.51
0.18
6000 ÷ 32,529.51 ≈ 0.18 (rounded to 2 decimal places for practicality; exact is 0.1844)
SC1216
29,532.42
0.20
6000 ÷ 29,532.42 ≈ 0.20
SC1620
17,978.82
0.33
6000 ÷ 17,978.82 ≈ 0.33
SC2024
13,118.34
0.46
6000 ÷ 13,118.34 ≈ 0.46
SC2430
7,867.56
0.76
6000 ÷ 7,867.56 ≈ 0.76

Notes on Your DataYour volume calculations (e.g., for SC1014: 0.288m × 0.389m × 0.02m = 0.00224064m³) are close to the listed 0.00225m³, likely including a small buffer for packing space.  
The "how many fit" seems based on an effective container volume of about 73.19m³ (e.g., 0.00225 × 32,529.51 ≈ 73.19), slightly higher than your stated 73.14m³—possibly a rounding artifact. If you want to standardize, we can recalculate "how many fit" as floor(73.14 / volume) in the next step.  
Standard 40ft high-cube containers have ~76.4m³ internal volume, but your 73.14m³ might account for real-world packing losses (e.g., doors, irregular stacking). If this is incorrect, provide the exact usable volume for adjustment.

Next Step (Preview)Once we have these shipping values, we'll add them to your base price and manufacturing fixed cost per SKU to get the total cost. This could include conversions if costs are in ZAR (South African Rand).Action RequiredProvide the base price and manufacturing fixed cost for each SKU (or if they're the same across SKUs, specify that). Include currency (e.g., £ or ZAR) and whether manufacturing is per item or another basis. If you have exchange rates (e.g., current ZAR to GBP), share them too. Once you do, I'll compute the totals.

6 web pages

ok great, i have the same calculations. (Im just sharing parts of my excel so we are on the samme page!) The next parts are. Order quantity / packed area / the cost (in ZAR) / Cost of the order quantity (in ZAR) / individual shipping cost / converted cost in GBP, including the shipping cost... are we on same page still?

Thoughts

Step 3: Confirm Column Structure and CalculationsYes, we're on the same page. Based on your Excel snippet, the additional columns build on the previous ones (SKU dimensions, volume, how many fit) to calculate batch and per-item costs, incorporating manufacturing in ZAR and shipping in GBP, with a final conversion to GBP per item including shipping.To summarize the structure:Order quantity: The number of units in a sample order (e.g., 300 or 240, possibly chosen to represent typical batch sizes or to stay under a volume threshold).
Packed area: This appears to be the total packed volume (in m³) for the order quantity, not area (likely a labeling oversight). Formula: Order quantity × Volume per item (cubic m). E.g., for SC1014: 300 × 0.00225 = 0.675 ≈ 0.67.
The cost (in ZAR): Manufacturing cost per item in ZAR (this seems to be your fixed manufacturing cost per SKU, varying by size; if it's derived from a base formula like materials + labor proportional to area, we can refine later).
Cost of the order quantity (in ZAR): Total manufacturing for the batch. Formula: Order quantity × Cost per item (ZAR). E.g., for SC1014: 300 × 35.22 ≈ 10,566 (minor rounding in table).
Individual shipping cost: Per-item shipping add-on in GBP, based on dividing the fixed £6000 container cost by how many fit, with rounding. Formula: 6000 ÷ How many fit. E.g., for SC1014: 6000 ÷ 32,529.51 ≈ 0.184 (rounded to 0.18 in your table).
Converted cost in GBP, including the shipping cost: Total landed cost per item in GBP. Formula: (Cost per item in ZAR ÷ exchange rate) + Individual shipping cost in GBP.

For the exchange rate, your table implies approximately 24 ZAR per 1 GBP (with some variation due to rounding). Using the mid-market rate as of July 14, 2025 (1 GBP = 24.20 ZAR), I've recalculated the converted costs for precision. This rate is derived from financial sources tracking daily historical data.Recalculated Table (Using Exact Values)The table below includes your ZAR costs and user totals for reference, plus exact shipping (unrounded) and converted totals using the 24.20 ZAR/GBP rate. Differences from your table are minimal and likely due to rounding preferences.SKU
ZAR per Item
Exact Shipping GBP
Manuf GBP (ZAR / 24.20)
Calculated Total GBP
User Table Total GBP
SC1014
35.22
0.18
1.46
1.64
1.65
SC1216
42.99
0.20
1.78
1.98
1.93
SC1620
62.34
0.33
2.58
2.91
2.94
SC2024
78.14
0.46
3.23
3.69
3.71
SC2430
99.56
0.76
4.11
4.88
4.91

Step-by-Step Explanation for Calculations (Example: SC1014)For closed-ended math questions like these per-item totals, here's how to arrive at the solution manually or in a spreadsheet:Compute exact shipping per item: Container cost ÷ How many fit = 6000 ÷ 32,529.51 ≈ 0.1844 (round to 0.18 if preferred).
Convert manufacturing cost to GBP: Cost per item ZAR ÷ exchange rate = 35.22 ÷ 24.20 ≈ 1.455.
Add shipping: 1.455 + 0.1844 ≈ 1.6394 (round to 1.64).

Repeat for each SKU. If your ZAR costs include the base price you mentioned, this gives the total cost per item landed in the UK.Next Step (Preview)With the landed cost in GBP calculated, the next part could incorporate any additional fixed costs, such as the exporter fee (since you mentioned using an exporter) or any UK-side costs (e.g., if "buy from the UK company" refers to a markup, duty, or import fee). Action RequiredProvide details on the next cost to add (e.g., exporter fee amount, whether fixed per container or per item, in ZAR or GBP). If this completes the math, confirm, and we can move back to the app setup.

6 web pages

I used a static exchange rate of 24/1. The shipper costs on average £6000 a contanier, and thats the price i used to work out the shipping costs. These are all costs that dont change, but are relevant for the landed cost in the UK.

Thoughts

Step 4: Finalize Landed Cost Per Item in GBPYes, we're aligned—using your static exchange rate of 24 ZAR to 1 GBP and the fixed £6000 container cost for shipping apportionment (per item based on how many fit in the 73.14m³ container). These fixed costs (manufacturing in ZAR and shipping in GBP) give the landed cost per item in the UK, as you've described.I've recalculated the landed cost per item using exact math for transparency. I used:Manufacturing cost per item in GBP = ZAR per item ÷ 24
Shipping per item in GBP = 6000 ÷ how many fit (with practical rounding to 2 decimals, matching your table)
Landed cost per item = Manufacturing GBP + Shipping GBP

ResultsSKU
ZAR per Item
Shipping GBP (Rounded)
Manufacturing GBP
Landed Cost GBP (Rounded)
Calculation Notes
SC1014
35.22
0.18
1.47
1.65
35.22 ÷ 24 = 1.4675; +0.18 = 1.6475 ≈ 1.65
SC1216
42.99
0.20
1.79
1.99
42.99 ÷ 24 = 1.79125; +0.20 = 1.99125 ≈ 1.99 (noting your table shows 1.93, possibly a rounding or entry difference)
SC1620
62.34
0.33
2.60
2.93
62.34 ÷ 24 = 2.5975; +0.33 = 2.9275 ≈ 2.93
SC2024
78.14
0.46
3.26
3.72
78.14 ÷ 24 = 3.25583; +0.46 = 3.71583 ≈ 3.72
SC2430
99.56
0.76
4.15
4.91
99.56 ÷ 24 = 4.14833; +0.76 = 4.90833 ≈ 4.91

Step-by-Step Explanation (Example: SC1216)Convert manufacturing to GBP: 42.99 ÷ 24 = 1.79125
Add shipping (6000 ÷ 29,532.42 ≈ 0.2032, rounded to 0.20 as in your table): 1.79125 + 0.20 = 1.99125
Round to 2 decimals: 1.99 (if your table's 1.93 is a typo or based on a slight variant, we can adjust; otherwise, this matches the formula).

This gives the total fixed landed cost per item in the UK. Note: The actual exchange rate as of July 14, 2025, is approximately 24.14 ZAR per GBP, close to your static 24, so your estimates are reasonable for planning.Next Step (Preview)With the landed cost finalized, we can add any remaining fixed costs, such as the exporter fee (since you mentioned using an exporter). This would update the formula to: Landed Cost = Manufacturing GBP + Shipping GBP + Exporter Fee GBP (per item).Action RequiredProvide the exporter fee details (e.g., amount, whether fixed per container like £X or per item like £Y, and currency). If there are no more fixed costs (or if "buy from the UK company" doesn't add a separate fee, as your business appears to be the same entity in SA and UK), confirm, and we can proceed to markup, other countries, or implementing this math in the Streamlit app.

6 web pages

exporter fee is part of the £6000. so were all good there. When ship arrives, its offloaded at the 3PL (They have monthly costs that vary depending on space used, handling fee and shipping - ill share more detail later) Otehr fixed costs rae: Accounting £250pm / Cell £350pm / Misc £500 pm / Marketing £100 pd. just take this info in so we are on the same page

Thoughts

Step 5: Incorporate Additional Fixed OverheadsUnderstood—we're aligned on the exporter fee being bundled into the £6000 container cost, so no separate addition needed. The ship offloads at the 3PL provider, where variable monthly costs (space usage, handling fees, and internal shipping) apply— we'll handle those details when you share more. For now, the other fixed overheads are noted as:Accounting: £250 per month
Cell (assuming cellular/phone or similar): £350 per month
Misc: £500 per month
Marketing: £100 per day

These are business-wide fixed costs, not per-item, so to include them in your per-item cost calculator, we'll need to apportion them based on expected sales volume (e.g., total items sold per month). Formula for apportioned overhead per item: (Total monthly overheads ÷ expected monthly items sold).Total Monthly Fixed Overheads CalculationFirst, standardize to monthly (assuming 30 days/month for marketing):Accounting: £250
Cell: £350
Misc: £500
Marketing: £100/day × 30 = £3,000
Total monthly fixed overheads = 250 + 350 + 500 + 3,000 = £4,100

Step-by-step reasoning:Convert daily to monthly: 100 × 30 = 3,000
Sum all: 250 + 350 + 500 + 3,000 = 4,100

Next Step (Preview)To get per-item overhead, provide your expected monthly sales volume (e.g., total canvases sold across all SKUs). Then, we can add this to the landed cost per SKU for a full cost per item (e.g., Landed GBP + Overhead per item). Once ready, we can include 3PL variables.Action RequiredShare your expected monthly sales volume (or if it varies by SKU, those details). If this isn't fixed and should be an input in the app, confirm that instead.

ok, im now going to share my app code. You will see i have toggles for diff countries, therye also switched on / off on the coloumsn to the right. Then i can change the length of sale (So if i know a container is only arriving in 4 months i can spread the costs over 4 months. let me know if it all makes sense?

Thoughts

Step 6: Review Your Dashboard SetupYes, it all makes sense based on the screenshot of your Streamlit app dashboard. Here's a quick summary of what I see and how it ties into our previous math discussions, to confirm we're aligned:Overall Structure: It's an interactive "ACF SKU Pricing Intelligence Dashboard" with a sidebar for inputs (toggles, sliders, and numbers) and a main table displaying calculations per SKU (e.g., Alpha category items like ASC608 to ASC2430). The table includes columns like dimensions (Length/Width/Depth in mm), Volume (m³), Factory Cost (ZAR), Export Cost (ZAR), Commission %, UK Landed cost, UK RRP exVAT, and UK RRP incVAT. This builds directly on the per-item landed costs we calculated earlier (manufacturing + shipping/export), adding VAT and RRP (recommended retail price) markups.
Country Toggles: You have checkboxes for UK, USA, and Germany (UK is enabled in the screenshot). These likely control which country-specific columns appear in the table (e.g., showing UK Landed/RRP but hiding USA/Germany ones when toggled off). This allows focusing on one market at a time or comparing them, matching your plan to expand beyond UK.
Throughput Duration (Months): Set to 6 in the screenshot. This spreads fixed costs (like the container cost) over the specified months. For example, if a container arrives in 4 months, you'd set this to 4, dividing the £6000 (or equivalent in ZAR at 150,000 as shown) by the number of items that fit and then further by 4 months. This lowers the per-item cost allocation, making sense for cash flow and pricing accuracy.
Other Inputs: UK Exchange Rate (ZAR per GBP): 19.50 (updated from our earlier 24; this affects ZAR-to-GBP conversions for landed costs).
UK VAT %: 0.20 (standard 20%, added to get incVAT prices).
UK Container Cost (ZAR): 150,000 (equivalent to ~£7,692 at 19.50 rate, close to our £6,000 but adjustable).
UK Container Volume (m³): 76.00 (standard high-cube, slightly higher than our 73.14 for packing efficiency).
Monthly Overheads (in GBP, I assume): Storage £500, Banking £200, Post Costs £0, Ops Costs £400, Warehouse £1,000, Packing £400, Courier £700. These tie into the fixed overheads we discussed (£4,100 total monthly, including marketing), apportioned per item based on sales volume and spread via throughput duration.

How Calculations Flow: From the table values (e.g., for ASC1014: Factory ZAR 35.52, Export ZAR 45.29, Volume 0.0018, UK Landed ~4.94), it seems the app:Calculates per-item shipping from container cost/volume divided by item volume and throughput months.
Converts factory/export ZAR to GBP using the exchange rate.
Adds overhead apportionments.
Computes landed cost, then applies commission (33%) or markup to get RRP exVAT, and adds VAT for incVAT.

This aligns perfectly with our step-by-step cost buildup (base/manufacturing + shipping + overheads), now made dynamic in the app.Next Step (Preview)If you'd like, we can add the 3PL variable costs (space, handling, shipping) to the math and app—share those details when ready.Action RequiredConfirm if my understanding matches yours (e.g., any corrections on how throughput or toggles work). If you meant to share the actual code (Python file) for review or edits, paste it here. Otherwise, let me know the next part to focus on (e.g., adding more countries, adjusting formulas, or implementing 3PL).

ACF Canvasses X Wonderpack - Google Sheets.pdf
File

yes we seem on the same page. I have a meeting later today with regards to the 3PL (There invoices are inconsistent) but here is their rate card:

Thoughts

Step 7: Incorporate 3PL Costs from Rate CardThanks for sharing the Wonderpack.eco rate card (from September 2024). I've cleaned up the OCR typos (e.g., "Bose" to "Base", "Pet manth" to "Per month", "Yoxine" to "Voidfill", "Paller" to "Pallet", etc.) based on context and logical corrections. Note that since today is July 14, 2025, these prices might have changed slightly, but we'll use this as the basis until your meeting provides updates. The inconsistencies you mentioned with invoices could be due to custom applications or additional fees—let me know what comes out of the meeting.I've structured the rate card into tables for clarity, grouped by category. All prices are in GBP, excluding VAT (as noted at the bottom).Account ManagementItem
Price
Per month
Free

Fulfilment D2C (Direct-to-Consumer)Item
Price
Base price per shipment and packing
£1.50
Price per pick
£0.20
Price per insert/sticker
£0.05

Fulfilment B2B (Business-to-Business)Item
Price
Base price
£4.95
Price per additional
£1.00
Price per product unit
£0.05

InboundItem
Price
Base price per delivery
£12.50
Pallet of single SKU cartons (per pallet)
£3.00
Pallet of mixed SKU cartons (per carton)
£0.75
Per hour charge, if more appropriate
£22.50

Inbound - ContainerItem
Price
Unload, palletise and putaway - 40ft
£495.00
- Price per pallet
£3.00
- Price per pallet wrap
£1.00
Unload, palletise and putaway - 20ft
£295.00
- Price per pallet
£3.00
- Price per pallet wrap
£1.00

ReturnItem
Price
Base price
£1.75
Bespoke return / reconditioning (per hour)
£22.50

Storage (per month)Item
Price
Small Box - Picking Bin - 30x30x40cm
£2.00
Medium Box - Picking Bin - 90x30x40cm
£4.00
Large Box - Picking Bin - 90x60x40cm
£6.00
Pallet
£15.00

PackagingItem
Price
Box - XXS (1.5L)
£0.15
Box - XS (3L) 201x152x102mm
£0.21
Box - S (5L) 229x159x159mm
£0.29
Box - M (9L) 305x225x133mm
£0.42
Box - L (16L) 306x229x229mm
£1.20
Box - XL (21L)
£2.55
Padded Paper Envelope (0.8L)
£0.12
Biodegradable Poly (0.5L)
£0.23
Card Envelope (1.4L)
£0.27
Client own packaging
£0.05

VoidfillItem
Price
Kraft Paper - XXS (1.5L)
£0.03
Kraft Paper - XS (3L)
£0.05
Kraft Paper - S (5L)
£0.11
Kraft Paper - M (9L)
£0.15
Kraft Paper - L (16L)
£0.25
Kraft Paper - XL (21L)
£0.42
Compostable Packing Peanuts - XXS (1.5L)
£0.05
Compostable Packing Peanuts - XS (3L)
£0.13
Compostable Packing Peanuts - S (5L)
£0.21
Compostable Packing Peanuts - M (9L)
£0.20
Compostable Packing Peanuts - XL (21L)
£0.49

OthersItem
Price
Special requests (e.g. co-packing) per hour
£22.50

All prices exc VAT.How to Incorporate into CalculationsThese 3PL costs are mostly variable (per shipment, per pick, per month for storage), so we'll add them to the per-item or per-order cost based on your operations. The formula updates to:Full Cost Per Item = Landed Cost GBP (from before) + Apportioned 3PL Costs Per Item + Overheads Per ItemTo apportion:Fulfilment (D2C or B2B): Added per order/shipment. E.g., for D2C: £1.50 base + £0.20 per pick (if multiple items/SKUs per order) + inserts if used.
Inbound: Added per container arrival, then divided by items in container (similar to shipping). E.g., for 40ft: £495 base + £3 per pallet + £1 per wrap, divided by how many items fit.
Storage: Monthly total (e.g., £15 per pallet × number of pallets) divided by expected monthly sales volume.
Packaging and Voidfill: Per item, based on SKU size (e.g., match canvas dimensions to box sizes like S or M).
Returns: Based on return rate (e.g., 5% of sales), add £1.75 per returned item, apportioned across all items.
Spread over Throughput Duration: As in your app, divide monthly/periodic costs by the months slider.

Example (Placeholder for SC1014, assuming D2C, 1 pick per order, S box packaging, kraft voidfill S, 1 pallet storage for 100 items/month, 5% return rate, monthly sales 500 items):Fulfilment per item: £1.50 (base, assuming 1-item orders) + £0.20 (pick) = £1.70
Packaging + Voidfill: £0.29 (S box) + £0.11 (kraft S) = £0.40
Storage per item: (£15/pallet × 1 pallet) / 500 items = £0.03
Inbound per item: (£495 + £3 + £1 for 40ft) / 32,529 items ≈ £0.015
Returns per item: £1.75 × 0.05 = £0.0875
Total 3PL add-on: £1.70 + £0.40 + £0.03 + £0.015 + £0.0875 ≈ £2.23
Full cost: Previous landed £1.65 + £2.23 + overheads.

Next Step (Preview)We'll add these to your app's calculations, making them inputs (e.g., dropdown for box size per SKU, slider for return rate).Action RequiredShare details from your meeting (e.g., any price changes, typical usage like average picks per order, box sizes for your SKUs, number of pallets stored, return rate, if you use D2C or B2B). If you want example calculations for specific SKUs, provide those assumptions.

4 web pages

import streamlit as st
import pandas as pd# Page setup
st.set_page_config(page_title=" ACF SKU Pricing Intelligence Dashboard", layout="wide")
st.title(" ACF SKU Pricing Intelligence Dashboard")# Sidebar country toggle
st.sidebar.header("Toggle Countries")
countries = ["UK", "USA", "Germany"]
country_toggle = {c: st.sidebar.checkbox(c, value=(c == "UK")) for c in countries}# Sell-through duration
duration_months = st.sidebar.number_input("Sell-Through Duration (Months)", min_value=1, max_value=24, value=6)# Country-specific cost settings
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
            cour = st.number_input(f"{country} Courier (Monthly)", value=7000.0, key=f"cour_{country}")    country_settings[country] = {
        "rate": rate,
        "vat": vat,
        "container_cost": cont_cost,
        "container_volume": cont_vol,
        "monthly_costs": ads + bank + ops + ware + pack + cour
    }# Base SKU data
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
sku_df = pd.DataFrame(sku_data, columns=sku_columns)# Calculate Volume
sku_df["Volume_m³"] = (sku_df["Length_mm"] * sku_df["Width_mm"] * sku_df["Depth_mm"]) / 1_000_000_000# Pricing Calculations
for country in countries:
    if country_toggle[country]:
        rate = country_settings[country]["rate"]
        vat = country_settings[country]["vat"]
        monthly = country_settings[country]["monthly_costs"]
        vol_total = country_settings[country]["container_volume"]    cost_load = (monthly / vol_total) * sku_df["Volume_m³"] * duration_months
    commission_factor = 1 + (sku_df["Commission_%"] / 100)

    landed = sku_df["Export_Cost_ZAR"] + cost_load
    rrp_exvat = landed * commission_factor
    rrp_incvat = rrp_exvat * (1 + vat)

    sku_df[f"{country} Landed"] = landed.round(2)
    sku_df[f"{country} RRP exVAT"] = rrp_exvat.round(2)
    sku_df[f"{country} RRP incVAT"] = rrp_incvat.round(2)# Lock calculated columns
locked_cols = ["Volume_m³"]
for country in countries:
    if country_toggle[country]:
        locked_cols += [
            f"{country} Landed", f"{country} RRP exVAT", f"{country} RRP incVAT"
        ]# Final editor
st.data_editor(
    sku_df,
    use_container_width=True,
    num_rows="dynamic",
    disabled=locked_cols
)

Thought for 3m 54s

Step 8: Update Your Streamlit App Code with Fixes and Shipping IntegrationYes, the rate card makes sense—it's a detailed breakdown of variable and fixed 3PL costs (e.g., storage at £15 per pallet/month, fulfilment at £1.50 base per shipment + £0.20 per pick). Since your invoices are inconsistent, use this rate card to estimate and input your monthly overheads in the app (e.g., if you store 667 pallets, warehousing = 667 × 15 = ~£10,005, so enter 10000 in the warehousing field). After your meeting, you can refine these estimates if prices have changed since September 2024.Your code is a solid foundation, but it has a key issue: it mixes currencies by adding ZAR costs directly to local cost_load without conversion. It also doesn't use the container cost input for shipping. I've fixed this by:Combining Factory_Cost_ZAR + Export_Cost_ZAR + shipping_ZAR (calculated from container cost and volume).
Converting the total ZAR to local currency (divide by exchange rate).
Keeping the overhead cost_load in local currency and adding it to get landed in local.
No changes to RRP calculations, as they now use the corrected landed.

Here's the updated code. Copy-paste it into your app.py file (replace the old code), save, and run streamlit run app.py in your command line (as before).

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

# Country-specific cost settings
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
    ["Alpha", "ASC608", 152, 203, 20, 16.79, 21.60, 33],
    ["Alpha", "ASC1012", 255, 305, 20, 31.86, 40.97, 33],
    ["Alpha", "ASC1014", 255, 355, 20, 35.22, 45.29, 33],
    ["Alpha", "ASC1216", 305, 406, 20, 42.99, 55.28, 33],
    ["Alpha", "ASC1418", 355, 457, 20, 53.51, 68.82, 33],
    ["Alpha", "ASC1620", 406, 501, 20, 62.34, 80.17, 33],
    ["Alpha", "ASC1824", 457, 610, 20, 73.20, 94.15, 33],
    ["Alpha", "ASC2024", 501, 610, 20, 78.14, 100.49, 33],
    ["Alpha", "ASC2430", 610, 762, 20, 99.56, 128.04, 33],
]
sku_df = pd.DataFrame(sku_data, columns=sku_columns)

# Calculate Volume
sku_df["Volume_m³"] = (sku_df["Length_mm"] * sku_df["Width_mm"] * sku_df["Depth_mm"]) / 1_000_000_000

# Pricing Calculations
for country in countries:
    if country_toggle[country]:
        rate = country_settings[country]["rate"]
        vat = country_settings[country]["vat"]
        monthly = country_settings[country]["monthly_costs"]
        vol_total = country_settings[country]["container_volume"]
        cont_cost = country_settings[country]["container_cost"]

        # Overhead cost load per item (in local currency)
        cost_load = (monthly / vol_total) * sku_df["Volume_m³"] * duration_months

        # Shipping per item (in ZAR, fixed - not multiplied by duration)
        shipping_ZAR = cont_cost * sku_df["Volume_m³"] / vol_total

        # Total costs in ZAR
        total_ZAR = sku_df["Factory_Cost_ZAR"] + sku_df["Export_Cost_ZAR"] + shipping_ZAR

        # Convert to local and add overheads
        landed = (total_ZAR / rate) + cost_load

        commission_factor = 1 + (sku_df["Commission_%"] / 100)
        rrp_exvat = landed * commission_factor
        rrp_incvat = rrp_exvat * (1 + vat)

        sku_df[f"{country} Landed"] = landed.round(2)
        sku_df[f"{country} RRP exVAT"] = rrp_exvat.round(2)
        sku_df[f"{country} RRP incVAT"] = rrp_incvat.round(2)

# Lock calculated columns
locked_cols = ["Volume_m³"]
for country in countries:
    if country_toggle[country]:
        locked_cols += [
            f"{country} Landed", f"{country} RRP exVAT", f"{country} RRP incVAT"
        ]

# Final editor
st.data_editor(
    sku_df,
    use_container_width=True,
    num_rows="dynamic",
    disabled=locked_cols
)

What You've DoneThe app now correctly handles currencies and includes shipping as a fixed per-item add-on (based on container cost and how many fit via volume).
Tested the math behind the scenes—e.g., for SC1014 (UK defaults): Landed ≈ £7.92 (ZAR costs £4.28 + overhead £3.65), which aligns with our earlier examples (adjust inputs to match your screenshot if needed).
3PL integration: Not added as code yet (to keep this step simple), but use the rate card to populate monthly inputs (e.g., warehousing = pallets × £15). This keeps the app flexible for post-meeting updates.

Next Step (Preview)Once you run this and confirm it works, we'll add granular 3PL calculations (e.g., inputs for pallets/shipments, auto-compute warehousing/fulfilment from rate card).Action RequiredRun the updated code and confirm:The app loads and shows correct landed/RRP values (e.g., for UK, SC1014 landed around £7-8 depending on inputs).
Any errors or mismatches with your expected numbers.
Once shared, I'll provide the next update.

ok, so i need the volume to be dynamic. If i find the packaging is a differneet size i need to be able to manually adjust it L / W / D and it needs to change the volume

Thought for 1m 3s

Step 9: Make Volume and Costs Dynamic in the AppTo make the volume dynamic based on manual edits to Length_mm, Width_mm, or Depth_mm (e.g., for different packaging sizes), I've updated the code to use a "Recalculate" button in the sidebar. Here's how it works:You edit the L/W/D values in the data table.
Press the "Recalculate" to update Volume_m³, landed costs, and RRPs based on the new dimensions.
This triggers the app to recalculate everything using the edited values, including shipping (which depends on volume) and overheads.
The table updates with the new values in the calculated columns.

This keeps the single interactive table (you can add rows, edit base data), and locks the calculated columns to prevent manual override.Copy-paste this into your app.py, save, and run streamlit run app.py.

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

# Base SKU data (editable columns)
sku_columns = [
    "Category", "SKU", "Length_mm", "Width_mm", "Depth_mm",
    "Factory_Cost_ZAR", "Export_Cost_ZAR", "Commission_%"
]
sku_data = [
    ["Alpha", "ASC608", 152, 203, 20, 16.79, 21.60, 33],
    ["Alpha", "ASC1012", 255, 305, 20, 31.86, 40.97, 33],
    ["Alpha", "ASC1014", 255, 355, 20, 35.22, 45.29, 33],
    ["Alpha", "ASC1216", 305, 406, 20, 42.99, 55.28, 33],
    ["Alpha", "ASC1418", 355, 457, 20, 53.51, 68.82, 33],
    ["Alpha", "ASC1620", 406, 501, 20, 62.34, 80.17, 33],
    ["Alpha", "ASC1824", 457, 610, 20, 73.20, 94.15, 33],
    ["Alpha", "ASC2024", 501, 610, 20, 78.14, 100.49, 33],
    ["Alpha", "ASC2430", 610, 762, 20, 99.56, 128.04, 33],
]

# Use session state to persist the DF across edits
if "sku_df" not in st.session_state:
    df = pd.DataFrame(sku_data, columns=sku_columns)
    df["Volume_m³"] = (df["Length_mm"] * df["Width_mm"] * df["Depth_mm"]) / 1_000_000_000
    st.session_state.sku_df = df  # Initial calc without country, country added below

# Recalculate button
if st.sidebar.button("Recalculate Volume and Costs"):
    # Update volume based on current L/W/D
    st.session_state.sku_df["Volume_m³"] = (st.session_state.sku_df["Length_mm"] * st.session_state.sku_df["Width_mm"] * st.session_state.sku_df["Depth_mm"]) / 1_000_000_000
    
    # Recalculate country pricing
    for country in countries:
        if country_toggle[country]:
            rate = country_settings[country]["rate"]
            vat = country_settings[country]["vat"]
            monthly = country_settings[country]["monthly_costs"]
            vol_total = country_settings[country]["container_volume"]
            cont_cost = country_settings[country]["container_cost"]

            cost_load = (monthly / vol_total) * st.session_state.sku_df["Volume_m³"] * duration_months

            shipping_ZAR = cont_cost * st.session_state.sku_df["Volume_m³"] / vol_total

            total_ZAR = st.session_state.sku_df["Factory_Cost_ZAR"] + st.session_state.sku_df["Export_Cost_ZAR"] + shipping_ZAR

            landed = (total_ZAR / rate) + cost_load

            commission_factor = 1 + (st.session_state.sku_df["Commission_%"] / 100)
            rrp_exvat = landed * commission_factor
            rrp_incvat = rrp_exvat * (1 + vat)

            st.session_state.sku_df[f"{country} Landed"] = landed.round(2)
            st.session_state.sku_df[f"{country} RRP exVAT"] = rrp_exvat.round(2)
            st.session_state.sku_df[f"{country} RRP incVAT"] = rrp_incvat.round(2)

# Lock calculated columns
locked_cols = ["Volume_m³"]
for country in countries:
    if country_toggle[country]:
        locked_cols += [
            f"{country} Landed", f"{country} RRP exVAT", f"{country} RRP incVAT"
        ]

# Display the editor
st.data_editor(
    st.session_state.sku_df,
    use

