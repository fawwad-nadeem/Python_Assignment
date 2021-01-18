# number_of_sub = eval(input("Enter number of Subjects: "))
# number_of_certification = eval(input("Enter number of Certifications: "))
# if number_of_sub == 3 and number_of_certification == 2:
#     print("Student is enrolled in 3 subjects with 2 certifications")
# elif number_of_sub == 2 and number_of_certification == 3:
#     print("Student is enrolled in 2 subjects with 3 certifications")
# else:
#    print("not enrolled")
# passwords = [10, 33, 44, 78, 100, 443, 556, 77, 55]
# for x in passwords:
#     if x > 500:
#         print("Password cannot be greater then 500")
#         break
#     else:
#         print("The password is: ", x)
# import pandas as pd
# import numpy as np
# print(df)
# print(" ")
# print("This is Column One:", df["one"])
# print("")
# print(df.loc['a'])
# df=pd.DataFrame(np.random.rand(3, 3),index=['a', 'b', 'c'], columns=['one', 'two', 'three'])
# df=df.reindex(['a','b','c','d','e'])
# print(df)
# print("")
# df=df.fillna('null')
# print(df)
# print("")
# df=df.reindex(columns=['one','two','three',"four"])
# print(df)
# DATA={
#     "Column 1":[1,2,3],"Column 2":[4,5,6],"Column 3":[7,8,9]
# }
# df=pd.DataFrame(DATA,index=[1,2,3])
# print(df)
# print("")
# df=df.reindex(columns=["Column 1","Column 2","Column 3","Column 4"])
# print(df)
# df=df.fillna(0)
# print(df)
# import matplotlib.pyplot as plt
# x_quad = [n/10 for n in range(0,  100)]
# y_quad = [(n-4)**2+5 for n in x_quad]
# plt.figure(figsize=(10,7))
# plt.plot(x_quad, y_quad, 'k--')
# plt.axis([0,10,0,30])
# plt.plot([1, 2, 3], [14, 9, 6], 'ro')
# plt.plot([5, 7, 8],[6, 14, 21], 'bo')
# plt.plot(4, 5, 'ko')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Quadratic Equation')
# plt.show()
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# data=pd.read_csv("RESOURCES/a08a1080b88344b0c8a7-0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
# print(data)
# print("")
# df1=data['sepal_length']
# print(df1)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("RESOURCES/a08a1080b88344b0c8a7-0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
print(data)
df1=data['sepal_length']
df2=data['petal_length']
plt.figure(figsize=(6,4))
plt.plot(df1,df2,'kx')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()
