# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:23:20 2022

@author: xyyan
"""
import csv

def read_file(filename, has_header = True):
    transactions = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        if has_header:
            next(reader, None)
        for row in reader:
            transactions.append((row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()))
    return transactions

def get_text_between_two_delimiters(text, delimiter_1, delimiter_2):
    index_start = text.index(delimiter_1)
    index_end = text.index(delimiter_2)
    return text[index_start + 1:index_end]