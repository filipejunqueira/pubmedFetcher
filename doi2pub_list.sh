#!/bin/bash
conda init
conda activate "def"
input="doi_list.txt"
while IFS= read -r line; 
do
    echo $(convert doi2pmid $line)
    sleep 3
done < $input
