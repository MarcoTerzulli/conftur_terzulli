# *********** TEST ************ #

from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

# ************ Scraper V1 ***************

# Get the conference location from DBLP
# Called during the MAG preprocess
def get_conf_location_from_dblp_v1(link):
    html = urlopen(link)
    header = BeautifulSoup(html.read(), 'html.parser').h1
    try:
        return str(header).split(':')[1].split('<')[0][1:] # da verificare
    except:
        return None

# Prepare the URL and get the conference location from DBLP
# Called during the MAG preprocess
def mt_get_mag_conf_location_from_dblp_operation_v1(conf_name, dblp_url):
    try:
        s = str(conf_name).split(' ') # example: "dexa 2002"
        url = dblp_url + s[0] + '/' + s[0] + s[1] + '.html' # example: "https://dblp.org/db/conf/dexa/dexa2002.html"
        print(url) # TODO DEBUG
    except:
        pass
    try:
        d_item = get_conf_location_from_dblp_v1(url)
    except:
        d_item = np.nan
    return conf_name, d_item

# ************ Scraper V2 ***************

# Get the conference location from DBLP
# Called during the MAG preprocess
def get_conf_location_from_dblp_v2(link, year):
    html = urlopen(link)
    h2s = BeautifulSoup(html.read(), 'html.parser').find_all("h2")
    print("dentro")
    print(h2s)

    for this_h2 in h2s:
        print(this_h2.text) # TODO DEBUG
        print(this_h2.id) # TODO DEBUG
        if this_h2.id == year:
            try:
                print("Tag trovato! " + this_h2.text.split(": ")[1]) # TODO DEBUG
                return this_h2.text.split(": ")[1] # 17th ICON 2011: Singapore --> Singapore
            except:
                return np.nan

    return np.nan

# Prepare the URL and get the conference location from DBLP
# Called during the MAG preprocess
def mt_get_mag_conf_location_from_dblp_operation_v2(conf_name, dblp_url):
    try:
        s = str(conf_name).split(' ') # example: "dexa 2002"
        url = dblp_url + s[0] + '/index.html' # example: "https://dblp.org/db/conf/dexa/index.html"
        print(url) # TODO DEBUG
    except:
        pass
    try:
        d_item = get_conf_location_from_dblp_v2(url, s[1])
    except:
        d_item = np.nan
    return conf_name, d_item

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