import pandas as pd
# df=pd.read_csv("RESOURCES/a08a1080b88344b0c8a7-0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
# print(df.to_string())
# print(df.corr())
# correlation=df['sepal_length'].corr(df['petal_length'])
# print(correlation)
df=pd.read_csv("RESOURCES/abalone.data.csv")
df.columns=['C1','C2','C3','C4','C5','C6','C7','C8','C9']
#df=df.drop(['C5','C6','C7','C8','C9'],axis=1)
df=df[['C2','C3','C4','C5']]
b=df.head(1000)
print(b)
b.dropna()
print(b.drop_duplicates())
print(b.corr())
print(b['C4'].corr(b['C5']))

