# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:58:05 2023

@author: rosal
"""

import pandas as pd
import matplotlib.pyplot as plt


com_total = pd.read_csv("tmph4izx_fb.csv")

com_total = com_total.sort_values('reason')
print(com_total)

neighborhood = com_total.sort_values("neighborhood")
neighborhood = com_total.dropna()
print(neighborhood)
print("Total # of Cases:",len(neighborhood))
#sort cases, drop reports without neighborhood identfied, print total number of cases

#%%
reasons = ["Street Lights",
           "Sanitation",
           "Signs & Signals",
           "Highway Maintenance", 
           "Notification", 
           "Street Cleaning", 
           "Code Enforcement", 
           "Recycling", 
           "Environmental Services", 
           "Graffiti", 
           "Building", 
           "Employee & General Comments", 
           "Enforcement & Abandoned Vehicles", 
           "Housing", 
           "Trees", 
           "Health", 
           "Weights and Measures", 
           "Park Maintenance & Safety", 
           "Abandoned Bicycle", 
           "Administrative & General Requests", 
           "Operations", 
           "Traffic Management & Engineering", 
           "Cemetery", 
           "Office of The Parking Clerk", 
           "Volunteer & Corporate Groups", 
           "Bridge Maintenance", 
           "Valet",
           "Alert Boston",
           "Parking Complaints",
           "Programs",
           "Current Events",
           "Catchbasin",
           "Water Issues",
           "Fire Hydrant",
           "School Transportation",
           "School Department",
           "Sidewalk Cover / Manhole",
           "Billing",
           "MBTA",
           "Pothole",
           "General Request",
           "Fire Department",
           "Survey",
           "Animal Issues",
           "Neighborhood Services Issues",
           "Generic Noise Disturbance",
           "Air Pollution Control",
           "Administration",
           "Administrative",
           "Disability",
           "Metrolist",
           "Call Inquiry",
           "Consumer Affairs Issues",
           "Call Center Intake",
           "Investigations and Enforcement",
           "Boston Bikes",
           "Participatory Budgeting Idea Collection"]

for r in reasons:
     selected=com_total.query(f"reason=='{r}'")
     print(f"{r} Cases: {len(selected)}")
counts=com_total["reason"].value_counts()
count_row=counts.sort_values()
print(count_row)
count_row.to_csv("case_counts.csv")
#print and sort reasons by number of cases, create csv

#%%

fig, ax1=plt.subplots(figsize=(8,5))
count_row[-20:].plot.barh(ax=ax1)
fig.suptitle("Most Reported Cases (Top 20)")
ax1.set_xlabel("Cases")
ax1.set_ylabel("# of Cases Reported")
fig.tight_layout()
fig.savefig("big_case_numbers.png")

fig, ax1=plt.subplots(figsize=(8,5))
count_row[:-20].plot.barh(ax=ax1)
fig.suptitle("Least Reported Cases (Bottom 20)")
ax1.set_xlabel("Cases")
ax1.set_ylabel("# of Cases Reported")
fig.tight_layout()
fig.savefig("small_case_numbers.png")
#create bar graphs for most and least reported cases