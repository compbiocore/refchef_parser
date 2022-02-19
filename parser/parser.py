#!/usr/bin/env python3

import os
import oyaml as yaml
import csv
import pandas as pd

#make an empty dictionary:


file = csv.reader('/Users/jwalla12/Repositories/refchef_parser/tests/data/new_references.csv')

new_keys = ['timestamp', 'command', 'name', 'common', 'taxon_id', 'organism', 'organization', 'custom', 'description', 'ensembl_rel', 'genbank', 'refseq', 'component']

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
            new_list.append(new_dict)
    print(new_list)

yaml_dict = {}






yaml_dict={}
yaml_dic
d.get('refseq')
d.get('release')

        for d in lst:
            d['Make'] = d.pop('Label')
            d['Code'] = d.pop('Value')
        for new_key in new_keys:
            for k,v in d.items():
                d[new_key] = d.pop(k)
                print(d)
    for d in ref_list:
        for (k,v) in zip(d.items, new_keys):
            print(k,v)


            for (lat, lon) in zip(latitudes, longitudes):

            print(k)

        a_dict[new_key] = a_dict.pop(old_key)


        In[5]:
        import csv

        ...:
        with open("in.csv") as csvfile:
            ...: reader = csv.DictReader(csvfile, delimiter=" ")
        ...:
        for dct in map(dict, reader):
            ...: print(dct)
        ...: print(f"{dct['first_name']} {dct['last_name']}")


        import csv

        with open('videos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['id'])

>>> with open('names.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['first_name'], row['last_name'])


new_keys = ['timestamp', 'command', 'name', 'common', 'taxon_id', 'organism', 'organization', 'custom', 'description', 'ensembl_rel', 'genbank', 'refseq', 'component']
test=file.iloc[0].tolist()

file_string = file.to_string()

{file_dict.get('name'):['metadata', 'levels']}

file2 = file.rename(columns={list(file):keys}, inplace = TRUE)

test = file.loc[[1]]
file.iloc[0]

csv_reader = csv.reader(file)
next(csv_reader)
for row in csv_reader:
    print(row)











with open("/Users/jwalla12/Repositories/refchef_parser/tests/data/new_references.csv") as form_csv:
    form=csv.reader(form_csv)
    for row in form:
        print(','.join(row))

    file = open('sample.csv')

    csv_reader = csv.reader(file)

    next(csv_reader)

    for row in csv_reader:
        print(row)





    form_read = csv.DictReader(form_csv)
    for row in form_read:
        print(row)

for row in csv.DictReader("/Users/jwalla12/Repositories/refchef_parser/tests/data/new_references.csv"):
    print(row)


    u = open("/Users/jwalla12/Repositories/refchef_parser/tests/data/new_references.csv", "r+")
    # read each line
    ulines = u.readlines()
    print(ulines)
    # remove trailing whitespace
    #u_stripped = [l.rstrip() for l in u.readlines()]
    #print(u_stripped)
    # make a dictionary
    #d = {}
    #for item in u_stripped:
    #    key, value = item.split('\t')
    #    d[key] = (value)
