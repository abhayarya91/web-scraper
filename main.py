import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Function to scrape product prices, images, reviews
def scrape_website():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL!")
        return

    try:
        driver = webdriver.Chrome()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        # Example: Extract product name, price, and images
        product_info = soup.find('h1')  # Modify based on website's structure
        price_info = soup.find('span', class_='price')  # Example price class
        img_tag = soup.find('img', class_='product-image')  # Example image class

        # Scrape text information
        product_name = product_info.text if product_info else "Not Found"
        product_price = price_info.text if price_info else "Price Not Found"
        
        # Scrape image
        if img_tag and img_tag['src']:
            image_url = img_tag['src']
            response = requests.get(image_url)
            img_data = Image.open(BytesIO(response.content))
            img_data = img_data.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img_data)
            img_label.config(image=img)
            img_label.image = img

        # Update output text with the scraped data
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Product Name: {product_name}\n")
        output_text.insert(tk.END, f"Price: {product_price}\n")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to scrape the website: {str(e)}")


# Main Tkinter Window
root = tk.Tk()
root.title("Web Scraper Tool")
root.geometry("600x500")
root.configure(bg='#34495E')

# Styling
style = ttk.Style()
style.configure("TLabel", background="#34495E", foreground="white")
style.configure("TButton", background="#2ECC71", foreground="white")

# URL Entry Field
label_url = ttk.Label(root, text="Enter URL:", font=("Arial", 12, 'bold'))
label_url.pack(pady=10)
entry_url = ttk.Entry(root, width=50, font=("Arial", 12))
entry_url.pack(pady=10)

# Scrape Button
btn_scrape = ttk.Button(root, text="Scrape", command=scrape_website)
btn_scrape.pack(pady=20)

# Image Display Area
img_label = ttk.Label(root, text="Image will be displayed here", background='#34495E', font=("Arial", 10))
img_label.pack(pady=20)

# Output Text Area
output_text = scrolledtext.ScrolledText(root, width=70, height=10, wrap=tk.WORD, font=("Arial", 12))
output_text.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
