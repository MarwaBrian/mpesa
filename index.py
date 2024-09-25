import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import xmltodict as xd
import string
import re
from datetime import datetime
# def splitter(x):
#     parts = x.split()
#     final = []
#     for part in parts:
#         subplits = [word.strip(string.punctuation).upper() for word in part.split()]
#         final.append(subplits)
#     return final

# sample = 'SDJ6NL185I Confirmed. On 19/4/24 at 12:54 PM Take Ksh5,500.00 cash from MWENDWA KANYAI Your M-PESA float balance is Ksh71,087.00. Click the link to Download M-Pesa Agent App and Transact the SMART way https://bit.ly/3Ll6JQU'
# sample_2 = 'SDJ3NAIRL9 confirmed.You bought Ksh50.00 of airtime on 19/4/24 at 11:25 AM.New M-PESA balance is Ksh738.04. Transaction cost, Ksh0.00. Amount you can transact within the day is 499,950.00. Reverse erroneously purchased airtime using M-PESA by sending the M-PESA SMS to 456'
# # print(splitter(sample))


# """ 
# function that takes a string as input, splits it
# replaces any punctuation marks with (), 
# only exception for the punctuation replacement is if it starts
# 'KSH' and also has numeric figures eg 'kshs10879.99'
# """

# def cleaner(x):
#     parts = x.split()
#     final = []
#     amount_pattern = r'Ksh[\d,]+\.\d{2}'
#     for part in parts:
#         if re.match(amount_pattern, part):
#             final.append(part)
#         else:
#             part = part.replace('.', ' ')
#             subsplits = part.split()
#             subsplits = [word.strip(string.punctuation).upper() for word in part.split()]
#             final.extend(subsplits)
#     return final


# print(cleaner(sample_2))



#testing out a new function for extracting the transaction type
df = pd.read_csv('mochada_sms.csv')


#columns to keep
keep = ['@address', '@body', '@readable_date']

#new data frame 
data = df[keep].copy()

#renaming the columns 
data.columns = ['address', 'body', 'date']

# Define the pattern
transaction_type_pattern = r'(Confirmed|Business\sDeposit\sConfirmed)'

# Compile the pattern once for efficiency
compiled_pattern = re.compile(transaction_type_pattern, re.IGNORECASE)

# Loop through the first 20 entries and print the extracted values
for index, row in data.head(20).iterrows():
    body_text = row['body']
    match = compiled_pattern.search(body_text)
    extracted = match.group(0) if match else None
    print(f"Index: {index}, Extracted Value: {extracted}")



