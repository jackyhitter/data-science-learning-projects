'''
                        WEB SCRAPPING
https://en.wikipedia.org/wiki/Website
https://en.wikipedia.org/wiki/History_of_the_World_Wide_Web
https://en.wikipedia.org/wiki/Web_2.0

'''
import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://en.wikipedia.org/wiki/Website",
    "https://en.wikipedia.org/wiki/History_of_the_World_Wide_Web",
    "https://en.wikipedia.org/wiki/Web_2.0"
]

def fetchContent(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"{'-'*80}")
    print(response.status_code)
    print(response.url)
    print(response.text[:100])
    print(f"{'-'*80}")
    print(f"Title of {url}:\n {soup.find('title').text} \n and total characters are {len(soup.text)} \n")


threads = []

for url in urls:
    thread = threading.Thread(target=fetchContent, args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()

print("All threads have completed execution.")
