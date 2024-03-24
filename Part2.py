from bs4 import BeautifulSoup
import requests, json

## article 1 
url = Link1
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
url = Link2 
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div#bodyContent")[0].select('p')
article_text = ' '.join([p.get_text(strip=True) for p in article])
articles['article_2'] = article_text 

##article 3 
url = Link3
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
url = Link4
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div.wysiwyg--all-content")[0].select('p')
article_text = ' '.join([p.get_text(strip=True) for p in article])
date = soup.select("div.date-simple")[0].select('span.screen-reader-text')[0].text
print(date)
articles['article_4'] = article_text
articles['article_4_date'] = date

##article 5 
url = Link5
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("div#maincontent")[0].select('p')
article_text = ' '.join([p.get_text(strip=True) for p in article])
date = soup.select("details.dcr-1vmj0r")[0].select('span')[0].text
print(date)
articles['article_5'] = article_text
articles['article_5_date'] = date
##article 6 
url = Link6
response = requests.get(url=url)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("p")
article_text = ' '.join([p.get_text(strip=True) for p in article])
print(article_text)
articles['article_6'] = article_text
##article 7 
url = Link7
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
url =  Link8
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
url =  Link9
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
url =   Link10
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
url =    Link11
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
url =    Link12
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
url =    Link13
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
url =    Link14
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
url = Link15   
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

