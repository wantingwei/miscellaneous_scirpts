
Using Nextstrain Augur for Phylogenetic Anlaysis 
================================================
This tutorial is for anyone who wants to use nextstrain for baisc phylogentic anlsyis. No coding experience requried. I will try to include a lot of details to increase reproduciblity. You won't need to use all the command, feel free to use modify this scirpt to fit best on your dataset. <br>

Prerequisites
=============

[Install Jupyter notebook](https://jupyter.org/install)
[Nextstrain Installation tutorial](https://docs.nextstrain.org/projects/augur/en/stable/installation/installation.html) These instructions will install all of the software you need to complete this tutorial and others.

Tutorial
===========
1. Activate nextstrian enviroment in your terminal <br>
```%%bash
conda activate nextstrain 
jupyter notebook
```
2. Working on your metadata <br>
[Preparing your Metadata](https://docs.nextstrain.org/projects/augur/en/stable/faq/metadata.html) you will able to find detail information from the link 
Nextstrian does not recommend using excel to modify your data, but if you are using excel the best way is to save the file using python or R. <br>
```
#open jupyter notebook
import pandas as pd
from datetime import datetime
```
```
meta_data = pd.read_csv('marshfield_ref_metadata.csv')
meta_data.rename( columns={0 :'strain',1 :'date',2 :'region',3 :'country'}, inplace=True ) 
#adding header for the csv file based on the column name you have. it is important to do this step, otherwise Augur will not able to read the metadata
meta_data.to_csv("marshfield_ref_metadata_rf.csv", sep='\t', index=False)
``` 
you will use the new csv file you generate as the metadata input
3. cleaning your fasta file
first you want to concat all the fasta file together <br>
```
%%bash
cat *.fa* > Sample_concat.fa 
``` 
This step will concat all the sequence into one file, since we are mostly interested in building phylogenetic tree based on HA and NA we need to subtract the HA and HA in to a new file. Another option, you can include a list only contains the name of you interested segment and input the list in augur.<br>
To subtract the gene segments from the ```Sample_concat.fa``` Simply download the ```phrase.sh``` file from this repo, and move it to the directory contain your file interest. Change the ```filename``` into your file name and run ```bash phrase.sh ``` <br>
You will get 8 files at the end,each file contains the gene segment from each sample sequence.

