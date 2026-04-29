# HTML Basics for Web Scraping with Python

## 1. HTML Document Structure
- **DOCTYPE**: Declares HTML version (`<!DOCTYPE html>`)
- **html**: Root element
- **head**: Contains metadata, title, links
- **body**: Contains visible page content

## 2. Common HTML Tags

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
