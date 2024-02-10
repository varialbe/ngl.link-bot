import requests
from bs4 import BeautifulSoup

class ProxyScraper:
    def __init__(self):
        self.all_proxies = []

    def _fetch_from_free_proxy_list(self):
        response = requests.get("https://free-proxy-list.net/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            proxies = [line.strip() for line in soup.select_one('#raw > div > div > div.modal-body > textarea').text.split('\n')[3:] if line.strip()]
            self.all_proxies.extend(proxies)

    def _fetch_from_proxyscrape(self):
        response = requests.get("https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&proxy_format=ipport&format=text")
        if response.status_code == 200:
            proxies = [proxy.strip() for proxy in response.text.strip().split('\n') if proxy.strip()]
            self.all_proxies.extend(proxies)

    def _fetch_from_geonode(self):
        response = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc")
        if response.status_code == 200:
            proxies = [f"{proxy['ip']}:{proxy['port']}" for proxy in response.json()['data']]
            self.all_proxies.extend(proxies)

    def fetch_from_netzwelt(self):
        response = requests.get("https://www.netzwelt.de/proxy/index.html")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.select('#article > div.tblc > table > tbody > tr')
            proxies = [f"{row.find('td').find('a').text.strip()}:{row.find_all('td')[1].text.strip()}" for row in rows]
            self.all_proxies.extend(proxies)

    def fetch_from_openproxylist(self):
        response = requests.get("https://api.openproxylist.xyz/http.txt")
        if response.status_code == 200:
            proxies = response.text.strip().split('\n')
            self.all_proxies.extend(proxies)

    def fetch_and_combine_proxies(self):
        self._fetch_from_free_proxy_list()
        self._fetch_from_proxyscrape()
        self._fetch_from_geonode()
        self.fetch_from_netzwelt()
        self.fetch_from_openproxylist()
        return self.all_proxies

def get_all_proxies():
    scraper = ProxyScraper()
    return scraper.fetch_and_combine_proxies()


'''
Usage:

import variscrapeMOD as vs

proxyList = vs.get_all_proxies() -> Returns an array of proxies ['IP:PORT']

print(proxyList)

'''
