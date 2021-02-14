import pandas as pd
import numpy as np
from apriori_TID import *
from apriori_interest import *
from apriori import *
#from fpgrowth import *
from fpgrowth import *
import time
import matplotlib.pyplot as plt
import sys


def PreprocessData (dataset,filepath,write_csv =  True):
    if dataset == 'GBIF':
        # read input data as .txt
        data = pd.read_csv(filepath, sep='\t')
        # concat columns to new columns SPECIES_ID2
        data["SPECIES_ID2"] =  data['taxonRank'] + data['kingdom']+ data['class']+ data['order']+ data['family']+ data['genus']+ data['acceptedScientificName']
        # GPS information for generating transactions -> default decimals 3
        data['decimalLatitude'] = data['decimalLatitude'].round(decimals=3)
        data['decimalLongitude'] = data['decimalLongitude'].round(decimals=3)
        # reduce dataset to three columns
        data_red = data [['decimalLatitude', 'decimalLongitude','SPECIES_ID2']]
        # drop missing values
        data_red = data_red.dropna()
        # get transactions ny grouping based on GPS-information
        data_grouped = data_red.groupby(['decimalLatitude', 'decimalLongitude']).agg({'SPECIES_ID2':lambda x: list(set(x))})
        # remove transactions that have noch Specie
        data_grouped = data_grouped[data_grouped['SPECIES_ID2'].str.len()>1]
        if write_csv:
            data_grouped.to_csv('data\GBIF_TransData.csv')
    else:
        # read input data as csv
        data = pd.read_csv(filepath,low_memory=False)
        # concat columns to new columns SPECIES_ID2
        data["SPECIES_ID2"] =  data['DWC_TAXA'] + data['KINGDOM']+ data['CLASS']+ data['ORDER']+ data['FAMILY']+ data['GENUS']+ data['LAT_SCI_NAME']
        # reduce dataset to two columns
        data_red = data [['PLOTID','SPECIES_ID2']]
        # get transaction by grouping based on PLOTID
        data_grouped = data_red.groupby(['PLOTID']).agg({'SPECIES_ID2':lambda x: list(set(x))})
        if write_csv:
            data_grouped.to_csv('data\BE_TransData.csv')

    return data_grouped
