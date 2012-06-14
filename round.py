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

import words
import sched
from threading import Timer, Thread

class Round(object):

    def __init__(self, max_palavras, interval, names, interface):
        self.max_palavras = max_palavras # quantas palavras por rodada
        self.interval = interval # quantos segundos por palavra
        self.names = names # nomes dos jogadores
        self.interface = interface # interface gráfica
        self.words = words.Words(names, max_palavras)
        self.count = 0

    def start(self):
        Timer(self.interval, self.interface.start_clock, ()).start()
        Timer(self.interval, self.refresh, ()).start()
        self.interface.start()

    def refresh(self):
        word = self.words.next() 
        self.interface.print_word(word)
        self.count += 1
        if (self.count < self.max_palavras):
           Timer(self.interval, self.refresh, ()).start() 
        else:
           Timer(self.interval, self.finish, ()).start() 

    def finish(self):
        self.interface.stop()

if __name__ == "__main__":
    
    print "Let's rock!"
    round = Round(10, 4)
    round.start()

