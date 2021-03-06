#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012, Leonardo Leite
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
import re
import sys
import urllib2
import urllib
import os
import random
from BeautifulSoup import BeautifulSoup

BASE_URL = 'http://%s.wikipedia.org/wiki/%s'

ROCK_FOLDER = 'resources/rock/'

LANGUAGE_PT = 'pt'
LANGUAGE_EN = 'en'

import glob

def get_image(word, wiki=False):
    """Acha uma imagem para uma palavra
    word: palavra em português
    wiki: se wiki=True e imagem não existe nas pasta img, então baixa figura da wikipedia
    return caminho para a imagem; None se palavra não tem imagem (ou se não achar na wikipedia)
    """
    folder = "resources/img/"
    word = word.replace(" ", "_")
    list = glob.glob("%s%s.*" % (folder, word))
    if list:
        return list[0]
    else:
        if wiki:
            try:
                img_url = from_wikipedia(word)
            except:
                return None
            if img_url:
                img_url = unicode(img_url)
                path = folder + word + _ext(img_url)
                download(img_url, path)
                return path
        return None

def _ext(path):
    """Returns the extension of the file (including the dot)
    path: it can be local or an URL, it doesn't matter
    """
    regex = '.*(\.[a-zA-Z]{3})'
    res = re.match(regex, path)
    if res:
        return res.group(1)
    else:
        return ''

def download(img_url, path):
    """Downloads an image in the path
    path: the absolute path to the image, including the image name
    """
    # todo extensão da imagem
    print "downloading " + img_url
    request = urllib2.Request(img_url, headers={'User-Agent' : "Magic Browser"})
    data = urllib2.urlopen(request).read()
    f = open(path, 'w')
    f.write(data)
    f.close()

def from_wikipedia(word):
    """Returns the link of a figure in the verbet of 'word' (a string)
    For example, passing word='cavalo' it is expected to get a horse figure
    If no figure is found, None is returned
    By default the words are searched in the Wikipedia in Portuguse; the second try is the English Wikipedia
    To change the language, set the language.LANGUAGE variable
    """ 
    try:
        url = BASE_URL % (LANGUAGE_PT, word)
        request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        site = urllib2.urlopen(request)
    except:
        print '%s does not exist in the wikipedia-%s' % (word, LANGUAGE_PT)
        try: 
            url = BASE_URL % (LANGUAGE_EN, word)   
            request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
            site = urllib2.urlopen(request)
        except:
            print '%s does not exist in the wikipedia-%s' % (word, LANGUAGE_EN)
            return None
    soup = BeautifulSoup(site)
    img_src = soup.find("a", { "class" : "image" }).findChild('img').get('src')
    return 'http://' + img_src.replace('//', '')

def rock():
    """Pega uma imagem da pasta rock aleatoriamente"""
    figures = os.listdir(ROCK_FOLDER)
    random.shuffle(figures)
    return ROCK_FOLDER + figures[0]

if __name__ == "__main__":
#    print get_image(sys.argv[1], True)
    print rock()

