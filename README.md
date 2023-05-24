<p align='center'>
<img src ="src/portada.png" height=200>
<p>

## **Context**

<p align="justify">
Air accidents are unexpected and unwanted events that result in physical damage to both the people and the aircraft involved. They can affect any type of aircraft, be it commercial, private, helicopters, gliders or hot air balloons.

These accidents can be caused by various factors, such as human error, equipment failure, adverse weather conditions, maintenance problems, air traffic management deficiencies, design or manufacturing defects. The consequences of accidents can be devastating both in terms of human and economic losses.

That's why the aviation industry, regulatory authorities and researchers are working tirelessly to improve safety and prevent future accidents.

To achieve this, it is essential to analyze historical data on air accidents. The systematic collection and analysis of this data helps researchers identify patterns, trends, and contributing factors that can lead to safety improvements. This data is valuable for improving the training of pilots and maintenance personnel, as well as for improving the design and manufacturing of aircraft and aviation equipment.

This porject is focused as a report to the **International Civil Aviation Organization (ICAO)**, an intergovernmental organization dedicated to promoting the safety and efficiency of international civil aviation.

The 193 countries collaborating with the ICAO are actively striving to achieve their shared global objective of zero fatalities by the year 2030. This ambitious goal is being pursued alongside efforts to enhance regulatory capabilities and implement various programs and objectives. These initiatives focus on the key areas in global aviation security planning, oversight, and risk mitigation.

</p>

<br/>

## **Objective**

The project aims to develop an interactive dashboard that enables users to explore the data and extract relevant information about aircraft accidents. Additionally, a comprehensive report will be generated to present the findings derived from the analyzed data.

To accomplish this objective, a database of aircraft accidents worldwide spanning from 1908 to 2021 was utilized. The data was thoroughly analyzed and visualized to identify patterns and trends pertaining to civil aviation safety.

In order to align the data analysis with the organization's goals and gain a comprehensive understanding of the dataset, the following key performance indicators (KPIs) are showcased on the dashboard:

+ Reduce the annual mortality rate by 5%, calculated as the number of fatalities in aviation accidents relative to the total number of individuals on board the flights involved.
+ Decrease the percentage of accidents attributed to technical issues by 5% within a 5-year timeframe.
+ Minimize the number of undetermined causes of aircraft accidents by 10% over a 5-year period.
+ Reduce accidents attributed to human error by 5% within a 5-year timeframe, specifically focusing on the countries of the United States and Canada.

By monitoring these KPIs through the interactive dashboard, the organization can gain valuable insights and track progress towards improving aviation safety.

<br/>

## **Scope**

**`Data cleaning and transformation`**🧼✨

Preformed in the `EDA` notebook, this process involved handling null values, adjusting data types, and creating new columns with more meaningful values for the analysis. To enhance the accuracy of the 'country' column, dictionaries, partly provided by ChatGPT, were utilized. The classification of the 'summary' column was achieved with the assistance of natural language processing (NLP) functions.

**`Exploratory Data Analysis (_EDA_)`**🔍📊📉

The `EDA` was conducted in a notebook using libraries such as pandas, matplotlib, seaborn and plotly. A comprehensive analysis of all variables was performed, including key assessments such as identifying null values, determining unique values in categorical features, and generating bar plots and box plots.
Following this initial analysis, a multi-variable examination was conducted, commencing with a pairplot and subsequently incorporating line and area plots to visualize correlations between years and various variables.

**`Analysis report`**📋📊📉

Created with `Streamlit`. Summary of the insights provided by the EDA.

**`Dashboard`**👩‍💼💻📊

The dashboard is created with `Streamlit`. In the dashboard, one can filter by year and by contiennt. The dashboard displays the `KPIs` previously defined, the number of accidents per cause in the previous 10 year() taking as current year the choosen year), the top 5 countries and aircraft type involved, general information of that year's accident (local time, day of the week, number of fatalities, cause), total fatalities and people aboard in the last 10 years, total fatalities on ground of the given year and number of accidents by continent.

<br/>

## **Technology Stack**

- Visual studio code
- Python
- Streamlit

<img src="src/vsc_logo.png" width="150"/><img src="src/python_logo.png" width="150"/><img src="src/streamlit_logo.png" width="150"/>

<br/>

## :warning: **Disclaimer** 

This personal project was developed for learning purposes. While exploring the contents of this repository and its associated API, it is paramount that the information presented and the results obtained **should not** be relied upon for making real-world decisions.

