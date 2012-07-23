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
import words, figures
import sched
from threading import Timer, Thread

class Round(object):

    def __init__(self, max_palavras, interval, names, lists, interface, img_from_wiki):
        self.max_palavras = max_palavras # quantas palavras por rodada
        self.interval = interval # quantos segundos por palavra
        self.names = names # nomes dos jogadores
        self.interface = interface # interface gráfica
        self.img_from_wiki = img_from_wiki # boolean que indica se imagens vão ser carregadas da wikipedia
        self.words = words.Words(names, lists, max_palavras)
        self.figures = {} # key is word, and value figure path
        self.count = 0

    def start(self):
        RoundLoader(self).start()
        self.interface.start()

    def refresh(self):
        word = self.words.next()
        img_path = None
        if self.figures.has_key(word):
            img_path = self.figures[word] 
        self.interface.print_word(word, img_path)
        self.count += 1
        if (self.count < self.max_palavras):
           Timer(self.interval, self.refresh, ()).start() 
        else:
           Timer(self.interval, self.finish, ()).start() 

    def finish(self):
        self.interface.stop()

    def load_figures(self):
        for w in self.words.words:
            self.figures[w] = figures.get_image(w, self.img_from_wiki)
        print 'Figures loaded'
        self.interface.rock()

class RoundLoader(Thread):

    def __init__(self, round):
        """round -- Round object"""
        Thread.__init__(self)
        self.round = round

    def run(self):
        self.round.load_figures() 
        Timer(self.round.interval, self.round.interface.start_clock, ()).start()
        Timer(self.round.interval, self.round.refresh, ()).start()
        

if __name__ == "__main__":
    
    print "Let's rock!"
    round = Round(10, 4)
    round.start()



