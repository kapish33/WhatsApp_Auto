import pandas as pd

df=pd.read_csv("contact.csv")

contact_Names=df['Name'].to_list()
contact_Number=df['Contact'].to_list()