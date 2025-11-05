# AIML_Data_Mining_Project
AIML_Data_Mining_Project
AI Data Product Scraper – All Authorized Websites
🔍 Overview

The AI Data Product Scraper is a Python desktop application built using Tkinter and SerpApi that allows users to search products on Google Shopping and automatically find the best deals from authorized online retailers.

It displays product name, price, rating, source website, and direct purchase links — all inside a clean and interactive GUI.

🚀 Features

✅ Smart Search – Fetches product data from Google Shopping using SerpApi.
✅ Clean Results – Filters and displays verified links from trusted sites (Amazon, Flipkart, etc.).
✅ Best Deal Detection – Sorts products by lowest price and highest rating.
✅ Interactive GUI – Simple and responsive interface built with Tkinter.
✅ Clickable Links – Open product pages directly in your web browser.
✅ Error Handling – Gracefully handles missing data or API issues.

🧩 Tech Stack

Language: Python 3.x
GUI Library: Tkinter
API: SerpApi (Google Shopping Engine)

Other Libraries:
tkinter and ttk (for GUI)
webbrowser (to open links)
serpapi (for Google Shopping search)

⚙️ Setup Instructions
Install Dependencies
pip install serpapi


Add Your SerpApi Key
Replace the placeholder API key in the script:
SERPAPI_API_KEY = "your_api_key_here"
You can get a free key from https://serpapi.com
.

Run the Application

python product_scraper.py


Search for Any Product!
Enter a product name (like “iPhone 15” or “Laptop”) and click 🔍 Search.
The table will show the top results with prices, ratings, and sources.

🧠 How It Works

Takes product input from user.
Uses SerpApi to fetch results from Google Shopping.
Cleans and parses data (price, rating, source, and link).
Sorts by lowest price and highest rating.
Displays the top 10 best options in a Tkinter table.
Allows the user to click on the product link to open it in their browser.

📸 UI Preview
(You can add a screenshot here once you take one)
Example:

+--------------------------------------------------------------+
| AI Data Product Scraper - All Authorized Websites            |
+--------------------------------------------------------------+
| Enter Product Name: [ Laptop                  ] [ Search 🔍 ] |
| Best Price: ₹54999 | Rating: 4.5/5 | Source: Amazon          |
|--------------------------------------------------------------|
| ID | Product | Price | Rating | Source | Link                |
|--------------------------------------------------------------|
| 1  | Dell Inspiron ... | ₹54999 | 4.5 | Amazon | open link → |
+--------------------------------------------------------------+

⚡ Example Queries
“Bluetooth headphones”
“Samsung Galaxy S24”
“Gaming laptop 16GB RAM”
“Electric kettle”
