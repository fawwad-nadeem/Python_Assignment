import pandas as pd
Student_Dataset={
    'Name': ['ALI','SAAD','BILAL','USAMA','AHMED',"RAZA",'ZAHEEM',"JIBRAN"],
    'ENGLISH':[78,88,56,33,88,90,78,45]
}
result=pd.DataFrame(Student_Dataset,index=[1,2,3,4,5,6,7,8])
print(result)