from email.mime import image
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


# url = "https://www.pinterest.com/vib3ch3ck/Fits-and-heat/"
# the pinterest board in question, set later on line 27 ish


# also mostly for testing
def openUrlImage(url):
    try:
        # fetch image from url
        response = requests.get(url)
        response.raise_for_status()  # error check (courtesty of internet)

        img_data = BytesIO(response.content)
        img = Image.open(img_data) #convert binary to image

        img.show() #open image
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve image: {e}")

# set the url
url = "https://www.pinterest.com/vib3ch3ck/Fits-and-heat/"

# this one is also from the internet bc ??
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# fetch HTML
response = requests.get(url, headers=headers)
if response.status_code == 200:
    page_content = response.text
else:
    print("Failed to retrieve the webpage:", response.status_code)

# parse html
soup = BeautifulSoup(page_content, 'html.parser')

# find all img tags 
image_elements = soup.find_all('img')

# store the urls for images in list
image_urls = [img['src'] for img in image_elements if 'src' in img.attrs]




# open the images, more for testing than use
for i in range(len(image_urls)):
     if i != 0:
        openUrlImage(image_urls[i])



