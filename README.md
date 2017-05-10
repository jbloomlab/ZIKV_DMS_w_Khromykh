# Deep mutational scanning of ZIKV Natal strain

## Authors
Yin Xiang Setoh, Jesse Bloom, [Alexander Khromykh](https://staff.scmb.uq.edu.au/staff/alexander-khromykh) 

## Goal
Yin and Alexander are performing deep mutational scanning of the Natal strain of Zika virus. 
Initially, they are examining domain III of the E protein.
The first goal is to do barcoded subamplicon sequencing of the mutant library of this region.

## Organization

### Analysis notebooks
The analysis is performed by the iPython notebook [analyze_E_DIII_subamplicons.ipynb](analyze_E_DIII_subamplicons.ipynb). 
This notebook describes what is doing and summarizes the results and conclusions.
The created files are in the `./results/` subdirectory.

### Input files
The input files used in the analysis are all found in the `./data/` subdirectory. 
Specifically:

1. `./data/fastq/` contains the FASTQ files from the deep sequencing:

    * `J999_S90_L001_R*_001.fastq.gz` gives the files received from Yin on May-1-2017 for sequencing the E protein domain III.

2. `./data/seqs/` contains reference sequences:

    * `NatalEDIII.fa` contains the sequence of the Natal ZIKV E domain III obtained from Yin on May-1-2017.

3. `./data/images/` contains input images:

    * `ZIKV_E_DIII.pdf` is a schematic of the E domain III sequencing obtained from Yin on May-1-2017.

### Code
Some Python modules used by the analysis notebooks are in `./pymodules/`.

## Results and Conclusions
Conclusions are at the end of the iPython notebook [analyze_E_DIII_subamplicons.ipynb](analyze_E_DIII_subamplicons.ipynb).

## To-do
