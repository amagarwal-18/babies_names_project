# %load q01_create_dict/build.py
import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])
    
def q01_create_dict(data):
    'write your solution here'
    names_dict = {'Name':data['Name'],
                 'Count':data['Count']}
    return names_dict


print(q01_create_dict(data))


