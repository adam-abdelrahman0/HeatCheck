import requests
import zipfile
import shutil
import threading
import uuid
import os
import time
from PIL import Image
from io import BytesIO

#specify paths
imageDir = 'imageDirectory'
newZipDirAndName = 'zipName'

accessToken = 'accessToken'

#get hashtag name
def getHashName(hashtag_id):
    url = f"https://graph.facebook.com/v21.0/{hashtag_id}"
    params = {
        'fields': 'name',
        'access_token': accessToken
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # check if the name field exists 
    if 'name' in data:
        return data['name']
    else:
        return None  # if the name is not found

def downloadImg(url, tagName):
    try:
        print(f"Downloading image {uuid.uuid4()} from {url}")
        image_response = requests.get(url)
        img = Image.open(BytesIO(image_response.content))
        img.save(f'{imageDir}/{tagName}_{uuid.uuid4()}.jpg', 'JPEG')
        print(f"Image {tagName}_{uuid.uuid4()} saved successfully")
        
    except Exception as e:
        print(f"Error downloading image {uuid.uuid4()}: {e}")

# hashtag ID list
idList = ['17841592771073334', '17843146432007976', '17843829844009940', '17843727913052565', '17842284655067909', '17843698438042472', '17843892265020344', '17843723689007987', '17843830906017148', '17841563308101050', '17841599389072250', '17842555510061799', '17843802649050725', '17841591718073119', '17843742502017651']

#set retries for when it breaks
MAX_RETRIES = 3

for id in idList:
    try:
        
        tagName = getHashName(id)
        if not tagName:
            print(f"Hashtag name not found for ID {id}")
            continue  #if not found, skip to next ID

        params = {
            'user_id': '17841449940140462',
            'access_token': accessToken,
            'q': id, 
            'fields': 'media_url'
        }
        
        topMediaUrl = f'https://graph.facebook.com/v21.0/{id}/top_media'

        #attempt fetch
        pageNum = 0
        retries = 0  

        while retries < MAX_RETRIES:
            response = requests.get(topMediaUrl, params=params)
            
            if response.status_code == 200:
                break  # if successful, no retry
            else:
                print(f"Error {response.status_code}: retrying in 5 seconds...")
                retries += 1
                time.sleep(5)

        if retries == MAX_RETRIES:
            print(f"Max retries reached for ID {id}. Skipping to the next ID.")
            continue  # go to next ID

        data = response.json()

        # check if 'data' exists and is not empty
        if 'data' in data and data['data']:

            # download images from the first page
            media_urls = [item.get('media_url') for item in data['data']]
            pageNum += 1
            
            for url in media_urls:
                threading.Thread(target=downloadImg, args=(url, tagName)).start()
            
            #keep paging along
            for i in range(99):
                next_page_url = data['paging'].get('next')

                if not next_page_url:
                    print("No more pages to load.")
                    break  # exit the loop if there's no next page

                print(f"Next url: {next_page_url}")

                retries = 0  #reset tries

                while retries < MAX_RETRIES:
                    response = requests.get(next_page_url, params=params)
                    if response.status_code == 200:
                        break
                    print(f"Error {response.status_code}: retrying in 5 seconds...")
                    retries += 1
                    time.sleep(5)

                if retries == MAX_RETRIES:
                    print(f"Max retries reached for the next page. Skipping to the next ID.")
                    break  

                data_next_page = response.json()

                # download images from the next page
                media_urls_next_page = [item.get('media_url') for item in data_next_page.get('data', [])]
                
                for url in media_urls_next_page:
                    threading.Thread(target=downloadImg, args=(url, tagName)).start()
                
                pageNum += 1

                # update data for the next page
                data = data_next_page
        else:
            print(f"No media data found for ID {id}.")
    
    except Exception as e:
        # if any exception, next ID
        print(f"An error occurred with ID {id}: {e}")
        continue  

#zip all the images
try:
    shutil.make_archive(newZipDirAndName, 'zip', imageDir)
    print("Images successfully zipped.")
except Exception as e:
    print(f"Error while zipping files: {e}")

#clean all images from directory bc its a giant directory
try:
    for file_name in os.listdir(imageDir):
        file_path = os.path.join(imageDir, file_name)
        if os.path.isfile(file_path):  
            os.remove(file_path)
    
    print("All files in the images directory have been deleted!")
except Exception as e:
    print(f"Error while deleting files: {e}")
