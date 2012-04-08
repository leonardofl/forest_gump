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
import time
from threading import Timer

class Round(object):

    def __init__(self, max_palavras, interval):
        self.max_palavras = max_palavras # quantas palavras por rodada
        self.interval = interval # quantos segundos por palavra
        self.words = words.Words()
        self.count = 0

    def start(self):
        Timer(self.interval, self.refresh, ()).start()

    def refresh(self):
        print self.words.next()
        self.count += 1
        if (self.count < self.max_palavras):
           Timer(self.interval, self.refresh, ()).start() 
        else:
           Timer(self.interval, self.finish, ()).start() 

    def finish(self):
        print 'ACABOU!'

if __name__ == "__main__":
    
    print "Let's rock!"
    round = Round(10, 4)
    round.start()

