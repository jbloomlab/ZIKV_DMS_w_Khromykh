# Deep mutational scanning of ZIKV Natal strain

## Authors
Yin Xiang Setoh, Jesse Bloom, [Alexander Khromykh](https://staff.scmb.uq.edu.au/staff/alexander-khromykh) 

## Goal
Yin and Alexander are performing deep mutational scanning of the Natal strain of Zika virus. 
Initially, they are examining domain III of the E protein.

## Organization

### Analysis notebooks
Each analysis is in its own iPython notebook.

  1. [analyze_E_DIII_subamplicons.ipynb](analyze_E_DIII_subamplicons.ipynb) describes an initial analysis of the barcoded subamplicon sequencing of a region of the E DIII.

### Input files
The input files used in the analysis are all found in the `./data/` subdirectory. 
Specifically:

1. `./data/fastq/` contains the FASTQ files from the deep sequencing:

    * `J999_S90_L001_R*_001.fastq.gz` gives the files received from Yin on May-1-2017 for sequencing the E protein domain III.

    * `C636DMS_R*_001.fastq.gz` and `vero8dpt_R*_001.fastq.gz` are files received from Yin on June-15-2015 that contain the results of passing the E protein domain III library in C636 cells and Vero cells.

2. `./data/seqs/` contains reference sequences:

    * `NatalEDIII.fa` contains the sequence of the Natal ZIKV E domain III obtained from Yin on May-1-2017. This actually had DIII plust some region upstream.

    * `NatalEDIIIonly.fa` contains the sequence of **only** the Natal ZIKV E domain III obtained from Yin on June-15-2017.

3. `./data/images/` contains input images:

    * `ZIKV_E_DIII.pdf` is a schematic of the E domain III sequencing obtained from Yin on May-1-2017.

### Code
Some Python modules used by the analysis notebooks are in `./pymodules/`.

## Results and Conclusions
Conclusions are found in each iPython notebook.

## To-do
