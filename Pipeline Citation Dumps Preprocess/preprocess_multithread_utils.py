# *********** TEST ************ #

from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

# Get the conference location from DBLP
# Called during the MAG preprocess
def get_conf_location_from_dblp(link):
    html = urlopen(link)
    bsh = BeautifulSoup(html.read(), 'html.parser').h1
    try:
        return str(bsh).split(':')[1].split('<')[0][1:]
    except:
        return None

# Prepare the URL and get the conference location from DBLP
# Called during the MAG preprocess
def mt_get_mag_conf_location_from_dblp_operation(conf_name, dblp_url):
    try:
        s = str(conf_name).split(' ') # example: "dexa 2002"
        url = dblp_url + "conf/" + s[0] + '/' + s[0] + s[1] + '.html' # example: "https://dblp.org/db/conf/dexa/dexa2002.html"
    except:
        pass
    try:
        d_item = get_conf_location_from_dblp(url)
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