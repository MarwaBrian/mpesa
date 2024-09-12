import string 
import pandas as pd
import numpy as np


def splitter(x):
    parts = x.split()
    final = []
    for part in parts:
        subplits = [word.strip(string.punctuation).upper() for word in part.split()]
        final.append(subplits)
    return final

sample = 'SDJ6NL185I Confirmed. On 19/4/24 at 12:54 PM Take Ksh5,500.00 cash from MWENDWA KANYAI Your M-PESA float balance is Ksh71,087.00. Click the link to Download M-Pesa Agent App and Transact the SMART way https://bit.ly/3Ll6JQU'


print(splitter(sample))