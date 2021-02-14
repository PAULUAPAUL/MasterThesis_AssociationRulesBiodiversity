import csv

# csv export freqItemSet
def write_csvfile_freq(fname,freqItemSet):
    with open(fname, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['frequent itemsets:'])
        writer.writerow('')
        for key, value in freqItemSet.items():
            writer.writerow([str(x) for x in value])
    csv_file.close()

# csv export for rules
def write_csvfile_rules(fname,rules):
    with open(fname, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Regeln:'])
        writer.writerow(['LHS','RHS','Conf'])
        for el in rules:
            writer.writerow(el)
    csv_file.close()

# csv export for FP-Growth
def write_csvfile_freq2(fname,freqItemSet):
    print(fname)
    with open(fname, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['frequent itemsets:'])
        writer.writerow('')
        freqItemSet.sort(key=len)
        for value in freqItemSet:
            writer.writerow([str(x) for x in value])
    csv_file.close()
