from csv import reader
from collections import defaultdict, Counter
from itertools import chain, combinations, product

def getAboveMinSup(itemSet, itemSetList, minSup, minInt, globalItemSetWithSup, k):
    freqItemSet = set()
    localItemSetWithSup = Counter()
    [(globalItemSetWithSup.update(frozenset([item])), localItemSetWithSup.update(frozenset([item]))) for item in itemSet for itemSet in itemSetList if item.issubset(itemSet)]

    for item in localItemSetWithSup:
        support = float(localItemSetWithSup[item] / len(itemSetList))
        if k > 1:
            item_last = list(item)[k-1:k]
            item_first = list(item)[:k-1]
            # print('item ', item)
            # print('last ',item_last)
            # print('first ',item_first)
            interest = abs(support-(globalItemSetWithSup[frozenset(item_last)]/len(itemSetList) * globalItemSetWithSup[frozenset(item_first)]/len(itemSetList)))
            # print ('item ',item,' interest ',interest, ' support ', support)
            if(support >= minSup and interest >= minInt):
                freqItemSet.add(item)
                #print ('added: item ',item,'interest ',interest)
        else:
            # print ('item ',item, ' support ', support)
            if (support>=minSup):
                freqItemSet.add(item)
    return set(freqItemSet)

def getUnion(itemSet, length):
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def pruning(candidateSet, prevFreqSet, length):
    tempCandidateSet = candidateSet.copy()

    for item in candidateSet:
        subsets = combinations(item, length)
        for subset in subsets:
            # if the subset is not in previous K-frequent get, then remove the set
            if(frozenset(subset) not in prevFreqSet):
                tempCandidateSet.remove(item)
                # print('pruned ', frozenset(subset), ' not in ',prevFreqSet)
                break
    return tempCandidateSet

def associationRule(freqItemSet, itemSetWithSup, minConf):
    rules = []
    for k, itemSet in freqItemSet.items():
        for item in itemSet:
            subsets = powerset(item)
            for s in subsets:
                confidence = float(
                    itemSetWithSup[item] / itemSetWithSup[frozenset(s)])
                if(confidence > minConf):
                    rules.append([set(s), set(item.difference(s)), confidence])
    return rules

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

def getItemSetFromList(itemSetList):
    tempItemSet = set()

    for itemSet in itemSetList:
        for item in itemSet:
            tempItemSet.add(frozenset([item]))

    return tempItemSet
