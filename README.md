# galvanize_mid_term_project
Analysis of the U.S. Customs and Border Protection's Nationwide Encounters FY21_FY24 dataset.
1. Overview of the Project.
   The purpose of this project is to display general data from the U.S. Customs and Border Protection's Nationwide Encounters FY21_FY24 dataset. Specifically, due to national security concerns, emphasis is placed on encounters with citizens from China, Russia, and Venezuela.
  
2. Project Proposal or Research Question.
   - What is the sum of the total encounters count by fiscal year?
   - What is the sum of the total encounters by month and fiscal year?
   - Sum of total the total encounters by fiscal year and month with statistics.
   - What are the max and min values of the total encounters count?
   - What is the sum of total encounters count by citizenship and fiscal year? 
   - Trend line of the sum of total encounters by citizenship and fiscal with statistics. 
   - Yearly trendline of demographics by fiscal year.
   - Trend line of total encounters by FY and month for citizens == ‘China’ with statistics. 
   - Trend line of total encounters by FY and month for citizens == ‘Russia’ with statistics. 
   - Trend line of total encounters by FY and month for citizens == ‘Venezuela’ with statistics.
  
3. Describe the Source of Data.
   - Encounters data includes U.S. Border Patrol Title 8 apprehensions, Office of Field Operations Title 8 inadmissibles, and all Tilt 42 expulsions for fiscal years 2020 to date. Data is available from the Northern Land Border, and Natiowide(i.e.,air, land, and sea modes of transportation) encounters.
   - Data is extracted from live CBP systems and data sources. Statistical information is subject to change due to corrections, systems changes, change in data definition, additional information, or encounters pending final review. Final statistics are available after each fiscal year.
   - (https://www.cbp.gov/newsroom/stats/cbp-public-data-portal)
   - (https://www.cbp.gov/document/stats/nationwide-encounters)
   - (https://www.cbp.gov/sites/default/files/assets/documents/2023-Sep/nationwide-encounters-data-dictionary.pdf)
  
4. Describe how you cleaned and transformed data. 
   a. Used the following Python libraries: pandas, numpy.
   b. Saved the original dataset in a data frame with a variable known as encounters_aor_df.
   c. Reviewed encounters_aor_df to gather general information related to the number of columns and data type.
   d. Changed the data type for the 'Fiscal Year' column from int64 to an object.
   e. Verified the data frame had the correct data types.
   f. Saved data frame into a new variable 'encounters_aor_cleaned_df.
   g. Dropped the 'Month Grouping' column.
   h. Renamed the columns 'Month (abbv)' and 'AOR (abbv)' to 'Month' and 'AOR'.
   i. Replace a value in the 'Citizenship' column from 'CHINA, PEOPLES REPUBLIC OF' to 'CHINA'.
   j. Created the column 'Continent' to group each 'Citizenship' country with their respective continent into the 'Continent' column.
   k. Saved the cleaned data frame into a new variable called 'encounters_aor_df'.
   l. Review unique values in columns to identify unknown data points.

5. Contextual Visualizations. What visualizations do we need to understand your topic?
   a. Bar chart.
   b. Heatmap.
   c. Stacked bar chart.
   d. Line plot.
   f. Plotly tables.
   g. Interactive tables with plotly.

6. Show objective specific visualizations.
   a. Bar chart to display the sum of Total Encounters by Fiscal Year.
   b. Bar chart and heatmap to display the sum of Total Encounters by Fiscal Year and month.
   c. Line plot to display the trend line of Total Encounters by Fiscal Year with a table to display statistics.
   d. Bar chart to display the Max and Min values of the total Encounters by FY.
   e. Stacked bar chart to display the Total Encounters by Citizenship and Fiscal Year.
   f. Line chart and plotly tables to display the trend line of Total Encounters by Citizenship and Fiscal Year with statistics.
   g. Yearly trend of demographics by fiscal year.
   h. Line chart to display the trend of Total Encounters by Fiscal Year and Month for Citizenship == China.
   i. Line chart to display the trend of Total Encounters by Fiscal Year and Month for Citizenship == Russia.
   j. Line chart to display the trend of Total Encounters by Fiscal Year and Month for Citizenship == Venezuela.

7. Present Key Insights. 
   a. Bar chart. Bar chart depicting the sum of total encounters by fiscal year FY21-FY24.
   b. Bar chart/heatmap. On the left side, we have a bar chart highlighting the total encounters by fiscal year showing December of FY24 with the highest number of encounters among the rest of the months and FYs. On the right side we have a heat map displaying the actual numbers for total encounters also highlighting the month of December of FY24 with the highest number of encounters with 370,883.
   c. Line plot. Depicting the trend line of total encounters by FY with statistics. This line plot highlights a constant increase in encounters from FY21 to FY23 with a slight decrease in the first quarter of FY24/ The tren line represents an upward pattern of increase from FY21 to FY24. The main takeaway from this chart is to identify FY23 as the year with the most encounters with 3,201,144 encounters.
   d. Bar chart. This bar chart represents the maximum and minimum number of encounters by fiscal year. The maximum number of encounters occurred during fiscal year FY23 with 3,201,144 encounters and the minimum number of encounters occurred in FY21 with a total number of 1,956,519 total encounters.
   e. Stacked Bar Chart. This is a stacked bar chart depicting the sum of total encounters by citizenship and fiscal year. Mexican citizens have the highest number of encounters with 2,901,821, followed by Guatemala with 946,172 encounters, and Honduras with 896,525 encounters.
   f. Line chart and Table. The citizenships represented by the trend lines show a mix of increases and decreases in encounters across the fiscal years.
   g. Line chart. This line chart depicts the four demographics categories used by the U.S. Customs and Border Protection to identify people based on age, admissibility, and relationship. Single Adults represented by the green line show an increase during during FY21, 22, and 23 with a slight decrease in the first quarter of fiscal year 2024. The Family Unit show a similar pattern but with smaller numbers of encounters, followed by the Single and Accompanied Minors with almost straight lines across the fiscal years.
   h. Line chart. This line chart depicts a mix of increases and decreases in total encounters across the fiscal years. The most significant number of encounters occurred during December of FY23 with 9.927 encounters followed by September of FY23 with 7,271 encounters. 
   i. Line chart. This line chart depicts a mix of increases and decreases in total encounters across the fiscal years. The most significant number of encounters occurred during December of FY24 with 8,615 encounters followed by November of FY23 with 6,931 encounters.
   j. Line chart. This line chart depicts a mix of increases and decreases in total encounters across the fiscal years. The most significant number of encounters occurred during September of FY23 with 72,325 encounters followed by December of FY24 with 62,852 encounters.

8. Tell us what (if anything) you recommend.
   - Continue to monitor CBP's nationwide encounter dataset to analyze the total encounters trend.
  
9. Tell us what future areas you might want/need to study.
    - Conduct an analysis of the Nationwide encounters dataset from FY17-FY18 to identify patterns in increases and decreases of encounters by the three citizenships mentioned in this presentation. 

    - Gather both datasets and attempt to predict the Nationwide encounters for FY25.

    - Identify correlation of data points based on factors such as Presidential Elections and economic situations in China, Russia, and Venezuela. 

