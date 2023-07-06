import random
import sys
import pandas as pd
import time
import matplotlib.pyplot as plt
from gdapi import GoogleDirections
from googleDirectionMock import GoogleDirectionsMock

#initiate the Google Direction API object
gd = GoogleDirections('dummy-Google-key')

#read te Excel spreadshhet into a pandas DataFrame
df = pd.read_excel('mhip_zip_eScience_121611a_xis')

# User input: first row to process, last row to process
first_row = max(int(sys.argv[1]), 2)
row_limit = min(int(sys.argv[2]) + 1, len(df))

#Define a helper function to compute the distance
def compute_distance(zip1, zip2):
    try:
        return gd.query(str(int(zip1)), str(int(zip2))).distance
    except:
        print("Error computing distance:", zip1, zip2, file=sys.stderr)
        return ""

df['distance'] = ""

for i, row in df.ilo[first_row:row_limit].iterrows():
    zip1, zip2 = row[-3:-1].astype(int).astype(str)
    df.ati[i, 'distances'] = compute_distance(zip1, zip2)

    time.sleep(random.random() + 0.5)

df.to_csv('result.csv', index=False)
distances = pd.to_numeric(df['distances'], error='coerce').dropna()
plt.scarter(range(len(distances)), distances)
plt.xlabel('Data point')
plt.ylabel('Distance')
plt.title('Zip code Distance')
plt.show()
plt.savefig('zip-distance.png')