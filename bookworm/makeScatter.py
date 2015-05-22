import json
import pandas as pd

weights = dict()

for line in pd.read_csv("../mainmodelpredictions.coefs.csv").iterrows():
    
