import pandas as pd
from faker import Factory

fake = Factory.create()

def generate_fake_first_name():
    return fake.first_name()
        
print(generate_fake_first_name())

def generate_fake_last_name():
    return fake.last_name()


def data_cleaner(df, cols):
    for cols_name in cols:
        
        keys = {}
        #keys= {cats:i for i, cats in enumerate(df[cols_name].unique())} # Turn values into numbers for each unique instance
        for cats in (df[cols_name].unique()):
            keys[cats] = generate_fake_first_name()
        df[cols_name] = df[cols_name].apply(lambda x: keys[x])
    return df

df = pd.read_csv('testdata.csv')
# print(df.head(2))

cols = ['firstName']
df = data_cleaner(df, cols)
df.to_json('anondata.json')

print()