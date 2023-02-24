# Some codes that I thing are useful for data processing

### 1. How to rename a batch files in the directory
%%bash
path_with_reads='data_output_redo/' 
#mkdir data_output_redo
cd $path_with_reads

for f in *.fastq.gz; do mv "$f" "${f/name_you_to_select/the_replace_string}"; done


## 2.How to remove duplicate string in a text file

awk '!seen[$0]++' file.name

## 3.How to using .txt file to select spcific file in to a different folder
#first, you need to generate a .txt file contain all the file name that you are interested 
#eg. nano test_script.txt
#you can do mv or cp the select file in to a folder, here the path of the folder is /Users/Wanting/Desktop/test_case/folder

for fileName in `cat test_script.txt`; do cp $fileName /Users/Wanting/Desktop/test_case/folder; done
