import pandas as pd
import numpy as np

#import data and make into a dataframe
faculty = pd.read_csv('/Users/Jessica/ds/metis/prework/dsp/python/faculty.csv', na_values = [""," ", 0], skipinitialspace = True)
faculty = pd.DataFrame(faculty)
faculty_dic_frame = pd.DataFrame(faculty)

#make series to lists
degrees = pd.np.array(faculty['degree'])

#make new dataframe with all degrees and tally
degreetypes = faculty['degree'].str.replace('.','').str.split(' ', expand = True)
degreelist = degreetypes.apply(pd.value_counts)
degreelist['sum'] = degreelist.sum(axis=1)
print(degreelist['sum'])
#???seems like a long way to do this, end up making two dataframes and creating a new column


#make new dataframe with all titles and tally
title = pd.np.array(faculty['title'])
titles = faculty['title'].str.replace(' of Biostatistics', '').str.replace(' is Biostatistics', '')
titlelist = titles.apply(pd.value_counts)
titletotals = titlelist.sum(axis = 0)
titletotals 

#make a list of the emails
emaillist = faculty['email'].tolist()
print(emaillist)

#find unique email domains and tally
domainlist = []
def emails(emaillist):
    for email in emaillist:
        a = email.index('@')
        emails = email[a:]
        domainlist.append(emails)
    return domainlist

emails(emaillist)
        
from collections import Counter
counts = Counter(domainlist)
print(counts)