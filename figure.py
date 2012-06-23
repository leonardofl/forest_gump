import sys
import urllib2
from BeautifulSoup import BeautifulSoup

BASE_URL = 'http://%s.wikipedia.org/wiki/%s'

LANGUAGE = 'pt'

def from_wikipedia(word):
    """Returns the link of a figure in the verbet of 'word' (a string)
    For example, passing word='cavalo' it is expected to get a horse figure
    If no figure is found, None is returned
    By default the words are searched in the wikipedia in Portuguse
    To change the language, set the language.LANGUAGE variable
    """ 
    url = BASE_URL % (LANGUAGE, word)
    try:
        request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        site = urllib2.urlopen(request)
    except:
        print '%s does not exist in the wikipedia-%s' % (word, LANGUAGE)    
        return None
    soup = BeautifulSoup(site)
    img_src = soup.find("a", { "class" : "image" }).findChild('img').get('src')
    return img_src.replace('//', '')

if __name__ == "__main__":
    print from_wikipedia(sys.argv[1])
