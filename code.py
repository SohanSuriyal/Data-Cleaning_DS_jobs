import pandas as pd
data=pd.read_csv("Uncleaned_DS_jobs.csv")
data["Salary Estimate"]=data["Salary Estimate"].str.extract(r"([$0-9-K]+)")
print(data["Salary Estimate"].head(30))
print(data)
data["Size"]=data["Size"].str.replace(" to "," - ").str.extract(r"([+0-9 -]+)")
data["Size"]=data["Size"].str.replace("-1","Not Classified")
data["Rating"]=data["Rating"].astype(str).str.replace("-","")
data["Revenue"]=data["Revenue"].str.extract(r"([$0-9 a-zA-Z+]+)").replace("1","Not Classified")
data["Company Name"]=data["Company Name"].str.extract(r"([A-Za-z0-9-. ]+)")
data["Industry"]=data["Industry"].str.replace("-1","Not Classified")
data["Type of ownership"]=data["Type of ownership"].str.replace("-1","Not Classified")

print(data["Company Name"].head(200))


data.drop(columns=["Competitors"],inplace=True)
data.drop(columns=["Sector"],inplace=True)
data.drop(columns=["Job Description"],inplace=True)
data.drop(columns=["Founded"],inplace=True)
data.drop(columns=["index"],inplace=True)
data.drop(columns=["Headquarters"],inplace=True)

print(data)
data.to_csv("Cleaned.csv",index=False)
