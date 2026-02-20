#Using boolean mask to detect dormant leads

import pandas as pd

#load the data
df=pd.read_csv("Restructured_Leads_Database.csv")

#covert last activity date to datetime format(currently string), errors=coerce handles missing data as NaT not a time, which is useful for handling missing or invalid date entries without causing errors in the code. It allows the code to continue running smoothly even if there are issues with the date data.

df["Last_Activity_Date"]=pd.to_datetime(df["Last_Activity_Date"],errors='coerce')

#defnining todays date
today=pd.Timestamp.today().normalize() #normalize to remove time component, today() will give both date and time

#Calculate dormancy days, dormant if inactive for 60+ days

df['Is_Dormant']=(today-df['Last_Activity_Date']).dt.days >=60 #appending dt (date) property , further adding days property to get the output in days and notin months

#NORMALIZE() IS A FUNCTION/METHOD AND .DT.DAYS IS A PROPERTY/ATTRIBUTE

#Segmenting dormant buyers
df['Dormant_Buyer']=df['Is_Dormant']&(df['Lead_Type']=='Buyer') #using boolean mask to segment dormant buyers

#Segment dormant sellers
df['Dormant_Seller']=df['Is_Dormant']&(df['Lead_Type']=='Seller') #using boolean mask to segment dormant sellers

#test the modified dataframe
print(df.head(100))

#Total count of dormant leads
print("Total Dormant Leads:",df['Is_Dormant'].sum())

#Total count of dormant buyers
print("Total Dormant Buyers:",df['Dormant_Buyer'].sum())

#Total count of dormant sellers
print("Total Dormant Sellers:",df['Dormant_Seller'].sum())

# Calculate Percentages
total_leads = len(df)
dormant_percentage=round((df['Is_Dormant'].sum()/total_leads)*100,2)#rounding to 2 decimal places


# Calculate percentage of dormant leads
print("--------Summary----------")
print(f"Total_Leads:{total_leads}")#f-string, formatted string, lets you embed variable directly in the string using curly braces {}
print(f"Percentage of Dormant Leads:{dormant_percentage}%")

#Save the modified dataframe to a new CSV file
df.to_csv("Modified_for_Dormancy_Leads_Database.csv", index=False)#keeping index=false prevents pandas from adding an extra unnecessary column

print("Dormant detection complete. File saved as Modified_for_Dormancy_Leads_Database.csv")
