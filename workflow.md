# Description of project


# Queries, data collection
## NCBI Entrez query
"Legionella"[Organism] AND ("unidentified plasmid"[Organism] OR plasmid[All Fields]) AND (ddbj_embl_genbank[filter] AND plasmid[filter])
Sequence length from 1000 to 10000000
download to file (summary format)

### NCBI summary parser to df

```python
import pandas as pd

plasmids_file_path = "/Legionella/legionella_plasmidome/2023_01_04_NCBI_nuccore_plasmids_list.txt"
with open(plasmids_file_path, 'r') as f:
    file_lines = f.readlines()

plasmids_df = pd.DataFrame(columns=['name', 'size', 'acc_number'])

for line in file_lines:
    if file_lines.index(line) % 4 == 0:
        name = line.strip("\n")
    elif file_lines.index(line) % 4 == 1:
        size = int(''.join(filter(str.isdigit, line)))
    elif file_lines.index(line) % 4 == 2:
        acc_number = line[:10]
        plasmids_df = plasmids_df.append({"name": name, "size": size, "acc_number": acc_number}, ignore_index=True)

plasmids_df.to_csv(
    "/home/user/PycharmProjects/Microbial_genomics_analysis/Legionella/legionella_plasmidome/2023_01_04_NCBI_nuccore_plasmids_list.csv",
    index=False,
    sep="\t")
```

```R
library(tidyverse)
plasmids_file_path <- "/home/user/PycharmProjects/Microbial_genomics_analysis/Legionella/plasmidome/2023_01_04_NCBI_nuccore_plasmids_list.csv"
plasmids_df <- read_tsv(plasmids_file_path)

legionella_plasmids_df <- plasmids_df %>% 
  filter(!str_detect(name, "Legionella adelaidensis"))

write_csv(legionella_plasmids_df, "/home/user/PycharmProjects/Microbial_genomics_analysis/Legionella/plasmidome/2023_01_04_NCBI_filtered_nuccore_plasmids_list.csv")
```
78 plasmids

## NCBI FTP RefSeq
https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/

plasmids.txt file
```R
library(tidyverse)
plasmids_file_path <- "/home/user/PycharmProjects/Microbial_genomics_analysis/Legionella/plasmidome/2023_01_04_NCBI_plasmids_list.txt"
plasmids_df <- read_tsv(plasmids_file_path)

legionella_plasmids_df <- plasmids_df %>% 
  filter(str_detect(Organism, "Legionella")) %>%
  filter(!str_detect(Organism, "Legionella adelaidensis"))

write_csv(legionella_plasmids_df, "/home/user/PycharmProjects/Microbial_genomics_analysis/Legionella/plasmidome/2023_01_04_NCBI_filtered_plasmids_list.csv")
```
64 plasmids
## Comparison of 2 datasets
```R
refseq_plasmids_path <- "/home/user/PycharmProjects/Microbial_genomics_analysis/Legionella/plasmidome/2023_01_04_NCBI_filtered_plasmids_list.csv"
nuccore_plasmids_path <- "/home/user/PycharmProjects/Microbial_genomics_analysis/Legionella/plasmidome/2023_01_04_NCBI_filtered_nuccore_plasmids_list.csv"

refseq_plasmids_df <- read_csv(refseq_plasmids_path)
nuccore_plasmids_df <- read_csv(nuccore_plasmids_path)

full_plasmids_df <- nuccore_plasmids_df %>%
  mutate(INSDC = gsub("\\..*","", acc_number)) %>% 
  full_join(refseq_plasmids_df)

```

