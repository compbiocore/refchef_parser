#!/usr/bin/env python3

import os
import re
import oyaml as yaml
import csv
# import pandas as pd
import json
import ast

# make an empty dictionary:


#file = csv.reader('/Users/jwalla12/Repositories/cbc-references-refchef/new_ref.yaml')

#new_keys = ['timestamp', 'command', 'name', 'common', 'taxon_lsid', 'organism', 'organization', 'custom', 'description',
            # 'ensembl_rel', 'genbank', 'refseq', 'component']
with open('/Users/jwalla12/Repositories/cbc-references-refchef/new_ref.yaml') as f:
    data = f.read()
    datajson = json.loads(data)
    yaml_level = datajson.get('level')
    yaml_commands = datajson.get('Commands')
    print(yaml_commands)
    print(datajson)
    yaml_dict = {
        datajson.get('name'):
            {'metadata':
                 {'name': datajson.get('name'),
                  'common_name': datajson.get('common'),
                  'custom': datajson.get('custom'),
                  'description': datajson.get('description'),
                  'downloader': 'joselynn wallace',
                  'ncbi_taxon_id': datajson.get('taxon_id'),
                  'ensembl_release_number': datajson.get('ensembl_rel'),
                  'accession':
                      {'genbank': datajson.get('genbank'),
                       'refseq': datajson.get('refseq')},
                  'organism': datajson.get('organism'),
                  'organization': datajson.get('organization'),
                  'category': datajson.get('category')
                  },
                'levels':
                    {yaml_level:
                     [
                         {
                             'component': datajson.get('component'),
                             'commands': [datajson.get('Commands')]
                         }
                     ]
                 }
             }
    }
    out = open('/Users/jwalla12/Repositories/cbc-references-refchef/new_parsed.yaml', 'w+')
    yaml.dump(yaml_dict, out, allow_unicode=True)


    #          'levels':
    #              {'references':
    #                  [
    #                      {
    #                          'component': datajson.get('component'),
    #                          'commands': [datajson.get('command')]
    #                      }
    #                  ]
    #              }
    #          }
    # }
    #f = open('/Users/jwalla12/Repositories/refchef_parser/tests/data/test.yaml', 'w+')
    #yaml.dump(yaml_dict, f, allow_unicode=True)