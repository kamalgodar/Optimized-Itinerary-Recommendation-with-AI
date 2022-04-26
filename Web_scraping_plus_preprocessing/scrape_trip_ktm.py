import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

attractions_list=[]

#since the first 30 entries on the first page has a different url, we make a different function for it (there could be so many ways to do but ....)

def get_first_30_attractions():
    #url to extract the first 30 attractions of Nepal
    url='https://www.tripadvisor.com/Attractions-g293890-Activities-a_allAttractions.true-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    attractions = soup.find_all('div', {'class': '_392swiRT fQ-rHrKc'})
    for item in attractions:
        title=item.find('span', {'name': 'title'}).text.split(".")[1:]
        try:
            avg_rating=item.find('svg',{'class':'zWXXYhVR'})["aria-label"].split(" ")
        except:
            avg_rating='Nan'

        try:
            voted_by=item.find('span',{'class':'DrjyGw-P _26S7gyB4 _14_buatE _1dimhEoy'}).text
        except:
            voted_by='0'

        try:
            genre=item.find('div',{'class':'DrjyGw-P _26S7gyB4 _3SccQt-T'}).text
        except:
            genre='Nan'

        #make the title as a string 

        title_string=""
        for item in title:
            title_string=title_string+item

        attraction = {
        'title':title_string[1:], #index starts from 1 to remove the excess space at the front 
        'avg_rating':avg_rating[0],
        'voted_by':int(voted_by.replace(',','')),
        'genre':genre,
        }
        attractions_list.append(attraction)
    return

def get_remaining_attractions(page):
    #url to extract the attractions of Nepal
    url=f'https://www.tripadvisor.com/Attractions-g293890-Activities-oa{page}-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    attractions = soup.find_all('div', {'class': '_392swiRT fQ-rHrKc'})
    for item in attractions:
        title=item.find('span', {'name': 'title'}).text.split(".")[1:]
        try:
            avg_rating=item.find('svg',{'class':'zWXXYhVR'})["aria-label"].split(" ")
        except:
            avg_rating='Nan'

        try:
            voted_by=item.find('span',{'class':'DrjyGw-P _26S7gyB4 _14_buatE _1dimhEoy'}).text
        except:
            voted_by='0'

        try:
            genre=item.find('div',{'class':'DrjyGw-P _26S7gyB4 _3SccQt-T'}).text
        except:
            genre='Nan'

        #make the title as a string 

        title_string=""
        for item in title:
            title_string=title_string+item

        attraction = {
        'title':title_string[1:], #index starts from 1 to remove the excess space at the front 
        'avg_rating':avg_rating[0],
        'voted_by':int(voted_by.replace(',','')),
        'genre':genre,
        }
        attractions_list.append(attraction)
    return

#get the first 30 attractions of Nepal 
get_first_30_attractions()

#for the remaining 3000+ attractions
page=30 #initializing page number 

while page<=2340:
    get_remaining_attractions(page)
    print(f"done #{page} attractions")
    page+=30 #keep increasing by 30 in each iteration
    

print(len(attractions_list))
#make a pandas dataframe 
df = pd.DataFrame(attractions_list)
print(df.shape)
# print(df)
#save to a csv file 
df.to_csv('attractions_of_ktm.csv', index=False)
