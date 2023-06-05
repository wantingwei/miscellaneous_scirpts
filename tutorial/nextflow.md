## How to download nextflow on a new computer
### I would recommned download X-code before you start anything in terminal. ``` $ xcode-select --install ```
1. make a directory called Bioinformatics for better organization
```mkdir Bioinformaticas```
2. Download the nextflow from the website and follow the instruction. https://www.nextflow.io/docs/latest/getstarted.html#installation
run ```./nextflow``` to verify the program is sucessfully installed
3. create ~/.zshrc file
If you have a new computer make sure create the .zshrc file. ``` nano ~/.zshrc```
export the path of nextflow in the file, ```e.g. export PATH=$PATH:/Users/wwei54/Bioinformatics ```
since the nextflow is an executable itself do need to specifcy like ```PATH=$PATH:/Users/wwei54/Bioinformatics/nextflow ```
4.restart the file, you can re-open the terminal or do ```source ~/.zshrc```
5.Navigate to another directory, and test whether nextflow has been succusfully install
