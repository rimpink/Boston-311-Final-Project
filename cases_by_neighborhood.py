# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 01:32:16 2023

@author: rosal
"""

import pandas as pd
import matplotlib.pyplot as plt

com_total=pd.read_csv("tmph4izx_fb.csv")

neighborhood = com_total.sort_values("neighborhood")
neighborhood = com_total.dropna()
print(neighborhood)
print("Total # of Cases:",len(neighborhood))
#sort cases, drop reports without neighborhood identfied, print total number of cases

num=com_total["neighborhood"]
neighborhood_counts=num.value_counts()
neighborhood_counts=neighborhood_counts.dropna()
print(neighborhood_counts)
neighborhood_counts.to_csv('neighborhood_counts.csv')
#count cases by neighborhood, write to csv

#%%
fig, ax1=plt.subplots(figsize=(8,5))
num.value_counts().plot.barh(ax=ax1)
fig.suptitle("Cases by Neighborhood")
ax1.set_xlabel("Neighborhood")
ax1.set_ylabel("# of Cases Reported")
fig.tight_layout()
fig.savefig("cases_by_neighborhood.png")
#create bar graph of cases by neighborhood

#%%
neighborhoods = ["Allston",
                "Allston / Brighton",
                "Back Bay",
                "Beacon Hill",
                "Boston",
                "Brighton",
                "Charlestown",
                "Chestnut Hill",
                "Dorchester",
                "Downtown / Financial District",
                "East Boston",
                "Fenway / Kenmore / Audobon Circle / Longwood",
                "Greater Mattapan",
                "Hyde Park",
                "Jamaica Plain",
                "Mattapan",
                "Mission Hill",
                "Roslindale",
                "Roxbury",
                "South Boston",
                "South Boston / South Boston Waterfront",
                "South End",
                "West Roxbury"]


for n in neighborhoods:
     selected=com_total.query(f"neighborhood=='{n}'")
     print(f"{n} Cases: {len(selected)}")
counts=com_total["neighborhood"].value_counts()
count_row=counts.sort_values()
percents=(count_row/276723)*100
sumup=sum(count_row/276723)
count_row=round((count_row/276723)*100)
print("% Total Cases by Neighborhood",count_row)
count_row.to_csv('neighborhood_percents.csv')
#calculate percentage of total cases by neighborhood

#%%
fig, ax1=plt.subplots(figsize=(15,15))
count_row.plot.pie(ax=ax1)
fig.suptitle("% Cases by Neighborhood")
ax1.set_xlabel("Neighborhood")
ax1.set_ylabel("# of Cases Reported")
fig.tight_layout()  
fig.savefig("percent_cases_by_neighborhood.png")
#create pie chart of case percentages by neighborhood