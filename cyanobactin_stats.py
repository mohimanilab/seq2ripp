################################################################################
# Filename: cyanobactin_stats.py
# Author: Yi-Yuan Lee
# Date: 10.27.2020
# Description: Find out the distribution of cores in cyanobactin_full.fasta
################################################################################
import matplotlib.pyplot as plt
def read_file(file):
    headers = []
    seqs = []
    with open(file, 'r') as f:
        for line in f:
            if "_" in line:
                headers.append([int(x) for x in line.strip().split("_")[1:]])
                seqs.append(f.readline().strip())
            else:
                headers.append([0])
                seqs.append(f.readline().strip())
    return headers, seqs

def stats(headers):
    max_cores = 0.0
    max_len   = 0.0
    min_cores = float('inf')
    min_len   = float('inf')
    all_cores_length = []
    for line in headers:
        max_cores = line[0] if line[0] > max_cores else max_cores
        min_cores = line[0] if line[0] < min_cores else min_cores
        for i in range(line[0]):
            begin = line[i*2 + 1]
            end = line[(i+1)*2]
            length = end - begin
            all_cores_length.append(length)
            max_len = length if length > max_len else max_len
            min_len = length if length < min_len else min_len
    print("Max number of cores:", max_cores, "\nMin number of cores:", min_cores,\
            "\nMax length of cores:", max_len, "\nMin length of cores:", min_len)

    fig, ax = plt.subplots()
    plt.rcParams["font.family"] = "Times New Roman"
    # ax.set(xlabel="length", ylabel="frequency")
    ax.set_xlabel('length', fontname="Times New Roman")
    ax.set_ylabel('frequency', fontname="Times New Roman")
    for tick in ax.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax.get_yticklabels():
        tick.set_fontname("Times New Roman")
    ax.hist(all_cores_length, bins = list(range(1, 15)))
    plt.savefig("cyanobactin_stats.png", dpi=300)

def get_cores(headers, seqs):
    cores = []
    for i, header in enumerate(headers):
        if header[0] > 1:
            # print(header)
            for j in range(header[0]):
                begin = header[j*2+1]-1
                end = header[(j+1)*2]-1
                # print(begin, end, header, seqs[i], seqs[i][begin:end])
                cores.append(seqs[i][begin:end])
    return cores



def main():
    file = "./cyanobactin_full.fasta"
    headers, seqs = read_file(file)
    stats(headers)
    cores = get_cores(headers, seqs)

    predicted_core = []
    with open("./sample_output.fasta", 'r') as file:
        for line in file:
            if ">" not in line:
                predicted_core.append(line.strip())
    # print(predicted_core)
    # print(cores)

    for core in cores:
        if core not in predicted_core:
            print(core)
        else:
            print("Yes")

if __name__ == "__main__":
    main()
