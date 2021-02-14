import pandas as pd
import numpy as np
from preprocess import *
import time
import sys

def ProcessData (minSup = 0.3,minConf = 0.5,minInt = 0.1,write_csv= True):

    print('Minimum Support: ', minSup)
    print('Minimum Confidence: ', minConf)
    print('Minimum Interest: ', minInt)

    print("FP-Growth")
    start = time.time()
    freqItemSet,rules = fpgrowth(data_grouped['SPECIES_ID2'].tolist(), minSupRatio=minSup, minConf=minConf)
    end = time.time()
    print('FP-growth needed: ',end - start, ' sec')

    if write_csv:
        write_csvfile_freq2('data/FPGrowth_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_freq.csv',freqItemSet)
        write_csvfile_rules('data/FPGrowth_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_rules.csv',rules)

    print("apriori")
    start = time.time()
    freqItemSet,rules = apriori(data_grouped['SPECIES_ID2'].tolist(), minSup=minSup, minConf=minConf)
    end = time.time()
    print('apriori needed: ',end - start, ' sec')
    if write_csv:
        write_csvfile_freq('data/Apriori_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_freq.csv',freqItemSet)
        write_csvfile_rules('data/Apriori_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_rules.csv',rules)


    print("apriori interest")
    start = time.time()
    freqItemSet,rules = apriori_interest(data_grouped['SPECIES_ID2'].tolist(), minSup=minSup, minConf=minConf, minInt=minInt)
    end = time.time()
    print('apriori int needed: ',end - start, ' sec')
    if write_csv:
        write_csvfile_freq('data/AprioriInt_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_freq.csv',freqItemSet)
        write_csvfile_rules('data/AprioriInt_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_rules.csv',rules)


    print("apriori tid")
    start = time.time()
    freqItemSet,rules = apriori_tid(data_grouped['SPECIES_ID2'].tolist(), minSup=minSup, minConf=minConf)
    end = time.time()
    print('apriori tid needed: ',end - start, ' sec')
    if write_csv:
        write_csvfile_freq('data/AprioriTid_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_freq.csv',freqItemSet)
        write_csvfile_rules('data/AprioriTid_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_rules.csv',rules)


# main
PreprocessData('GBIF',r'C:\Users\Paul\Documents\Studium_PP\Master\Masterarbeit\Gitlab\master-thesis-data-mining\Datasets\GBIF\full records\0079101-200613084148143\occurrence.txt',True)

for i in range (1,1,-1):
    ProcessData(minSup=float(i/10),minConf=0.5,minInt=0.1,True)
