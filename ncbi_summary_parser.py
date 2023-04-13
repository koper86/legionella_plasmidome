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

plasmids_df.to_csv("/home/user/PycharmProjects/Microbial_genomics_analysis/Legionella/legionella_plasmidome/2023_01_04_NCBI_nuccore_plasmids_list.csv",
                   index=False,
                   sep="\t")
