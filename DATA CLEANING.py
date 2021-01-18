import pandas as pd
data=pd.read_csv("RESOURCES/a08a1080b88344b0c8a7-0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
print(data)
print(data.drop_duplicates())
print(data.loc[0])
print(data.info())
data.dropna(inplace=True)
print(data.info())
a=data.fillna(120)
print(a)
a=data.drop("the_geom",axis=1)
print(a)
a=data.drop([12])
print(a)
print(data)
print(data["the_geom"])
data.loc[7,"the_geom"]="none"
print(data["the_geom"])
for x in data.index:
    if (data.loc[x,"sepal_length"]>5):
        data.loc[x,"sepal_length"]=6
print(data["sepal_length"])
for x in data.index:
    if data.loc[x,'sepal_length']<6:
        data.drop(x,inplace=True)
print(data['sepal_length'])
