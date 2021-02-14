from csv import reader
from collections import defaultdict, Counter
from itertools import chain, combinations
from optparse import OptionParser
from utils_interest import *
import numpy as np
from csv_writer import *

def apriori_interest(itemSetList, minSup, minConf, minInt):
    C1ItemSet = getItemSetFromList(itemSetList)

    # Final result global frequent itemset
    globalFreqItemSet = dict()
    # Storing global itemset with support count
    globalItemSetWithSup = Counter()

    L1ItemSet = getAboveMinSup(
        C1ItemSet, itemSetList, minSup,minInt, globalItemSetWithSup,1)
    currentLSet = L1ItemSet
    k = 2

    # Calculating frequent item set
    while(currentLSet):
        # Storing frequent itemset
        globalFreqItemSet[k-1] = currentLSet
        # Self-joining Lk
        # print(currentLSet)
        candidateSet = getUnion(list(currentLSet), k)
        # print('Union fertig ', candidateSet)
        # Perform subset testing and remove pruned supersets
        candidateSet = pruning(candidateSet, currentLSet, k-1)
        # Scanning itemSet for counting support
        # print('candidate fertig ', candidateSet)
        #print(str(k))
        currentLSet = getAboveMinSup(
            candidateSet, itemSetList, minSup, minInt, globalItemSetWithSup,k)
        #print('Bedingung: ',currentLSet)
        k += 1

    write_csvfile_freq('data/Apriori_Int_minSup_'+ str(minSup)+ "_freq.csv",globalFreqItemSet)

    for i in range(6,10):
        minConf=float(i/10)
        rules = associationRule(globalFreqItemSet, globalItemSetWithSup, minConf)
        rules.sort(key=lambda x: x[2])
        fname='data/Apriori_INT_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_rules.csv'
        write_csvfile_rules(fname,rules)
    return globalFreqItemSet, rules

# itemSetList = [['PR', 'P', 'CC'],['PR', 'DP'],['DP', 'CC'],['PR','P','CC']]
# # # itemSetList = [['A', 'B', 'D'],['A', 'B','C','D'],['B', 'D'],['B','C','D','E'],['A','C','E'],['B','D','F'],['A','E','F'],['C','F'],['B','C','F'],['A','B','C','D','F']]
# #
# freqItemSet, rules = apriori(itemSetList, minSup=0.3, minConf=0.5,minInt=0.0)
# print(rules)
