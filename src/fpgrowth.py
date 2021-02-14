from collections import defaultdict, OrderedDict
from csv import reader
from itertools import chain, combinations
from optparse import OptionParser
from fpgrowth_py.utils import *
from csv_writer import *

def fpgrowth(itemSetList, minSupRatio, minConf):
    frequency = getFrequencyFromList(itemSetList)
    minSup = len(itemSetList) * minSupRatio
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
    if(fpTree == None):
        print('No frequent item set')
        quit()
    else:
        freqItems = []
        mineTree(headerTable, minSup, set(), freqItems)
        write_csvfile_freq2('data/FPGrowth_minSup_'+ str(minSupRatio) +'_freq.csv',freqItems)
        for i in range(6,10):
            minConf = float(i/10)
            rules = associationRule(freqItems, itemSetList, minConf)
            rules.sort(key=lambda x: x[2])
            fname='data/FPGrowth_minSup_'+ str(minSupRatio) +'_minConf_'+ str(minConf)+'rules_.csv'
            write_csvfile_rules(fname,rules)
        return freqItems, rules
