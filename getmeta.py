from metapub import PubMedFetcher
import metapub
import subprocess
from rich import print
import time

def get_pmdi_from_doi(doi):
    doi = doi.rstrip()
    bashCommand = f"convert doi2pmid {doi}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()
    pmdi = str(output).split("PMID:  ")[0].split("\\")[0]
    if "PMDI" in pmdi:
        return pmdi, output, process
    else:
        pmdi = "None"
        return pmdi,output,process

with open('doi_list.txt') as f:
    lines = f.readlines()

a_array = []
pmdi_array =[]
for doi in lines:
    doi = doi.rstrip()
    pmdi, output, process = get_pmdi_from_doi(doi)
    if pmdi == "None":
        a_array.append("Not Found")
        pmdi_array.append("Not Found")
        print(f"PMDI for{doi} not found")
    else:
        print(f"getting abstract for {doi} | {pmdi}")
        fetch = PubMedFetcher()
        a=fetch.article_by_pmid(pmdi)
        a_array.append(a.abstract)
        pmdi_array.append(a)

        time.sleep(2)
