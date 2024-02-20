import csv
import requests
from bs4 import BeautifulSoup

# Function to extract information from each grid item and write to CSV
def extract_info_to_csv(url, output_file):
    # Make a GET request to the webpage
    response = requests.get(url)
    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all div elements with class 'grid-item'
        grid_items = soup.find_all('div', class_='grid-item')
        # Open the CSV file for writing
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header row
            writer.writerow(['Product', 'Price', 'Image URL'])
            # Extract information from each grid item and write to CSV
            for grid_item in grid_items:
                # Extract product name
                product_name = grid_item.find('h3').text.strip()
                # Extract price
                price = grid_item.find('p').text.strip().split(':')[1].strip()
                # Extract image URL
                image_url = grid_item.find('img')['src']
                # Write to CSV
                writer.writerow([product_name, price, image_url])
        print(f"CSV file '{output_file}' created successfully.")
    else:
        print("Failed to fetch webpage")

# URL of the webpage containing grid items
url = 'https://mycartshopping.000webhostapp.com/'
# Output CSV file path
output_file = 'products.csv'
# Call the function to extract information and write to CSV
extract_info_to_csv(url, output_file)
