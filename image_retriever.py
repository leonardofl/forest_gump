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

import glob

def get_image(word):
    """Acha uma imagem para uma palavra
    word: palavra em português
    return caminho para a imagem
    """
    folder = "resources/img/"
    word = word.replace(" ", "_")
    list = glob.glob("%s%s.*" % (folder, word))
    if list:
        return list[0]
    else:
        return None

if __name__ == "__main__":
    print get_image("escola")
    print get_image("python")
    print get_image("maçã")
    print get_image("quinta e breja")
    print get_image("naotem")


