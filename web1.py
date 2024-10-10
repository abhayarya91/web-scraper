import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
import requests

# Function to initialize Selenium WebDriver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Optional: Run in headless mode (no browser UI)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Function to scrape data from a URL
def scrape_data(url):
    driver = init_driver()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Example of scraping product names and prices (modify as per your requirement)
    product_info = []
    
    # Example selectors for Flipkart (these would need to change depending on the website structure)
    products = soup.find_all('a', {'class': '_1fQZEK'})  # Flipkart-specific class for products
    
    for product in products:
        name = product.find('div', {'class': '_4rR01T'})  # Flipkart product name class
        price = product.find('div', {'class': '_30jeq3 _1_WHN1'})  # Flipkart price class
        
        if name and price:
            product_info.append(f"Product: {name.text.strip()}, Price: {price.text.strip()}")
    
    driver.quit()
    return product_info

# Function to display scraped data in the UI
def display_data(data):
    result_box.delete(1.0, tk.END)
    if data:
        for item in data:
            result_box.insert(tk.END, item + '\n')
    else:
        result_box.insert(tk.END, "No data found or unable to parse the page.\n")

# UI Setup using Tkinter
root = tk.Tk()
root.title("Web Scraper Tool")
root.geometry("700x500")
root.configure(bg='#FFFAFA')

# Label for URL input
url_label = ttk.Label(root, text="Enter URL:", background='#FFFAFA')
url_label.pack(pady=10)

# Entry widget for URL
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=10)

# Scrape button
def on_scrape():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return
    try:
        data = scrape_data(url)
        display_data(data)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to scrape data: {e}")

scrape_button = ttk.Button(root, text="Scrape", command=on_scrape)
scrape_button.pack(pady=10)

# ScrolledText widget to display results
result_box = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD, bg='#F0F8FF')
result_box.pack(pady=10)

# Exit button
exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
