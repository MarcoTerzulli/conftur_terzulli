# *********** TEST ************ #

from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
from time import sleep


# ************ MAG Scraper V1 ***************

# Get the conference location from DBLP
# Called during the MAG preprocess
def get_conf_location_from_dblp_v1(url, year):
    html = urlopen(url)
    h2 = BeautifulSoup(html.read(), 'html.parser').find(id=year)

    print(f"{url} - Year {year}: {h2}") # TODO DEBUG
    try:
        return h2.text.split(": ")[1] # 17th ICON 2011: Singapore --> Singapore
    except:
        return np.nan

# Prepare the URL and get the conference location from DBLP
# Called during the MAG preprocess
def mt_get_mag_conf_location_from_dblp_operation_v1(conf_name, dblp_url, sleep_delay=0):
    try:
        sleep(sleep_delay)
        
        s = str(conf_name).split(' ') # example: "dexa 2002"
        url = dblp_url + s[0] + '/index.html' # example: "https://dblp.org/db/conf/dexa/index.html"
    except:
        pass
    try:
        d_item = get_conf_location_from_dblp_v1(url, s[1])
    except:
        d_item = np.nan
    return conf_name, d_item


# ************ MAG Scraper V2 ***************

# Get the conference location from DBLP
# Called during the MAG preprocess
def get_conf_location_from_dblp_v2(url):
    html = urlopen(url)
    header = BeautifulSoup(html.read(), 'html.parser').h1
    try:
        return str(header).split(':')[1].split('<')[0][1:]
    except:
        return None

# Prepare the URL and get the conference location from DBLP
# Called during the MAG preprocess
def mt_get_mag_conf_location_from_dblp_operation_v2(conf_name, dblp_url, sleep_delay=0):
    try:
        sleep(sleep_delay)
        
        s = str(conf_name).split(' ') # example: "dexa 2002"
        url = dblp_url + s[0] + '/' + s[0] + s[1] + '.html' # example: "https://dblp.org/db/conf/dexa/dexa2002.html"
        print(url) # TODO DEBUG
    except:
        pass
    try:
        d_item = get_conf_location_from_dblp_v2(url)
    except:
        d_item = np.nan
    return conf_name, d_item


# ************ DBLP Scraper ***************
# Prepare the URL and get the conference location from DBLP
# Called during the DBLP preprocess
def mt_get_dblp_conf_location_from_dblp_operation(conf_url, dblp_url, sleep_delay=0):
    try:
        sleep(sleep_delay)

        url = dblp_url + conf_url # example: "https://dblp.org/db/conf/dexa/dexa2002.html"
        print(url) # TODO DEBUG
    except:
        pass
    try:
        d_item = get_conf_location_from_dblp_v2(url)
    except:
        d_item = np.nan
    return conf_url, d_item



########### OLD

def get_place(link):
    html = urlopen(link)
    bsh = BeautifulSoup(html.read(), 'html.parser').h1
    try:
        return str(bsh).split(':')[1].split('<')[0]
    except:
        return None

def mt_get_place_operation(x, link):
    try:
        s = str(x).split('/')
        url = link + s[0] + '/' + s[1] + '/' + s[1]+s[2] + '.html'
    except:
        pass
    try:
        d_item = get_place(url)
    except:
        d_item = None
    return x, d_item

def mt_get_place_fix_none_operation(k, v, link):
    d_item = None
    
    if v == 'None':
        s = str(k).split('/')
        data = ''
        try:
            for x in range(4):
                data += s[2][x]
            url = link + s[0] + '/' + s[1] + '/' + s[1]+data + '.html' 
        except:
            pass
        try:
            d_item = get_place(url)
        except:
            d_item = None
    return k, d_item