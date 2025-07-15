from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Initialize Edge WebDriver
driver = webdriver.Edge()

# Target base URL (first page)
base_url = "https://sourcing.alibaba.com/rfq/rfq_search_list.htm?page={}"

all_data = []

# Loop through pages 1 to 5
for page in range(1, 6):
    print(f"[✓] Scraping Page {page}...")
    driver.get(base_url.format(page))
    time.sleep(5)

    # Scroll to load dynamic content
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    rfq_items = driver.find_elements(By.CSS_SELECTOR, ".alife-bc-brh-rfq-list__item")

    for item in rfq_items:
        try:
            title = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__subject-link").text.strip()
        except:
            title = ""

        try:
            description = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__detail").text.strip()
        except:
            description = ""

        try:
            quantity = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__quantity-num").text.strip()
            quantity_unit = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__quantity span:last-child").text.strip()
        except:
            quantity = quantity_unit = ""

        try:
            country = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__country").text.split(":")[-1].strip()
        except:
            country = ""

        try:
            quotes_left = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__quote-left span").text.strip()
        except:
            quotes_left = ""

        try:
            date_posted = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__publishtime").text.split(":")[-1].strip()
        except:
            date_posted = ""

        try:
            buyer_name = item.find_element(By.CSS_SELECTOR, ".avatar .text").text.strip()
        except:
            buyer_name = ""

        try:
            buyer_image = item.find_element(By.CSS_SELECTOR, ".avatar img").get_attribute("src")
        except:
            buyer_image = ""

        try:
            product_image = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__prod-img img").get_attribute("src")
        except:
            product_image = ""

        try:
            inquiry_url = item.find_element(By.CSS_SELECTOR, ".brh-rfq-item__subject-link").get_attribute("href")
        except:
            inquiry_url = ""

        all_data.append({
            "RFQ Title": title,
            "Description": description,
            "Quantity": quantity,
            "Unit": quantity_unit,
            "Country": country,
            "Quotes Left": quotes_left,
            "Date Posted": date_posted,
            "Buyer Name": buyer_name,
            "Buyer Image": buyer_image,
            "Product Image": product_image,
            "Inquiry URL": "https:" + inquiry_url if inquiry_url.startswith("//") else inquiry_url
        })

# Save all scraped data to CSV
df = pd.DataFrame(all_data)
df.to_csv("alibaba_rfqs_first_5_pages.csv", index=False)
print(f"[✓] Scraped {len(all_data)} RFQs across 5 pages. Data saved to alibaba_rfqs_first_5_pages.csv")

# Close browser
driver.quit()
