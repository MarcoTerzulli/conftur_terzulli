# *********** TEST ************ #

from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
import requests
from urllib.request import urlopen

# compute the city SWP from wikipedia
def get_city_swp_v1(url):
    page = requests.head(url)
    c=0

    while page.headers.get ( "content-length" ) == None:
        if c < 4:
            page = requests.head(url)
        else: 
            break
        c += 1

    return page.headers.get("content-length")

# Prepare the URL and compute the city SWP from wikipedia
def mt_get_city_swp_operation_v1(conf_location, wikipedia_url, sleep_delay=0):
    try:
        sleep(sleep_delay)
        url = wikipedia_url + conf_location[1] # example: "https://en.wikipedia.org/wiki/Shijiazhuang"
    except:
        pass
    try:
        swp = get_city_swp_v1(url)
    except:
        swp = np.nan
    return conf_location, swp


# Prepare the URL and compute the city SWP from wikipedia
def mt_get_city_swp_operation_v2(conf_location, wikipedia_url, sleep_delay=0):
    try:
        sleep(sleep_delay)
        url = wikipedia_url + conf_location[1] + ',' + conf_location[0].split(',')[1].replace(' ', '_') # example: "https://en.wikipedia.org/wiki/Auburn,_Washington"
    except:
        pass
    try:
        swp = get_city_swp_v1(url)
    except:
        swp = np.nan
    return conf_location, swp


