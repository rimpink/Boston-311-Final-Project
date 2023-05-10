# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:57:10 2023

@author: rosal
"""
 
Analyzing Boston’s Constituent Service Center

    This analysis explores usage of the Boston 311 Constituent Service program, a non-emergency service request platform easily available by phone, web, or app. Scripts explore the types of problems (from a range of 40 options) being reported in each of Boston's 23 neighborhoods, and highlight prevalence of usage across different neighborhoods.
       
Data

To access input data:
    1. Visit https://data.boston.gov/dataset/311-service-requests
    2. Download the CSV file for "311 Service Requests - 2022"
    3. Refer the "CRM Value Codex" on the website for more information on the values represented in each column of the CSV file
    
Scripts

Scripts may be run in any order. 

     cases_by_neighborhood.py
         This script counts number of cases reported in each neighborhood during the year and calculates the percentage of total cases reported in each neighborhood
         Deliverables: 
             neighborhood_counts.csv - number of cases reported in each neighborhood
             neighborhood_percents.csv - percentage of cases reported by neighborhood
             cases_by_neighborhood.png - bar graph of number of cases reported in each neighborhood
             percent_cases_by_neighborhood.png - pie chart of percentage of cases by neighborhood
        
     report_counts.py
         This script counts total number of cases reported to the system during the year and counts the number of cases for each reporting category
         Deliverables:
            case_counts.csv - number of cases by reason
            big_case_numbers.png - bar graph of top 20 most reported case categories (out of 40)
            small_case_numbers.png - bar graph of 20 least reported case categories (out of 40)

     top_neighborhood_cases
         This script records the top five most reported case categories in each neighborhood
         Deliverables:
            top_five.csv - top five most reported case categories in each neighborhood
            top_five_heatmap.png - heatmap of top five most reported case categories in each neighborhood
 
Results & Analysis
    
    In analyzing usage by neighborhood, Dorchester has a clear lead in number of cases reported. This is logical considering that Dorchester is Boston's largest neighborhood by population and land area. However, Dorchester is also a primarily residential neighborhood, made of up of multigenerational families, as are the following highest reporting neighborhoods - Roxbury and South Boston. This may suggest that there are strong feelings of pride for the neighborhood - residents care and actively report issues to improve the area. One of Boston's other largest neighborhoods, Allston/Brighton, has less usage than other large residential areas; however, this area is primarily made up of transient populations - students - suggesting that community ties are lacking and reporting is reduced as a result. The city may wish to run a coordinated campaign to inform different populations of residents - students, families, working professionals, etc. - on the ease and importance of reporting case issues. Otherwise, the system may fall prey to reporting bias and misrepresent the actual existence of problems across the city.

    In looking at the number of cases reported in each category, we see a clear lead in enforcement and abandoned vehicle cases, followed by street cleaning and code enforcement issues, then sanitation and highway maintenance. While some things are out of the government's control, such as the number of abandoned vehicles or code enforcement issues, this information could be very useful to city leaders in the deployment of city resources - for example, the city may seek to do more preventative highway treatment to avoid maintenance issues in the future, or rearrange street cleaning schedules based on geographic reporting data after observing trends. 

    With the further breakdown of top reported cases by neighborhood, the city can further target resource deployment and conduct analysis on differences among neighborhoods. Some categories are common across the city, such as vehicle abandonment and sanitation, suggesting a citywide approach is necessary, but other unique case rates could point to individualized problems that could be addressed by the city. For example, the South End and South Boston both had needle pickup cases in their top five most reported categories. This could suggest a prevalence of opioid abuse in these areas and push city leaders to take action such as implementing more addiction treatment programs in these neighborhoods or providing needle disposal sites to keep dangerous needles off the streets. Similarly, in West Roxbury, residents report tree issues as one of their top five most reported categories. Leaders may want to deploy the city arborist to conduct a study of the neighborhood and see if the city can take action to ameliorate tree issues and prevent future problems that could become liabilities for the city. 

    By using these data to better understand where problems are prevalent or services are failing, city leaders are able to efficiently and effectively address these issues. Targeted deployment of resources is good for taxpayers, and will generate satisfaction among constituents, politically benefitting the current mayor's administration - all while making the city a better, safer place. 

    
                   