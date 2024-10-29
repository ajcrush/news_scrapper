import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Get the current date in YYYY-MM-DD format
current_date = datetime.now().strftime("%Y-%m-%d")

url = "https://www.bbc.com/news"  # Example target site

# Send a request to fetch the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headlines = []
# Find all headline elements; ensure to update the class name as needed
# Ensure the correct class is used for headlines
for headline in soup.find_all('h2', class_="sc-8ea7699c-3 dhclWg"):  # Adjust the class name as necessary
    headlines.append(headline.text.strip())

# Define a delimiter to prepend to each headline
delimiter = "-"  # Change this to any delimiter you prefer

# Use the date in the filename
filename = f"headlines_{current_date}.csv"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])  # Write the header
    for h in headlines:
        # Write each headline with the delimiter prepended
        writer.writerow([f"{delimiter} {h}"])

# Confirm the file saving
print(f"\nScraped headlines saved to {filename}")