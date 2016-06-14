import pandas as pd
import numpy as np

#import data and make into a dataframe
faculty = pd.read_csv('/Users/Jessica/ds/metis/prework/dsp/python/faculty.csv', na_values = [""," ", 0], skipinitialspace = True)
faculty = pd.DataFrame(faculty)

emaillist = faculty['email'].tolist()
print(emaillist)

#Q6
#make column of last names in dataframe
faculty_dic_frame['lastname'] = faculty.name.str.split('\s+').str[-1]
faculty_dic_frame = faculty_dic_frame.drop('name', 1)
lastnames = faculty_dic_frame['lastname']
lastnames

#make dictionary
q6 = {}
for name in lastnames:
    x = faculty_dic_frame[lastnames == name]
    for index, row in x.iterrows():
        q6.setdefault(row['lastname'], []).append(row[['degree', 'title', 'email']].tolist())
#return first 3 pairs            
first3 = {k: q6[k] for k in sorted(q6.keys())[:3]}
first3

#q7
#make dictionary
q7 = {}
for index, row in faculty.iterrows():
    q7.setdefault((row['name'].split()[0], row['name'].split()[-1]), []).append(row[['degree', 'title', 'email']].tolist())

first3 = {k: q7[k] for k in sorted(q7.keys())[:3]}
first3

#q8
#make dictionary
q8 = {}
for index, row in faculty.iterrows():
    q8.setdefault((row['name'].split()[-1], row['name'].split()[0]), []).append(row[['degree', 'title', 'email']].tolist())

first3 = {k: q8[k] for k in sorted(q8.keys())[:3]}
first3