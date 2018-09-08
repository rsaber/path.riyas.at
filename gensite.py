#!/usr/bin/python3

import os
import glob
from collections import namedtuple
import pytoml as toml

from shutil import copytree, rmtree
    
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

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

if os.path.exists(output_dir):
    rmtree(output_dir)
os.makedirs(output_dir)

try:
    copytree(os.path.join('templates', 'css'), os.path.join(output_dir, 'css'))
    copytree(os.path.join('templates', 'fonts'), os.path.join(output_dir, 'fonts'))
except:
    pass

nav = {}

# populate navbar (probably couldve been done in file search or site_structure)

for country, itinaries in site_structure.items():
    nav[country] = []
    for itinerary in itinaries:
        filename = '{}_{}.html'.format(country, itinerary['itinerary_name'])
        output_path = os.path.join(output_dir, filename)
        nav[country].append(
            {
                'itinerary_name': itinerary['itinerary_name'],
                'link': filename
            }
        )

for country, itinaries in site_structure.items():
    for itinerary in itinaries:
        output_path = os.path.join(output_dir, '{}_{}.html'.format(country, itinerary['itinerary_name']))
        template = env.get_template('template.html')
        output = template.render(nav=nav, itin=itinerary)
        with open(output_path, "w") as f:
            f.write(output)
        
        