#!/usr/bin/env python3

import os
import oyaml as yaml
import csv
import pandas as pd

# make an empty dictionary:


file = csv.reader('/Users/jwalla12/Repositories/refchef_parser/tests/data/new_references.csv')

new_keys = ['timestamp', 'command', 'name', 'common', 'taxon_id', 'organism', 'organization', 'custom', 'description',
            'ensembl_rel', 'genbank', 'refseq', 'component']

with open('/Users/jwalla12/Repositories/refchef_parser/tests/data/new_references.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    ref_list = []
    for row in reader:
        ref_list.append(row)
    new_list = []
    for d in ref_list:
        zipped = zip(new_keys, d.values())
        new_dict = {}
        for k, v in zipped:
            new_dict[k] = v
        new_list.append(new_dict)  # just incase we have more than 1 entry at a time....
    print(new_list)

# new_dict will work for now bc there's only 1 dict but would otherwise need to do a for loop on the new list
new_dict = new_list[0]
yaml_name = new_dict.get('name')
yaml_dict = {
    new_dict.get('name'):
        {'metadata':
             {'name': new_dict.get('name'),
              'common_name': new_dict.get('common'),
              'custom': new_dict.get('custom'),
              'description': new_dict.get('description'),
              'downloader': 'joselynn wallace',
              'ncbi_taxon_id': new_dict.get('taxon_id'),
              'ensembl_release_number': new_dict.get('ensembl_rel'),
              'accession':
                  {'genbank': new_dict.get('genbank'),
                   'refseq': new_dict.get('refseq')},
              'organism': new_dict.get('organism'),
              'organization': new_dict.get('organization')
              },
         'levels':
             {'references':
                 [
                     {
                         'component': new_dict.get('component'),
                         'commands': [new_dict.get('command')]
                     }
                 ]
             }
         }
}
f = open('/Users/jwalla12/Repositories/refchef_parser/tests/data/test.yaml', 'w+')
yaml.dump(yaml_dict, f, allow_unicode=True)