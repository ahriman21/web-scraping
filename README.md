# web-scraping
python web scraping cheetsheat and summary

## start:
```
from bs4 import BeautifulSoup

html = requests.get(url)
soup = BeautifulSoup(html, 'html.parser')
```


## methods :
#### find() , find_all() : get tags with name and attributes
```
# Using find() to find the first paragraph with class="content"
first_content_paragraph = soup.find('p', class_='content')
print("First Content Paragraph:", first_content_paragraph)

# Using find_all() to find all paragraphs with class="content"
all_content_paragraphs = soup.find_all('p', class_='content')
print("All Content Paragraphs:", all_content_paragraphs)

# Using find_all() or find() to get tags with specific attributes:
soup.find(attrs={'id':'contact'})

# get value of an attribute of selected tag:
soup.find('a').get('href') 
```


#### select() : get tags with css selectors
```
soup.select('.container h3')
```
