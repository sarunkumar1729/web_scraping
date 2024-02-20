# downloading all the images
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download images from a webpage
def download_images(url):
    # Make a GET request to the webpage
    response = requests.get(url)
    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all div elements with class 'grid-item' containing img tags
        grid_items = soup.find_all('div', class_='grid-item')
        # Create a directory to store images if it doesn't exist
        if not os.path.exists('downloaded_images'):
            os.makedirs('downloaded_images')
        # Download each image
        for grid_item in grid_items:
            img_tag = grid_item.find('img')
            if img_tag:
                # Get the source URL of the image
                img_url = img_tag['src']
                # Construct the absolute URL if it's relative
                img_url = urljoin(url, img_url)
                # Get the image content
                img_content = requests.get(img_url).content
                # Extract the filename from the URL
                img_filename = os.path.basename(img_url)
                # Save the image to the directory
                with open(os.path.join('downloaded_images', img_filename), 'wb') as f:
                    f.write(img_content)
                print(f"Downloaded: {img_filename}")
    else:
        print("Failed to fetch webpage")

# URL of the webpage containing images
url = 'https://mycartshopping.000webhostapp.com/'
# Call the function to download images
download_images(url)


# file = open('sample.txt','w')
# file.write("hello")
# file.close()