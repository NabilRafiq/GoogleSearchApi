from bs4 import BeautifulSoup
import requests, json

## article 1 
url = "https://www.bbc.com/news/world-asia-68178513"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("main#main-content")[0].select('p')
article_text = ' '.join([p.get_text(strip=True) for p in article])
date = soup.select("time")[0].text
author = soup.select("div.ssrcss-68pt20-Text-TextContributorName")[0].text
articles = {
    'article':article_text,
    'date':date,
    'author':author
}

## article 2
url = "https://en.wikipedia.org/wiki/Imran_Khan"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div#bodyContent")[0].select('p')
article_text = ' '.join([p.get_text(strip=True) for p in article])
articles['article_2'] = article_text 

##article 3 
url = "https://www.bbc.com/news/world-asia-68005660"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("main#main-content")[0].select('p')
article_text = ' '.join([p.get_text(strip=True) for p in article])
date = soup.select("time")[0].text
author = soup.select("div.ssrcss-68pt20-Text-TextContributorName")[0].text
articles['article_3'] = article_text
articles['article_3_date'] = date
articles['article_3_author'] = author

##article 4 
url = "https://www.aljazeera.com/news/2023/12/30/pakistan-poll-body-rejects-ex-pm-imran-khans-nomination-for-2024-elections"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div.wysiwyg--all-content")[0].select('p')
article_text = ' '.join([p.get_text(strip=True) for p in article])
date = soup.select("div.date-simple")[0].select('span.screen-reader-text')[0].text
print(date)
articles['article_4'] = article_text
articles['article_4_date'] = date

##article 5 
url = "https://www.theguardian.com/world/2024/jan/31/imran-khan-pakistan-election-tactics-military"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div#maincontent")[0].select('p')
article_text = ' '.join([p.get_text(strip=True) for p in article])
date = soup.select("details.dcr-1vmj0r")[0].select('span')[0].text
print(date)
articles['article_5'] = article_text
articles['article_5_date'] = date
##article 6 
url = "https://www.aljazeera.com/news/2023/12/26/pakistan-court-restores-jailed-ex-pm-imran-khans-party-election-symbol",
response = requests.get(url=url)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("p")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article_text)
articles['article_6'] = article_text
##article 7 
url = "https://www.reuters.com/world/asia-pacific/pakistan-hold-national-election-jan-not-nov-vote-commission-2023-09-21/",
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div.article-body__content__17Yit")[0].select('div')
article_text = ' '.join([div.get_text(strip=True) for div in article])
date = soup.select("time")[0].select('span')[0].text    
author = soup.select("div.info-content__author-date__1Epi_")
print(author)
articles['article_7'] = article_text
articles['article_7_date'] = date
articles['article_7_author'] = author

##article 8
url =  "https://www.economist.com/by-invitation/2024/01/04/imran-khan-warns-that-pakistans-election-could-be-a-farce",
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("section.css-1a9zct9 euw0bys1")
##article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article)
date = soup.select("time")[0].select('span')[0].text
print(date)    
articles['article_8'] = article_text
articles['article_8_date'] = date
##article 9
url =  "https://www.chathamhouse.org/publications/the-world-today/2024-02/pakistan-imran-khans-party-faces-huge-election-losses",
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("p")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article_text)
script_tag = soup.find("script", {"type": "application/ld+json"})
json_ld_data = json.loads(script_tag.string)

# Extracting author name and published date
author_name = None
date_published = None

if json_ld_data:
    for item in json_ld_data:
        if "@type" in item and item["@type"] == "Article":
            author_name = item.get("author", {}).get("name")
            date_published = item.get("datePublished")
            break

print("Author:", author_name)
print("Published Date:", date_published)
articles['article_9'] = article_text
articles['author'] = author
articles['article_9_date'] = date
##article 10
url =   "https://time.com/6316623/pakistan-elections-imran-khan-jail/"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div#article-body-main")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article)
date = soup.select("time")[0].select('span')[0].text
print(date)    
articles['article_10'] = article_text
articles['article_10_date'] = date
   
##article 11
url =    "https://asia.nikkei.com/Politics/Pakistan-election-or-selection-Imran-Khan-s-exclusion-all-but-sealed",
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("p")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article)
date = "January 02, 2024"
print(date)    
articles['article_11'] = article_text
articles['article_11_date'] = date
with open('Articles_Data.json', 'w') as file:
        json.dump(articles, file,indent=3)        

##article 12
url =    "https://time.com/6556335/pakistan-election-imran-khan-nawaz-sharif-military-pti/",
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("article#article-body")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article)
date = soup.select("time")[0].select('span')[0].text
print(date)    
articles['article_12'] = article_text
articles['article_12_date'] = date
with open('Articles_Data.json', 'w') as file:
        json.dump(articles, file,indent=3)        

##article 13
url =    "https://www.brookings.edu/articles/did-pakistans-imran-khan-win-a-dirty-election-or-a-real-mandate/"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("p")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article)
date = soup.select("time")[0].select('span')[0].text
print(date)    
articles['article_13'] = article_text
articles['article_13_date'] = date
with open('Articles_Data.json', 'w') as file:
        json.dump(articles, file,indent=3)        

##article 14
url =    "https://apnews.com/article/pakistan-jailed-imran-khan-election-d9b4496716948c17d5c09a32f00c537e",
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div.RichTextStoryBody")[0].select("p")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article)
date = soup.select("span.data-date")[0].text
print(date)    
articles['article_14'] = article_text
articles['article_14_date'] = date
with open('Articles_Data.json', 'w') as file:
        json.dump(articles, file,indent=3)        

##article 15
url = "https://www.france24.com/en/asia-pacific/20231231-imprisoned-former-pakistan-pm-imran-khan-barred-from-election-candidacy"   
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div.t-content__body")[0].select("p")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article_text)
date = soup.select("span.m-pub-dates__date")[0].select("time")
print(date)    
articles['article_15'] = article_text
articles['article_15_date'] = date
with open('Articles_Data.json', 'w') as file:
        json.dump(articles, file,indent=3)        

