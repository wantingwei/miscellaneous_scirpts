
Using nextstrain augur for phylogenetic anlaysis 
================================================
This tutorial is for anyone who wants to use nextstrain but without any coding background. I wil try to include all the details to increase reproduciblity. you won't need to use all the command, feel free to use modify this scirpt to fit best on your dataset. <br>

Prerequisites
=============

(https://docs.nextstrain.org/projects/augur/en/stable/installation/installation.html) These instructions will install all of the software you need to complete this tutorial and others.

Tutorial
===========
1. activate nextstrian enviroment in your terminal <br>
```conda activate nextstrain``` <br>
```jupyter notebook``` <br>
2. working on your metadata <br>
```https://docs.nextstrain.org/projects/augur/en/stable/faq/metadata.html``` you will able to find all the detail info from the link <br> 
Nextstrian does not recommend using excel to modify your data, but if you are using excel the best way is to resave the file using python or R. <br>
```meta_data = pd.read_csv('marshfield_ref_metadata.csv')``` <br>
```meta_data.rename( columns={0 :'strain',1 :'date',2 :'region',3 :'country'}, inplace=True )``` adding header for the csv file based on the column name you have. it is important to do this step, other wise augur will not able to read the metadata <br>
```meta_data.to_csv("marshfield_ref_metadata_rf.csv", sep='\t', index=False)``` <br>
you will use the new csv file you generate as the metadata input
3. cleaning your fasta file
first you want to concat all the fasta file together <br>
```cat *.fa* > Sample_concat.fa ``` 
This step will concat all the sequence into one file, since we are mostly interested in building phylogenetic tree based on HA and NA we need to subtract the HA and HA in to a new file. Another option you can include a list only contains the name of you interested segment and input the list in augur.<br>
download the ```phrase.sh``` file from this repo, and move it to the directory contain your file interest. Change 

