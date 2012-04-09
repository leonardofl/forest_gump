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

import random

WORDS_FILE = "resources/words"

class Words(object):

    def __init__(self, names, max_palavras):
        self.count = -1
        self.words = self.__retrieve_words_from_file()
        random.shuffle(self.words)
        self.words = self.words[0:max_palavras]
        selected_names = self.select_names(names)
        for name, i in zip(selected_names, range(0,2)): # adiciona nomes dos jogadores na lista de palavras
            self.words[i] = name
        random.shuffle(self.words)

    def select_names(self, names):
        """Recebe uma lista de nomes e devolve uma lista com UM ou DOIS desses nomes"""
        random.shuffle(names)
        selected = [names[0]]
        if random.random() > 0.7: # 30% de chances de ter dois nomes
            selected.append(names[1])
        return selected

    def __retrieve_words_from_file(self):
        """Lê o arquivo resources/words e retorna uma lista"""
        file = open(WORDS_FILE)
        wds = file.read().splitlines()
        file.close()
        return wds

    def __iter__(self):
        return self

    def next(self):
        if (self.count == len(self.words)-1):
            raise StopIteration
        self.count += 1
        return self.words[self.count]


if __name__ == "__main__":
    
    print "Let's rock!"
    for word in Words():
        print word


