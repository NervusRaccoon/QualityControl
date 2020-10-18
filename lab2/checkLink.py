import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import datetime

valid = open('valid.txt', 'w')
invalid = open('invalid.txt', 'w')
storage = []

def check_url(url):
    try:
        r = requests.head(url)
        if int(r.status_code) == 200:
            valid.write("Правильная ссылка: " + url + ' ' + str(r.status_code) + '\n')
        else:
            invalid.write("Неправильная ссылка: " + url + ' ' + str(r.status_code) + '\n')
    except requests.ConnectionError:
        print("failed to connect")
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

#scheme://netloc/path;parameters?query#fragment
def website(url):
    urls = set()
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href) # присоединить URL, если он относительный (не абсолютная ссылка)
        parsed_href = urlparse(href)
        link = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path # удалить параметры URL GET, фрагменты URL и т. д.
        if parsed_href.scheme != 'http':
            continue
        if link in storage:
            continue
        if not check_url(link):
            continue
        storage.append(link)
    return storage

def crawl(url, links):
    i = 0
    while i < len(links):
        website(links[i])
        i += 1

if __name__ == "__main__":
    url = "http://91.210.252.240/broken-links/"
    website(url)
    crawl(url, storage)
    valid.write("Найдено ссылок:" + str(len(storage)) + "\n")
    valid.write("Дата: " + str(datetime.datetime.now()) + "\n")
    invalid.write("Найдено ссылок:" + str(len(storage)) + "\n")
    invalid.write("Дата: " + str(datetime.datetime.now()) + "\n")
