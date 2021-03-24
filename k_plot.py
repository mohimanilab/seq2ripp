################################################################################
# Filename: plot.py
# Author: Yi-Yuan Lee
# Date: 10.31.2020
# Description: plot the top_k vs accuracy on MIBiG data
################################################################################
import matplotlib.pyplot as plt
import os



def read_correct(filename):
    bgc = {}
    ctr = 0
    with open(filename, 'r') as file:
        for line in file:
            temp = line.strip().split(",")
            if temp[3]:
                ctr += 1
                if bgc.get(temp[0]):
                    bgc[temp[0]].append(temp[3])
                else:
                    bgc[temp[0]] = [temp[3]]
    return bgc, ctr


def read_avg_preds(input):
    avg_preds = []
    for i in range(1, len(input)+1):
        zero_pred = 0
        temp = []
        with open("./top_"+str(i)+"/avg_preds_"+str(i)+".txt", 'r') as file:
            for line in file:
                num = float(line.strip())
                if num != 0.0:
                    temp.append(num)
                else:
                    zero_pred += 1
        avg_preds.append(sum(temp)/len(temp))
        print("Zero pred #:", zero_pred)
    return avg_preds


def read_fasta(filename):
    cores = []
    with open(filename, 'r') as file:
        for line in file:
            if ">" not in line:
                cores.append(line.strip())
    return cores

def read_predicted_cores():
    # {"top_k" : {"BGC": [core1, core2, ...]}}
    result = {}
    for folder in os.listdir():
        if "top" in folder:
            BGC_result = {}
            for BGC in os.listdir("./" + folder):
                if "BGC" in BGC:
                    BGC_result[BGC] = read_fasta(folder+"/"+BGC+"/"+BGC+".core")
            result[folder] = BGC_result
    return result


def cal_accu_out(bgc, num_cores, predicted_cores):
    # this record for each k
    accuracy = {}
    num_outputs = {}
    # for each top_k, and its BGC predictions
    for k, BGC in predicted_cores.items():
        accu_ctr = 0
        output_ctr = 0
        # for each bgc and all cores predicted
        for bgc_id, cores in BGC.items():
            if bgc.get(bgc_id):
                output_ctr += len(cores)
                for cor_bgc in bgc[bgc_id]:
                    if cor_bgc in cores:
                        accu_ctr += 1
        accuracy[k] = accu_ctr/num_cores
        num_outputs[k] = output_ctr
    return accuracy, num_outputs



def plot(t_l, v_l, t_a, v_a, e, ids):
    x = [x*e for x in range(1, len(t_l)+1)]


    fig, ax1 = plt.subplots()
    train_loss, = ax1.plot(x, t_l, label = 'train_loss', color='red')
    valid_loss, = ax1.plot(x, v_l, label = 'valid_loss', color='blue')

    ax1.set(xlabel='epoch', ylabel='loss', title="Loss/Accuracy")
    ax1.set_ylim(bottom=0.0,top=1.0)
    legend1 = ax1.legend(bbox_to_anchor=(1.5, 1), loc="upper right")

    ax2 = ax1.twinx()
    train_accu, = ax2.plot(x, t_a, label = 'train_accuracy', color='green')
    valid_accu, = ax2.plot(x, v_a, label = 'valid_accuracy', color='orange')
    ax2.set(ylabel='accuracy')
    ax2.set_ylim(bottom=0.0,top=1.0)
    legend2 = ax2.legend(bbox_to_anchor=(1.5, 0.8), loc="upper right")

    filename = "models/model_" + ids + ".png"
    plt.savefig(filename, bbox_extra_artists=(legend1,\
            legend2), bbox_inches='tight')
    plt.close()

def plot_avg_pred(avg_preds):
    num = len(avg_preds)
    x = [x for x in range(1, num+1)]
    y = [x*x for x in range(1, num+1)]
    fig, ax1 = plt.subplots()
    preds_num = ax1.plot(x, avg_preds, label="MIBiG dataset", color='blue')
    theor_num = ax1.plot(x, y, label="Theoretical number", color='red')
    ax1.set(xlabel='top_k pair(s) of cleavage site', ylabel='number of predicted cores per orf')
    # ax1.set_ylim(bottom=0.0, top=1.0)
    legend = ax1.legend(bbox_to_anchor=(1.5, 1), loc='upper right')
    filename = "average_preds.png"
    plt.savefig(filename, bbox_extra_artists=([legend]), bbox_inches='tight')
    plt.close


def plot_accu_num(accu, num_output):
    num = len(accu)
    x = [x for x in range(1, num+1)]
    fig, ax1 = plt.subplots()
    plt.rcParams["font.family"] = "Times New Roman"
    theor_num = ax1.plot(x, num_output, label="Number of predicted cores", color='red')
    # ax1.set(xlabel='top_k pair(s) of cleavage site', ylabel='number of predicted cores per BGC')
    ax1.set_xlabel('k', fontname="Times New Roman")
    ax1.set_ylabel('Number', fontname="Times New Roman")
    legend = ax1.legend(bbox_to_anchor=(1.5, 1), loc='upper right')
    for tick in ax1.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax1.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax2 = ax1.twinx()
    preds_num = ax2.plot(x, accu, label="Accuracy", color='blue')
    ax2.set(ylabel = "Accuracy")
    ax2.set_ylim(bottom=0.0,top=1.0)
    legend2 = ax2.legend(bbox_to_anchor=(1.5, 0.9), loc="upper right")
    for tick in ax2.get_yticklabels():
        tick.set_fontname("Times New Roman")
    filename = "accu_numoutputs.png"
    plt.savefig(filename, dpi=300, bbox_extra_artists=(legend,\
            legend2), bbox_inches='tight')
    plt.close



def main():
    # read BGC id and correct cores
    bgc, num_cores = read_correct("./mibig_bgc_orf_core.csv")


    # read predicted cores
    predicted_cores = read_predicted_cores()

    # read predicted cores's outputs
    avg_preds = read_avg_preds(predicted_cores)

    # plot avg_pred vs top_k
    plot_avg_pred(avg_preds)

    # calcualte accuracy and number of outputs
    accuracy, num_outputs = cal_accu_out(bgc, num_cores, predicted_cores)
    accu_list = []
    num_out_list = []
    for i in range(1, len(accuracy)+1):
        accu_list.append(accuracy["top_"+str(i)])
        num_out_list.append(num_outputs["top_"+str(i)])

    # plot accurate perc + number of outputs vs top_k
    plot_accu_num(accu_list, num_out_list)


if __name__ == "__main__":
    main()
