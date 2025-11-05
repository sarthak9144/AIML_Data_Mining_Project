import tkinter as tk
from tkinter import ttk, messagebox
from serpapi import GoogleSearch
import webbrowser

# 🔑 Replace with your valid SerpApi key
SERPAPI_API_KEY = "5c67846972a791074613a9dbc027147408e755cdebfc8db3eea8ac57c193d31c"

# --- Search Google Shopping ---
def search_google_shopping(product_name):
    params = {
        "engine": "google_shopping",
        "q": product_name,
        "hl": "en",
        "gl": "in",
        "api_key": SERPAPI_API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if "error" in results:
        messagebox.showerror("API Error", results["error"])
        return []

    return results.get("shopping_results", [])

# --- Clean link safely ---
def clean_product_link(link):
    """Ensure link is a valid external URL (not a Google redirect)."""
    if not link:
        return None
    if link.startswith("https://www.google.com"):
        # Extract the real redirect target if possible
        import urllib.parse as up
        parsed = up.urlparse(link)
        query = up.parse_qs(parsed.query)
        real_link = query.get("url", [None])[0]
        if real_link:
            return real_link
    return link

# --- Process and sort products ---
def find_best_product(product_name):
    product_data = search_google_shopping(product_name)
    product_details = []

    for product in product_data:
        try:
            source = product.get('source', 'Unknown')

            # Price extraction
            price_str = product.get('price', '0')
            price = float(
                price_str.replace('₹', '').replace('$', '').replace(',', '').strip()
            ) if price_str else 0.0

            # Rating & reviews
            rating = float(product.get('rating', 0.0))
            reviews = product.get('reviews', 'No reviews')

            # Clean working link (priority order)
            link = (
                clean_product_link(product.get('product_link'))
                or clean_product_link(product.get('link'))
                or clean_product_link(product.get('serpapi_link'))
                or "No link"
            )

            product_details.append({
                'title': product.get('title', 'No title'),
                'price': price,
                'rating': rating,
                'link': link,
                'source': source,
                'reviews': reviews
            })
        except Exception as e:
            print("Error parsing product:", e)
            continue

    # Sort by price ascending, rating descending
    sorted_products = sorted(product_details, key=lambda x: (x['price'], -x['rating']))
    return sorted_products

# --- Search button handler ---
def on_scrape():
    product_name = url_entry.get().strip()
    if not product_name:
        messagebox.showerror("Input Error", "Please enter a product name.")
        return

    best_products = find_best_product(product_name)
    if not best_products:
        messagebox.showinfo("No Products Found", "No products found for this query.")
        return

    # Update best price label
    best_product = best_products[0]
    price_label.config(
        text=f"Best Price: ₹{best_product['price']} | Rating: {best_product['rating']}/5 | Source: {best_product['source']}"
    )

    # Clear table
    for row in pos_review_tree.get_children():
        pos_review_tree.delete(row)

    # Insert top 10 products
    for idx, product in enumerate(best_products[:10], start=1):
        display_link = product['link'] if len(product['link']) < 50 else product['link'][:47] + "..."
        pos_review_tree.insert(
            "", "end",
            values=(idx, product['title'], f"₹{product['price']}", product['rating'], product['source'], display_link),
            tags=("clickable",)
        )

# --- Click link handler ---
def on_tree_click(event):
    item = pos_review_tree.identify_row(event.y)
    col = pos_review_tree.identify_column(event.x)

    if not item:
        return

    # Open link only if "Link" column (#6) is clicked
    if col == "#6":
        data = pos_review_tree.item(item, "values")
        if len(data) >= 6:
            link = data[5]
            if link and link != "No link":
                webbrowser.open(link)

# --- GUI Setup ---
root = tk.Tk()
root.title("🧠 AI Data Product Scraper - All Authorized Websites")
root.geometry("1000x500")

title_label = tk.Label(root, text="AI Data Product Scraper - All Authorized Websites", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

url_label = tk.Label(root, text="Enter Product Name:")
url_label.pack()
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

scrape_button = tk.Button(root, text="🔍 Search", command=on_scrape,
                          bg="#0078D7", fg="white", font=("Arial", 10, "bold"))
scrape_button.pack(pady=10)

price_label = tk.Label(root, text="Best Price: -", font=("Arial", 12))
price_label.pack(pady=10)

# Table frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

columns = ("ID", "Product", "Price", "Rating", "Source", "Link")
pos_review_tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)

for col in columns:
    pos_review_tree.heading(col, text=col)
    pos_review_tree.column(col, anchor="w")

pos_review_tree.column("ID", width=50, anchor="center")
pos_review_tree.column("Product", width=300)
pos_review_tree.column("Price", width=100)
pos_review_tree.column("Rating", width=80)
pos_review_tree.column("Source", width=120)
pos_review_tree.column("Link", width=300)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=pos_review_tree.yview)
pos_review_tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
pos_review_tree.pack(fill="both", expand=True)

# Bind click on "Link" column
pos_review_tree.bind("<Button-1>", on_tree_click)

root.mainloop()
