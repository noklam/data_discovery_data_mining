# %%
import pandas as pd
DATA = 'data/train.json'

df = pd.read_json(DATA)
print(df.head().T)

