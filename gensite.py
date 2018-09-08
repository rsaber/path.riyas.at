#!/usr/bin/python3

import os
import glob
from collections import namedtuple
import pytoml as toml

Itinerary = namedtuple('Itinerary', 'path country city')

itins = []

site_structure = {}

path = 'itins/'
for toml_itin in glob.glob( os.path.join(path, '*.toml') ):

    cats = os.path.splitext(os.path.basename(toml_itin))[0].split('_')

    itins.append(
        Itinerary(
            toml_itin,
            os.path.splitext(os.path.basename(toml_itin))[0].split('_')[0],
            os.path.splitext(os.path.basename(toml_itin))[0].split('_')[1]
        )
    )

print(itins)

for itin in itins:
    with open(itin.path, "rb") as toml_file:
        obj = toml.load(toml_file)
    print(obj)