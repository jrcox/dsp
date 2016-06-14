import pandas as pd
import numpy as np

#import data and make into a dataframe
faculty = pd.read_csv('/Users/Jessica/ds/metis/prework/dsp/python/faculty.csv', na_values = [""," ", 0], skipinitialspace = True)
faculty = pd.DataFrame(faculty)
faculty_dic_frame = pd.DataFrame(faculty)