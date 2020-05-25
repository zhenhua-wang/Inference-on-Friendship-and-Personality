import pandas as pd
import numpy as np

# load personality survery and friendship rating data
survey = pd.read_csv('./Data/SurveyBig5.csv', index_col=0)
fs = pd.read_csv('./Data/SurveyFriendship.csv', index_col='date')

# rules for calculating Big Five personality from the survey data
big5 = {
    'E': [[1,11,16,26,36],[6,21,31]],
    'A': [[7,17,22,32,42],[2,12,27,37]],
    'C': [[3,13,28,33,38],[8,18,23,43]],
    'N': [[4,14,19,29,39],[9,24,34]],
    'O': [[5,10,15,20,25,30,40,44],[35,41]]
}

# calculate Big Five personality trait
personality = {}
for k, v in big5.items():
    p_val = pd.Series(0,index=survey.index)
    for i in v[0]:
        p_val += survey.iloc[:,i-1]
    for j in v[1]:
        p_val += 6-survey.iloc[:,j-1]
    personality[k] = p_val

# this is table i)
persona = pd.DataFrame.from_dict(personality)

# this is table ii)
fs = fs['2011-04-30':'2011-05-01']

fs.source = fs.source.str.upper()
fs.target = fs.target.str.upper()
f_p = survey.index.values
fs_clean = fs[fs['source'].isin(f_p) & fs['target'].isin(f_p)]
del fs_clean['Unnamed: 0']
fs_clean = fs_clean[fs_clean['source'] != fs_clean['target']]

# this is table iii)
dm = pd.merge(fs_clean, persona, how='left', left_on='source', right_index=True)
dm2 = pd.merge(dm, persona, how='left', left_on='target', right_index=True, suffixes=('_s','_t'))

# output data
fs_clean.to_csv('./Processed/fs.csv')
persona.to_csv('./Processed/personality.csv')
dm2.to_csv('./Processed/dm.csv')



