# HTML Basics for Web Scraping with Python
-HTML stands for Hyper Text Markup Language and it is one of the basic tools used to make website , it defines the meaning and structure of web content. 
-**HTML Markup syntex review**
`<h1 class="title">Titanic (1997)</h1>`
    the first element (<h1>) is a **tag**, they are hidden keywords within a webpage that defines how web browser must format and display  the content . Most tags must have two parts - an opening and a closing part .

    the second element (class="title")  we see is a tag attribute .They allow us to cusomize attack and  are defined within the opeing tag. attribute are often assigned a value using the  equal sign . the attribute value in this example is title

    and lastly we have the affected content which is what we usually see in the website .

    and all of these is know as an html element or node.
## 1. HTML Document Structure
- **DOCTYPE**: Declares HTML version (`<!DOCTYPE html>`)
- **html**: Root element
- **head**: Contains metadata, title, links
- **body**: Contains visible page content

## 2. Common HTML Tags for web scrapping
-`<>head` : this reperesent the head section and it is used mostly for  metadata
`<body>` : This establishes the body of an HTML document 
`<header>` : typically contains the introductory content and layout that goes above the body 
### Text Elements
- `<h1>` to `<h6>`: Headings (h1 largest, h6 smallest)
- `<p>`: Paragraph
- `<span>`: Inline text container
- `<div>`: Block-level container
- `<a>`: Hyperlink with `href` attribute

### Lists
- `<ul>`: Unordered list
- `<ol>`: Ordered list
- `<li>`: List item

### Tables
- `<table>`: Table container
- `<tr>`: Table row
- `<td>`: Table data cell
- `<th>`: Table header cell
- `<thead>`, `<tbody>`, `<tfoot>`: Table sections

## 3. HTML Attributes
- **id**: Unique identifier for element
- **class**: CSS class (multiple allowed)
- **href**: URL for links
- **src**: Source URL for images
- **name**: Element name
- **data-***: Custom data attributes

## 4. CSS Selectors (for scraping)
- **Element selector**: `p`, `div`, `a`
- **Class selector**: `.classname`
- **ID selector**: `#idname`
- **Attribute selector**: `[href]`, `[data-id="value"]`
- **Descendant**: `div p` (p inside div)
- **Child**: `div > p` (direct child)
- **Multiple classes**: `.class1.class2`

## 5. Web Scraping Tools in Python
- **BeautifulSoup**: Parse HTML/XML
- **Requests**: Fetch web pages
- **Selenium**: JavaScript-heavy pages
- **lxml**: Fast HTML/XML parsing

## 6. BeautifulSoup Basics
```python
from bs4 import BeautifulSoup
import requests

# Fetch and parse
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Select elements
element = soup.find('div', class_='classname')
elements = soup.find_all('p')
element = soup.select_one('.classname')
elements = soup.select('div > p')

# Extract data
text = element.get_text()
attr = element.get('href')
```

## 7. DOM Navigation
- `.parent`: Parent element
- `.children`: Child elements (iterator)
- `.next_sibling`, `.previous_sibling`: Adjacent elements
- `.string`: Direct text content
- `.stripped_strings`: Text without whitespace

## 8. Common Patterns
- Extract all links: `soup.find_all('a')`
- Get table data: Loop through `<tr>` and `<td>`
- Extract meta tags: `soup.find('meta', attrs={'name': 'description'})`
- Filter by attributes: `soup.find_all('div', attrs={'data-id': 'value'})`

## 9. Important Considerations
- Check robots.txt and site's terms of service
- Use appropriate delays between requests
- Set User-Agent header to mimic browser
- Handle errors gracefully (missing elements, timeouts)
- Respect the server's resources
