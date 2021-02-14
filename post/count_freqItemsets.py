import csv
from collections import Counter
from collections import defaultdict
import os

words_freq=[]

path="/home/paul/Documents/master-thesis-data-mining/student_work/Code/data/FP-Growth_0.1"

for file in os.listdir(path):
    if file.endswith("_freq.csv"):
        with open(os.path.join(path, file), 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            next(reader)
            for row in reader:
                # freq = '; '.join(row).replace('frozenset(','').replace(')','')
                # csv_words = freq.split("; ")
                freq = row
                csv_words = '{' + ', '.join(freq) + '}'
                # for i in csv_words:
                #      words_freq.append(i)
                words_freq.append(csv_words)

words_freq_counted = []

for i in words_freq:
    x = words_freq.count(i)
    words_freq_counted.append((i,x))

# def take_second(elem):
    # return elem[1]
items_freq_counted = sorted(set(words_freq_counted),reverse=True,key=lambda elem: elem[1])




# print(items_counted)
# #write this to csv file
with open('FP-Growth_Countfreqitemsets_0.1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['freqitems'])
    writer.writerows(items_freq_counted)
