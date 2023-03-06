
Using Nextstrain Augur for Phylogenetic Anlaysis 
================================================
This tutorial is for anyone who wants to use nextstrain for baisc phylogentic anlsyis. No coding experience is requried. I will try to include a lot of details to increase reproduciblity. You won't need to use all the command, feel free to use modify this scirpt to fit best on your dataset. <br>

Prerequisites
=============

[Install Jupyter notebook](https://jupyter.org/install) <br>
[Nextstrain Installation tutorial](https://docs.nextstrain.org/projects/augur/en/stable/installation/installation.html) These instructions will install all of the software you need to complete this tutorial and others.

Preprocess
===========
Before actually moving to the Augur pipeline you need to prepared the input file, including the .fasta and metadata.csv <br>
I will guide you go through the pre-process step.<br>
1. Activate nextstrian enviroment in your terminal <br>
```%%bash
conda activate nextstrain 
jupyter notebook
```
2. Working on your metadata <br>
[Preparing your Metadata](https://docs.nextstrain.org/projects/augur/en/stable/faq/metadata.html) you will able to find detail information from the link.
Nextstrian does not recommend using excel to modify your data, but if you are using excel the best way is to save the file using python or R. <br>
```
#open jupyter notebook
import pandas as pd
from datetime import datetime
```
```
meta_data = pd.read_csv('marshfield_ref_metadata.csv')
meta_data.rename( columns={0 :'strain',1 :'date',2 :'region',3 :'country'}, inplace=True ) 
#adding header for the csv file based on the column name you have. it is important to do this step, 
otherwise Augur will not able to read the metadata
meta_data.to_csv("marshfield_ref_metadata_rf.csv", sep='\t', index=False)
``` 
you will use the new csv file you generate as the metadata input <br>
3. Cleaning your fasta file
first you want to concat all the fasta file together <br>
```
%%bash
cat *.fa* > Sample_concat.fa 
``` 
Notes: make sure all your file name using "_" or "-" at same position
This step will concat all the sequence into one file, since we are mostly interested in building phylogenetic tree based on HA and NA. We need to subtract the HA and HA in to a new file. Another option, you can include a list only contains the name of you interested segment and input the list in augur.<br>
To subtract the gene segments from the ```Sample_concat.fa``` Simply download the ```phrase.sh``` file from this repo, and move it to the directory contain your file interest. Change the ```filename``` into your file name and run ```bash phrase.sh ``` <br>
You will get 8 files at the end,each file contains all the gene segment from sample sequence.

Tutorial
===========
I would recommend using jupyter notebook for running nextstain.
``` %%bash <br>

  augur index \ <br>
  --sequences gene_HA.fasta \  <br>
  --output marshfieldz_HA_index.tsv <br> 
  
  augur filter \  <br>
  --sequences gene_HA.fasta \  <br>
  --sequence-index marshfieldz_HA_index.tsv \  <br>
  --metadata 19_20_marshfield_metadata_H1N1.csv \  <br>
  --output marshfield_HA_filtered.fasta \  <br>
  
  augur align \ <br>
  --sequences marshfield_HA_filtered.fasta \ <br>
  --reference-sequence A\:Singapore\:GP1908\:2015\:H1N1_HA.fasta \ <br>
  --output marshfield_HA_aligned.fasta \ <br>
  
  augur tree \ <br>
  --alignment marshfield_HA_aligned.fasta \ <br>
  --output marshfield_HA_tree_raw.nwk 
  
  augur refine \ <br>
  --tree marshfield_HA_tree_raw.nwk \ <br>
  --alignment marshfield_HA_aligned.fasta \
  --metadata 19_20_marshfield_metadata_H1N1.csv \
  --output-tree marshfield_tree_HA.nwk \
  --output-node-data branch_lengths.json \
  --timetree \
  --coalescent opt \
  --date-confidence \
  --date-inference marginal \
  --clock-filter-iqd 4
  
  augur ancestral \
  --tree marshfield_tree_HA.nwk \
  --alignment marshfield_HA_aligned.fasta \
  --output-node-data marshfield_HA_node.json \
  --inference joint
  
  augur export v2 \
  --tree marshfield_tree_HA.nwk \
  --metadata 19_20_marshfield_metadata_H1N1.csv \
  --node-data branch_lengths.json \
              marshfield_HA_node.json\
  --output auspice/marshfield_19_20_H1N1_HA.json \
  --maintainers Wanting Wei

