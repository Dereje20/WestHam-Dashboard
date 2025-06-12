import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# URL for West Ham news on NewsNow
url = "https://www.newsnow.co.uk/h/Sport/Football/Premier+League/West+Ham+United?type=ln"

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send HTTP request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find article links (NewsNow uses specific classes)
headlines = soup.select('.newsfeed .hl')[:10]  # top 10 headlines

# Prepare data
data = []
for headline in headlines:
    title = headline.get_text(strip=True)
    link = headline.get('href')
    data.append([title, link])

# Filename with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
filename = f"data/headlines_{timestamp}.csv"

# Save to CSV
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Link'])
    writer.writerows(data)

print(f"✅ Saved {len(data)} headlines to {filename}")
