import urllib.request
import xml.etree.ElementTree as ET
import random
import requests

def get_random_arxiv():
    categories = ['cs.AI', 'cs.CR', 'q-bio.NC', 'cs.DC']
    cat = random.choice(categories)
    start = random.randint(0, 100)
    url = f'http://export.arxiv.org/api/query?search_query=cat:{cat}&start={start}&max_results=10'
    try:
        response = urllib.request.urlopen(url).read()
        root = ET.fromstring(response)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entries = root.findall('atom:entry', ns)
        if entries:
            entry = random.choice(entries)
            title = entry.find('atom:title', ns).text.replace('\n', ' ').strip()
            return f"📄 **ArXiv ({cat})** : {title}"
    except Exception: return "ArXiv Error"
    return "Nothing found"

def get_random_wiki_article():
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    try:
        headers = {"User-Agent": "ChaosEngine/1.0"}
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return f"🌀 **Random Concept** : {resp.json().get('title', '')}"
    except Exception: return "Wiki Error"
    return "Connection Error"

if __name__ == "__main__":
    print("=== 🌀 INITIATING CHAOS DROP ===\n")
    print(get_random_arxiv())
    print(get_random_wiki_article())
