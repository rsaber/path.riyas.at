#!/usr/bin/python3

import os
import glob
from collections import namedtuple
import pytoml as toml

# only supports two level site structure

itins = []

site_structure = {}

path = 'itins/'

for itin_path in glob.glob( os.path.join(path, '*.toml') ):
    with open(itin_path, "rb") as toml_file:
        obj = toml.load(toml_file)

    if obj['country'] not in site_structure:
        site_structure[obj['country']] = []
    site_structure[obj['country']].append(obj)

# create folders

output_dir = '_site'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for country, toml_obj in site_structure.items():
    country_path = os.path.join(output_dir, country)
    if not os.path.exists(country_path):
        os.makedirs(country_path)
    
    