# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:56:16 2023

@author: rosal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

com_total = pd.read_csv("tmph4izx_fb.csv")

com_total = com_total.sort_values('reason')
print(com_total)
#print and sort cases

neighborhood = com_total.groupby(["neighborhood","reason"]).size()
neighborhood=neighborhood.reset_index().query("neighborhood != ' '")
neighborhood=neighborhood.sort_values(["neighborhood",0],ascending=False)
top_five=neighborhood.groupby("neighborhood")
top_data=[]

for town,data in top_five:
    print("\n",town)
    print(data[0:5])
    top_data.append(data[0:5])
    
top_data=pd.concat(top_data)
top_data.to_csv("top_five.csv")
#select top five case reasons for each neighborhood, write to csv

grid=top_data.pivot(index="neighborhood",columns="reason",values=0)
fig,ax=plt.subplots(figsize=(6,12))
sns.heatmap(grid,ax=ax)
fig.savefig("top_five_heatmap.png")
#create heatmap of top five case reasons for each neighborhood

