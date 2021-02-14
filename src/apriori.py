from csv import reader
from collections import defaultdict,Counter
from itertools import chain, combinations
from optparse import OptionParser
from utils import *
from csv_writer import *

def apriori(itemSetList, minSup, minConf):
    C1ItemSet = getItemSetFromList(itemSetList)
    # Final result global frequent itemset
    globalFreqItemSet = dict()
    # Storing global itemset with support count
    globalItemSetWithSup = Counter()

    L1ItemSet = getAboveMinSup(
        C1ItemSet, itemSetList, minSup, globalItemSetWithSup)
    currentLSet = L1ItemSet
    k = 2

    # Calculating frequent item set
    while(currentLSet):
        # Storing frequent itemset
        globalFreqItemSet[k-1] = currentLSet
        # Self-joining Lk
        candidateSet = getUnion(currentLSet, k)
        # Perform subset testing and remove pruned supersets
        candidateSet = pruning(candidateSet, currentLSet, k-1)
        # Scanning itemSet for counting support
        currentLSet = getAboveMinSup(
            candidateSet, itemSetList, minSup, globalItemSetWithSup)
        k += 1

    write_csvfile_freq('data/Apriori_minSup_'+ str(minSup)+ "_freq.csv",globalFreqItemSet)

    for i in range(6,10):
        minConf=float(i/10)
        rules = associationRule(globalFreqItemSet, globalItemSetWithSup, minConf)
        rules.sort(key=lambda x: x[2])
        fname='data/Apriori_minSup_'+ str(minSup) +'_minConf_'+ str(minConf)+'_rules.csv'
        write_csvfile_rules(fname,rules)

    return globalFreqItemSet, rules
#
# itemSetList = [['PR', 'P', 'CC'],['PR', 'DP'],['DP', 'CC'],['PR','P','CC']]
# freqItemSet, rules = apriori(itemSetList, minSup=0.5, minConf=0.5)
# count = 0
# # using isinstance
# for x in freqItemSet:
#       count += len(freqItemSet[x])
#
# print('freq ', count)
# print('rules ',len(rules))

# print(freqItemSet)
#print ("\n")
# print(rules)
