# Some codes that I thing are useful for data processing

### 1. How to rename a batch files in the directory
``` %%bash``` <br>
```path_with_reads='data_output_redo/'``` <br>
```mkdir data_output_redo``` <br>
```cd $path_with_reads``` <br>
```for f in *.fastq.gz; do mv "$f" "${f/name_you_to_select/the_replace_string}"; done ```


## 2.How to remove duplicate string in a .txt file

``` %%bash``` <br>
``` awk '!seen[$0]++' file.name ```

## 3.How to using .txt file to select specific file in to a different folder

first, you need to generate a .txt file contain all the file name that you are interested <br>
eg. nano test_script.txt  <br>
you can do ```mv``` or ```cp``` the select file in to a folder, here the path of the folder is ```/Users/Wanting/Desktop/test_case/folder```<br>
``` %%bash``` <br>
``` for fileName in `cat test_script.txt`; do cp $fileName /Users/Wanting/Desktop/test_case/folder; done ```
