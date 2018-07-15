import pandas as pd
import numpy as np


def readIrish():
    data = []
    file = open("dataset.txt","r")

    for i in range(150):
        data.append(np.random.dirichlet(np.ones(5), size=1))

    i = 0
    for line in file:
        fields = line.split(",")
        field1 = fields[0]
        field2 = fields[1]
        field3 = fields[2]
        field4 = fields[3]
        field5 = fields[4]

        print field1, field2, field3, field4, field5

        data[i] = [float(field1), float(field2), float(field3), float(field4), field5]
        i+=1

    return data

data = readIrish()

print data[0]
df = pd.DataFrame(data,columns=['sepal length','sepal width', ' petal length', ' petal width', 'class' ])
print df

#to find out the ndim- number of dimensions
#size
#need to conver data inot series or can use the data frame
print pd.Series(data).size
print df.ndim

#produce the mean, std, min, max etc
print df.describe()

#change the column or row
# I changed column for [0,1,2,3,4,149 recors]
#display only those records with changed column names
df_reindexed = df.reindex(index=[0,1,2,3,4,149], columns=['class','sepal length','sepal width', ' petal length', ' petal width' ])
print df_reindexed


##### iteration ##########

#print columns
for col in df:
   print col

#based on the keys display the data values
#sepal length
#1- 150
#sepel width 1
#1-150 
for key,value in df.iteritems():
   print key,value

#take one item and display all the features with the name
#sepal lenght 2.3
#etc
for row_index,row in df.iterrows():
   print row_index,row

#display as a tuple
for row in df.itertuples():
    print row


######### sorts ############

#sort based on the index
sorted_df=df.sort_index(ascending=False)
print sorted_df

#sort based on a column
sorted_df=df.sort_index(axis=1)

print sorted_df

##########rolling ####
print df.rolling(window=3).mean()

## check null ##########
print df['class'].isnull()


print df['sepal length'].sum()


####### group by ###########

#display group and indexes
print df.groupby('class').groups

grouped = df.groupby('class')

for name,group in grouped:
    print name
    print group

#print the grup in rows
#print attribute like sepal lenght ....... in colums
#fill with the size
print grouped.agg(np.size)


#plot
df.plot()