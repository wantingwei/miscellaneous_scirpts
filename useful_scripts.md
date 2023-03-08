# Some useful scripts for data processing

### 1. How to rename a batch files in the directory
After received data from biotech, there always suffix at the end of each file.To minimize the workload, I will change the file name in to same format.This code helps to replace the undesired text in the name.<br>
``` %%bash``` <br>
```path_with_reads='data_output_redo/'``` <br>
```mkdir data_output_redo``` <br>
```cd $path_with_reads``` <br>
```for f in *.fastq.gz; do mv "$f" "${f/name_you_to_select/the_replace_string}"; done ``` <br>
eg. ```for f in *.fastq.gz; do mv "$f" "${f/_S*_L003_R1_001/_R1}"; done ``` <br>
eg. ```for f in *.fa; do mv "$f" "${f/c_consensus/c}"; done ``` <br>
using sed to remove all the symbol ```for f in *.fa; do sed 's/_/-/g';done```<br>

## 2.How to remove duplicate string in a .txt file
This scripts is super helpful for generate states.txt file, you don't want to submit a same job twice,so this scirpt will help you avoid having duplicate name in the states.txt file <br>
``` %%bash``` <br>
``` awk '!seen[$0]++' file.name ```

## 3.How to use .txt file to select specific file in to a different folder
first, you need to generate a .txt file contain all the file name that you are interested <br>
eg. nano test_script.txt  <br>
you can do ```mv``` or ```cp``` the select file in to a folder, here the path of the folder is ```/Users/Wanting/Desktop/test_case/folder```<br>
``` %%bash``` <br>
``` for fileName in `cat test_script.txt`; do cp $fileName /Users/Wanting/Desktop/test_case/folder; done ```

## 4. using sed to rename string in the text (mainly for snpEff)
solution link : https://github.com/pcingola/SnpEff/wiki/ERROR_CHROMOSOME_NOT_FOUND <br>
sometimes you will have special characters in the orginal text, use \ at the front at each character <br>
the orginal text are A/California/04/2009|NS <br>
``` sed "s/A\/California\/04\/2009\|NS/A_CALIFORNIA_04_2009_NS/g" > ${sample}_lofreq.vcf ```

# 5. adding suffix in file name 
``` for file in *.fa; do mv "$file" "${file%.fa}-fluA-H1.fa" ``` <br>

