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

#### children, contents : get children of a element
```
[print(child) for child in body.contents]
[print(child) for child in body.children]
```

#### get(), attrs : get attributes of a element
```
a_tag = soup.find('a')
atributes = a_tag.attrs
a_href = a_tag.get('href')
a_href = a_tag['href]
```

#### limit : limit result of search, with this option you can declare how many elements you want your program return :
```
div_tags = soup.find_all()('div',limit=1)
```

#### next_sibling : get nex sibling of an element
```
p_tag = soup.find('p')  # Find the <p> tag
if p_tag:
    next_tag = p_tag.next_sibling.next_sibling  # Get the next sibling tag of the <p> tag
```

#### next_siblings : get all next siblings of an element 
```
counter = 0
for i in p_tag.next_siblings:
    counter += 1
```

#### parent, parents : get parent or parents of an element
```
a = soup.find('a')
p = soup.find('p')

print(a.parent) # displays only parent of a tag
[print(child.name) for child in p.parents] # displays parents of parent of p tag
```

#### pre_sibling, pre_siblings : get one previous sibling of a tag
```
p_tag = soup.find('main')  # Find the <p> tag

if p_tag:
    next_tag = p_tag.previous_sibling  # Get the prev sibling tag of the <p> tag
    print("next sibling tag :", next_tag)


# prevoius siblings :
counter = 0
for i in p_tag.previous_siblings:
    counter += 1
```

#### append(): add a new string to the end of the content of an element
```
# get a tag
tag = soup.find('b')

# add a new string to the end of the string
tag.append(' you')
print(tag)
```

#### clear() : erase string of an element
```
# get a tag
tag = soup.find('b')

# wipe up the tag's string
tag.clear()
print(tag)
```

#### new_tag() : create a new element using beautifulsoup instance
```
soup = BeautifulSoup(html, 'html.parser')
new_tag = soup.new_tag('a')
```

#### wrap(), unwrap() : wrap or unwrap a tag with another tag
```
# wrap a tag with another tag
a_tag = soup.find('a')
wrapper = soup.new_tag('div')
# wrap "a" tag with a "div" tag
a_tag.wrap(wrapper)

# unwrap an element
a_tag.unwrap()
```

