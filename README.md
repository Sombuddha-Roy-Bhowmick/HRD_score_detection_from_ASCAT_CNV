# HRD_score_detection_from_ASCAT_CNV
Install ASCAT (Allele-Specific Copy Number Analysis of Tumors), following instructions: https://github.com/VanLoo-lab/ascat

Please cite the following paper: Van Loo P, Nordgard SH, Lingjærde OC, et al. Allele-specific copy number analysis of tumors. Proc Natl Acad Sci U S A. 2010;107(39):16910-16915. doi:10.1073/pnas.1009843107


Install scarHRD, following the instructions: https://github.com/sztup/scarHRD

Please cite the following paper: Sztupinszki et al, Migrating the SNP array-based homologous recombination deficiency measures to next generation sequencing data of breast cancer, npj Breast Cancer, https://www.nature.com/articles/s41523-018-0066-6.

# Code
Rscript Ploidy.R  

python scarHRD_input_formatting.py  

Rscript scarHRD.R

# Description

TumorSample-A.segments.txt (ASCAT Output - Tumor Segment File)

Ploidy.R (Extracts the ploidy value from another ASCAT Output - ASCAT_objects.Rdata)

scarHRD_input_formatting.py (Reformats the input - TumorSample-A.segments.txt into the desired input for scarHRD tool)

scarHRD.R (Gives the genomic scar scores)

Sample Output: HRD_Score.txt

# Output

HRD	Telomeric AI	LST	HRD-sum

14	19	15	48

For detailed description, please refer to the official github page of scarHRD.







