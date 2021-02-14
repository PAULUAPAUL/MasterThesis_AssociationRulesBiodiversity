from csv import reader
from collections import defaultdict, Counter
from itertools import chain, combinations, product

def getAboveMinSup(itemSet, itemSetList, minSup, globalItemSetWithSup, k):
    freqItemSet = set()
    itemSetList2 = set()
    localItemSetWithSup = Counter()

    [(globalItemSetWithSup.update(frozenset([item])), localItemSetWithSup.update(frozenset([item]))) for item in itemSet for itemSet in itemSetList if item.issubset(itemSet)]
    # print(itemSetList2)
    for item in localItemSetWithSup:
        support = float(localItemSetWithSup[item] / len(itemSetList))
        if (support>=minSup):
            freqItemSet.add(item)
            itemSetList2.add(item)
    # print(itemSetList)

    l = []
    for trans in itemSetList:
        # print(list(trans))
        inner = []
        for el in itemSetList2:
            inside = True
            for pat in el:
                inside = inside and (pat in list(trans))
                # print('pat ',pat, ' inside ', el, ' : ', inside )
            if inside:
                inner.extend([el])
        # print(inner)
        if inner: l.append(inner)
    itemSetList = l

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
