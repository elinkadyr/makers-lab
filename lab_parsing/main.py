import json

import requests
from bs4 import BeautifulSoup as BS
 

def get_data():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
    }
    
    url = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"

    res = requests.get(url=url, headers=headers)

    soup = BS(res.text, "lxml")


def main():
    get_data()

if __name__ == "__main__":
    main()
