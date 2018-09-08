#!/usr/bin/python3

import os
import glob
    
itins = []

path = 'itins/'
for itin in glob.glob( os.path.join(path, '*.toml') ):
    print "current file is: " + infile
    itins.append(itin)