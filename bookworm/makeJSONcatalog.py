import pandas as pd
import json
import pandas
import numpy as np

df = pd.read_csv("../poemeta.csv")

# Basically all code taken from https://gist.github.com/mikedewar/1486027

d = [ 
    dict([
        (colname, row[i]) 
        for i,colname in enumerate(df.columns)
    ])
    for row in df.values
]

for row in d:
    row['filename'] = row['docid']
    row['searchstring'] = "'%(title)s,' by %(author)s (%(imprint)s)" % row
    print json.dumps(row)


