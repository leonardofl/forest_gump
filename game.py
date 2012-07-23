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

import gui
import os

LISTS_DIR = "resources/lists/"

def __get_available_lists():
    """Retrieve the names of the files in the lists dir"""
    lists = os.listdir(LISTS_DIR)    
    return filter(lambda l: not l[-1]=='~', lists) # discard files ended with '~' (backups)

if __name__ == "__main__":
    lists = __get_available_lists()
    interface = gui.Interface(lists)
    interface.start()

