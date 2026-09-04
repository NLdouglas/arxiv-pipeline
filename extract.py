import requests
import xml.etree.ElementTree as ET

url = "http://export.arxiv.org/api/query?search_query=cat:cs.LG&max_results=10"
response = requests.get(url)

root = ET.fromstring(response.text)
namespace = "{http://www.w3.org/2005/Atom}"

for entry in root.findall(f"{namespace}entry"):
    title = entry.find(f"{namespace}title").text
    print(title)
