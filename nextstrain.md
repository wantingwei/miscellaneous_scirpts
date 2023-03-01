# using nextstrain augur for phylogenetic anlaysis 
for this scirpt I wil try to include all the detail to increase further reproduciblity. you won't need to use all the scirpts, feel free to use modify this scirpt to fit best on your dataset. <br>
1. activate nextstrian enviroment in your terminal <br>
```conda activate nextstrain``` <br>
```jupyter notebook``` <br>
2. working on your metadata <br>
```https://docs.nextstrain.org/projects/augur/en/stable/faq/metadata.html``` you will able to find all the detail info from the link <br> 
Nextstrian does not recommend using excel to modify your data, but if you are using excel the best way is to resave the file using python or R.
```meta_data = pd.read_csv('marshfield_ref_metadata.csv')```
```meta_data.rename( columns={0 :'strain',1 :'date',2 :'region',3 :'country'}, inplace=True )``` adding header for the csv file based on the column name you have. it is important to do this step, other wise augur will not able to read the metadata <br>
```meta_data.to_csv("marshfield_ref_metadata_rf.csv", sep='\t', index=False)```
