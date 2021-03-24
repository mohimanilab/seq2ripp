################################################################################
# Filename: plot.py
# Author: Yi-Yuan Lee
# Date: 11.13.2020
# Update: 01.27.2021
# Description: This file outputs all plots for the manuscript, too keep 
# everything in the same style. It will have different function to process
# different figure.
################################################################################
import sys
import numpy as np
import matplotlib.pyplot as plt

def read_csv(infile):
    out = []
    with open(infile, 'r') as f:
        for line in f:
            temp = line.strip().split(",")
            temp = [float(x) for x in temp]
            out.append(temp)
    print(len(out))
    return np.asarray(out)

def plot_orf2core(d):
    x = [x*50 for x in range(1, len(d)+1)]
    fig, ax1 = plt.subplots()
    plt.rcParams["font.family"] = "Times New Roman"
    
    train_loss, = ax1.plot(x, d[:,0], label = 'train_loss', color='red')
    valid_loss, = ax1.plot(x, d[:,7], label = 'validation_loss', color='blue')

    ax1.set(xlabel='epoch', ylabel='loss', title="orf2core")
    ax1.set_xlabel('epoch', fontname="Times New Roman")
    ax1.set_ylabel('loss', fontname="Times New Roman")
    # ax1.set_title("orf2core", fontname="Times New Roman")
    ax1.set_title("DeepRiPP", fontname="Times New Roman")
    for tick in ax1.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax1.get_yticklabels():
        tick.set_fontname("Times New Roman")
    legend1 = ax1.legend(bbox_to_anchor=(1.5, 1), loc="upper right")

    ax2 = ax1.twinx()
    train_accu, = ax2.plot(x, d[:,1], label = 'train_accuracy', color='green')
    valid_accu, = ax2.plot(x, d[:,8], label = 'validation_accuracy', color='orange')
    ax2.set(ylabel='accuracy')
    ax2.set_ylim(bottom=0.0,top=1.0)
    legend2 = ax2.legend(bbox_to_anchor=(1.5, 0.8), loc="upper right")

    # filename = "orf2core.png"
    # filename = "DeepRiPP.png"
    filename = "bgc2orf.png"
    plt.savefig(filename, dpi=300, bbox_extra_artists=(legend1,\
        legend2), bbox_inches='tight')




def main():
    infile = "../orf2core/orf2core/data/archive/1019/1019_1_stats.csv"
    infile = "../orf2core/orf2core/data/archive/1019/1019_deepripp_stats.csv"

    data = read_csv(infile)
    plot_orf2core(data)


if __name__ == "__main__":
    main()



    # def plot(self, d, e, end):
        # x = [x*e for x in range(1, len(d[0])+1)]

        # fig, ax1 = plt.subplots()
        # train_loss, = ax1.plot(x, d[0], label = 'train_loss', color='red')
        # valid_loss, = ax1.plot(x, d[1], label = 'valid_loss', color='blue')

        # ax1.set(xlabel='epoch', ylabel='loss', title=self.ids)
        # legend1 = ax1.legend(bbox_to_anchor=(1.5, 1), loc="upper right")

        # ax2 = ax1.twinx()
        # train_accu, = ax2.plot(x, d[2], label = 'train_accuracy', color='green')
        # valid_accu, = ax2.plot(x, d[3], label = 'valid_accuracy', color='orange')
        # ax2.set(ylabel='accuracy')
        # ax2.set_ylim(bottom=0.0,top=1.0)
        # legend2 = ax2.legend(bbox_to_anchor=(1.5, 0.8), loc="upper right")

        # filename = self.ids + end
        # plt.savefig(self.save_path / filename, bbox_extra_artists=(legend1,\
            # legend2), bbox_inches='tight')
