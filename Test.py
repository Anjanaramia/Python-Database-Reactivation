import pandas as pd
from Reactivation_Engine import process_crm
df=pd.read_csv('Restructured_Leads_Database.csv')
dormancy_days=60
temp_thresholds=[30,90,180]
df,buyer_dormant,seller_dormant,summary=process_crm(df,dormancy_days=dormancy_days,temp_thresholds=temp_thresholds)
print(df.head())

