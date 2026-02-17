import pandas as pd
from datetime import datetime
df=pd.read_csv('Restructured_Leads_Database.csv')

# Initialize new column recalculated_score

df["Recalculated_Score"]=0 #create new column

#Initiate process to build buyer scroing logic by classifying lead type into buyer

df["Buyer_Mask"]=df["Lead_Type"]=="Buyer" #Classify lead type into buyer

#Buyer scoring rules

df.loc[df["Buyer_Mask"] & (df["Email_Opened"]=="Yes"),"Recalculated_Score"]+=5 #using .loc select row and colum conditionally and add 5 points df.loc[ rows_condition , column_to_modify ] to recalculated score if conditions match
df.loc[df["Buyer_Mask"] & (df["Link_Clicked"] == "Yes"), "Recalculated_Score"] += 15 #df.loc[ rows_condition , column_to_modify ]
df.loc[df["Buyer_Mask"] & (df["Showing_Requested"] == "Yes"), "Recalculated_Score"] += 35 #df.loc[ rows_condition , column_to_modify ]
df.loc[df["Buyer_Mask"] & (df["Budget_or_Home_Value"] > 850000), "Recalculated_Score"] += 20 #df.loc[ rows_condition , column_to_modify ]
df.loc[df["Buyer_Mask"] & (df["Timeline"] == "0-3 months"), "Recalculated_Score"] += 25 #df.loc[ rows_condition , column_to_modify ]

#Initiate process to build seller scroing logic by classifying lead type into seller

df["Seller_Mask"]=df["Lead_Type"]=="Seller" #Classify lead type into seller

#Seller scoring rules

df.loc[df["Seller_Mask"] & (df["Email_Opened"]=="Yes"),"Recalculated_Score"]+=10 #using .loc select row and colum conditionally and add 10 points df.loc[ rows_condition , column_to_modify ] to recalculated score if conditions match

#Initiate categorization of leads into hot,war,cold buckets based on scoring

#define the function used for categorization

def categorize(Recalculated_Score):
    if Recalculated_Score >= 55: #We defined business logic thresholds for categorization
        return "Hot"
    elif Recalculated_Score >= 30:
        return "Warm"
    else:
        return "Cold"
#Apply categorize function to categorize the leads

df["Lead_Temperature"]=df["Recalculated_Score"].apply(categorize) #using .apply method to apply the categorize function to each value in the Recalculated_Score column and create a new column Lead_Temperature with the results
    
#test the modified dataframe
print(df.head(150))

#Save the modified dataframe to a new CSV file
df.to_csv("Modified_Leads_Database.csv", index=False)#keeping index=false prevents pandas from adding an extra unnecessary column

print("Scoring complete. File saved as Modified_Leads_Database.csv")
