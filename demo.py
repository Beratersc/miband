"""
- number of runs
- total distance of walks
- total distance of runs
- total distance of walks + runs

- show best runs (sort + head)
- show best time for 1km, 2km 
- line plot (smoothed) of 1km run time
"""

import pandas as pd

df = pd.read_csv("./data/jan2022_to_june2022.csv")
# walk is type 6, run is type 1
runs = df[(df['type'] == 1) & (df['distance(m)'] >= 1000)].copy()
num_of_runs = runs.shape[0] # 63
print(num_of_runs)

# runs['mins_per_km'] = runs['sportTime(s)'] / runs['distance(m)'] * 60
runs['seconds_per_km'] = (1000 / runs['distance(m)']) * runs['sportTime(s)'] 
m, s = divmod(runs['seconds_per_km'], 60)

def create_m_s(seconds):
    m, s = divmod(seconds, 60)
    return "{:02.0f}:{:02.2f}".format(m, s)

runs['speed_per_km'] = runs['seconds_per_km'].map(lambda x: create_m_s(x))
runs = runs.sort_values(by='seconds_per_km')
print(runs.head())

runs['distance_rounded'] = (runs['distance(m)'].round(decimals=-3)/1000).astype('category')
