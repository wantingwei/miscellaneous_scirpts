## please check the computer setting and docker setting before use this pipeline

### Generate sample sheet 
```
python3 ./fastq_dir_to_samplesheet.py <FASTQ_DIR> samplesheet.csv
```
### Using QIAseq
```
/Users/wwei54/BioInformatics/nf/nextflow run nf-core/viralrecon \
--input prolonged_infection_hamster_viralrecon_metadata.csv \
--outdir output \
--platform illumina \
--protocol amplicon \
--genome 'MN908947.3' \
--gff \
--primer_bed DIRECTwithBoosterAprimersfinal.bed \
--primer_left_suffix '_LEFT' \
--primer_right_suffix '_RIGHT' \
--ivar_trim_offset 5 \
--skip_assembly \
-p low_freq_ivar.params \
-profile docker 
-resume {run name}
```

### Using artic protocol
```
/Users/wwei54/BioInformatics/nf/nextflow run nf-core/viralrecon \
--input hamster_1.csv \
--outdir hamster_1_output \
--platform illumina \
--protocol amplicon \
--genome MN908947.3 \ 
--primer_set artic \
--primer_set_version 4.1 \
--ivar_trim_offset 5 \
--skip_assembly \
-c low_freq_ivar.config \
-profile docker \
-resume desperate_panini 
```
### config file change the default variant calling parameters
```
process {
        withName: 'IVAR_VARIANTS' {
            ext.args = '-t 0.01 -q 30 -m 200'
        }
    }
```

viralrecon with modified gff
```nextflow run nf-core/viralrecon \
-config run_configs/viralrecon-hpc.config \
-profile singularity \
--input run_inputs/test/samplesheet.csv \
#--gff run_inputs/MN908947.3-orf1a-orf1b-gene-split.gff \
--outdir run_results/test \
--platform illumina \
--protocol amplicon \
--genome 'MN908947.3' \
--primer_set artic \
--primer_set_version 5.3.2 \
--skip_assembly \
--skip_asciigenome \
--schema_ignore_params 'genomes,primer_set_version' \
 -resume
```
