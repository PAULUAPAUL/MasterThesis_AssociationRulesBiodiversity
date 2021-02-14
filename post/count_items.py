import csv
from collections import Counter
from collections import defaultdict
import os

words_LHS=[]
words_RHS=[]
path=r"C:\Users\Paul\Documents\Studium_PP\Master\Masterarbeit\Gitlab\master-thesis-data-mining\student_work\Code\data\Apriori-Int_0.1"

for file in os.listdir(path):
    if file.endswith("_rules.csv"):
        with open(os.path.join(path, file), 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            next(reader)
            for row in reader:
                LHS = row[0].replace('{', '').replace('}', '')
                csv_words = LHS.split(", ")
                for i in csv_words:
                     words_LHS.append(i)
                RHS = row[1].replace('{', '').replace('}', '')
                csv_words = RHS.split(", ")
                for i in csv_words:
                     words_RHS.append(i)

words_LHS_counted = []
words_RHS_counted = []
print(len(words_LHS))
print(len(words_RHS))
quit()
for i in words_LHS:
    x = words_LHS.count(i)
    words_LHS_counted.append((i,x))

for i in words_RHS:
    x = words_RHS.count(i)
    words_RHS_counted.append((i,x))

# def take_second(elem):
    # return elem[1]
items_LHS_counted = sorted(set(words_LHS_counted),reverse=True,key=lambda elem: elem[1])
items_RHS_counted = sorted(set(words_RHS_counted),reverse=True,key=lambda elem: elem[1])



# print(items_counted)
# #write this to csv file
with open('FP-Growth_CountItems0.1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['LHS'])
    writer.writerows(items_LHS_counted)
    writer.writerow(['RHS'])
    writer.writerows(items_RHS_counted)
