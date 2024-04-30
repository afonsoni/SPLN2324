pip install beautifulsoup4 (usado para navegar em html)
pip install requests

soup.title -  vai buscar a tag do title (ex <title> Example </title>)
soup.title.text - vai buscar o texto do title (ex Example)
soup.a("href") - vai buscar o link do href (ex "http://www.example.com/")

soup.find_all("li") - vai buscar todas as tags li (ex <li> Example </li>)
soup.find_all("li", class_="example") - vai buscar todas as tags li com a class example (ex <li class="example"> Example </li>)
soup.find("li") - vai buscar a primeira tag li (ex <li> Example </li>)
soup.find_children("li") - vai buscar os filhos da tag li (ex <li> Example </li>)
soup.find_parent("li") - vai buscar o pai da tag li (ex <li> Example </li>)