from utils import get_array_from_csv, get_meta_pubmed, import_bib
import pandas as pd
import numpy as np

list_attribute = ['ID','author','title','year', 'journal']
df = import_bib(file_path= 'bibliography_aminiotic_withDOi.bib')

selection = df[list_attribute]

# removing exceptions
exceptions = [4,22,23]
selection.drop(exceptions, axis=0,inplace=True)
selection = selection.reset_index(drop=True)
selection.to_csv('temp.csv', index=True)
title_list = selection['title'].to_list()
id_list = selection['ID'].to_list()
abstract_list = list.randoms(67)
i = 0
selection['abstract'] = abstract_list

# for id, title in zip(id_list,title_list):
#      print(f"First loop {i}")
#      pubmed_obj = get_meta_pubmed(title,tool="PubMedSearcher",email="myemail@ccc.com").abstract
#      abstract_list.append(pubmed_obj)
#      print(f"First loop {i} passed, id: {id}")
#      i = i+1
#

