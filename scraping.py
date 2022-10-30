# https://www.youtube.com/watch?v=WXATmwVcSYg&ab_channel=SuvethaSuresh

import requests
import os
from tqdm import tqdm
from time import sleep

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
query = input('Enter Keyword Here:')
endpage = (int(input('Amount of pages:')))

# Downloading 
cur_dir = os.getcwd()
output = cur_dir + f'/{query}'
if not os.path.exists(output):
    os.mkdir(output)

api_url = ['https://unsplash.com/napi/search/photos?query={}&per_page=20&page={}&xp='.format(query, x) for x in range (1, endpage)]
for url in tqdm(api_url):
    r = requests.get(url, headers=headers)
    json_data = r.json()
    for images in tqdm(json_data['results']):
        image_title = images['alt_description']
        image_url = images['urls']['raw']
        try:
            with open(output + '/' + image_title + '.jpg', 'wb') as file:
                r = requests.get(image_url, stream = True)
                file.write(r.content)
        except:
            pass    
    sleep(1)