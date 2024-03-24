import requests, json 

Api_key = open('Api_Key.txt').read()
Search_Query = 'Imran Khan in Election'
SearchEngineId = open('SearchEngineId.txt').read()
links = []
url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'key': Api_key,
    'cx' : SearchEngineId,
    'q'  : Search_Query,
    'start' : 11
}

response = requests.get(url, params=params)
result = response.json()
### Get Links
if 'items' in result:
   for item in result['items']:
       links.append(item['link'])
       
with open('Search_Data.json', 'w') as file:
    json.dump(result, file,indent=3)
    
with open('Search_Data_Links.json', 'w') as file:
        json.dump(links, file,indent=3)