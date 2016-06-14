#import data and make into a dataframe
faculty = pd.read_csv('/Users/Jessica/ds/metis/prework/dsp/python/faculty.csv', na_values = [""," ", 0], skipinitialspace = True)
faculty = pd.DataFrame(faculty)

#make into list
emaillist = faculty['email'].tolist()
print(emaillist)

#Q5 :  write list of emails to a csv
import pandas as pd
emaildataframe = pd.DataFrame(emaillist, columns = ['emails'])
emaildataframe.to_csv('/Users/Jessica/ds/metis/prework/dsp/python/emails.csv', sep = ',')
