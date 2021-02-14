import csv
from collections import Counter
from collections import defaultdict
import os

words_rule=[]
path="/home/paul/Documents/master-thesis-data-mining/student_work/Code/data/Apriori-Int"

for file in os.listdir(path):
    if file.endswith("_rules.csv"):
        with open(os.path.join(path, file), 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            next(reader)
            for row in reader:
                rule = row[0]+'->'+row[1]
                words_rule.append(rule)

words_rules_counted = []

for i in words_rule:
    x = words_rule.count(i)
    words_rules_counted.append((i,x))

# def take_second(elem):
    # return elem[1]
items_rules_counted = sorted(set(words_rules_counted),reverse=True,key=lambda elem: elem[1])




# print(items_counted)
# #write this to csv file
with open('Apriori-Int_CountRules.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['rule'])
    writer.writerows(items_rules_counted)
