import requests
import threading
import variscrapeMOD as vs
from colorama import Fore, Style
import time


count = 0
failCount = 0
lock = threading.Lock()

print(Fore.GREEN + "Scraping Proxies..." + Style.RESET_ALL)

start_time = time.time() 

proxies_list = vs.get_all_proxies()

end_time = time.time()
duration = end_time - start_time

print(Fore.GREEN + "Scraped Proxies in " + Style.RESET_ALL + f"{duration:.2f} seconds")

def send(proxy):
    global count
    global failCount
    while True:
        url = "https://ngl.link/api/submit"
        payload = {
            "username": "abbajiza", # Username here
            "question": "Test Message", # Message content here
            "deviceId": "02ef6283-1ad3-44f3-8546-e4b0117970", # Any string here
        }
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }

        try:
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                count += 1
                ratio = (count / (count + failCount)) * 100
                
                if ratio <= 20:
                    color = Fore.RED
                elif 20 < ratio < 50:
                    color = Fore.YELLOW
                else:
                    color = Fore.GREEN

                print(Fore.GREEN + f"Success : {count} | " + Fore.YELLOW + f"Fails : {failCount} | " + Fore.MAGENTA + "Ratio : " + color + f"{ratio:.2f}%" + Style.RESET_ALL)
            else:
                failCount += 1
        except Exception as e:
            failCount += 1
def start_threads(proxies_list, max_threads=10000):
    threads = []
    for proxy in proxies_list:
        if len(threads) < max_threads:
            thread = threading.Thread(target=send, args=(proxy,))
            threads.append(thread)
            thread.start()
        else:
            for t in threads:
                t.join()
            threads = []

if __name__ == "__main__":
    start_threads(proxies_list)
