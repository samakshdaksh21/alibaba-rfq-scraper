Alibaba RFQ Scraper Assignment

Author: Samaksh Daksh  
Language: Python  
Output Format: CSV  
Target: Scrape first 5 pages of RFQs from Alibaba

Description:
This script uses Selenium to scrape RFQ (Request for Quotation) data from the Alibaba Sourcing platform.

It extracts fields like:
- RFQ ID
- Title
- Buyer Name & Country
- Quantity Required
- Inquiry Time & Date
- Email Confirmation Status
- Buyer Preferences (e.g., Experienced Buyer, Completed Order via RFQ, etc.)
- RFQ URL
- Scraping Timestamp

How to Run:

1. Install dependencies:
pip install -r requirements.txt

2. Run the script:
python alibaba_scraper.py

3. Output:
The file `alibaba_rfqs_first_5_pages.csv` will be created in the same directory.

Notes:
------
- The scraper uses Selenium with Microsoft Edge (`msedgedriver`).
- It navigates through 5 pages using URL modification (pagination).
- `cookies.json` can be added for session login (if scraping private data).
- No "Next" button is used, as Alibaba pages are navigated using query strings.