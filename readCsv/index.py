import pandas as pd

# df = pd.read_csv('startups.csv');
df = pd.read_csv('Position_Salaries.csv');
# print(df.to_string()) 

# perticularRow = pd.read_csv('startups.csv',nrows=1);
# print(perticularRow.to_string()) 
# perticularColumn = pd.read_csv('startups.csv',usecols=['State',"Administration"]);
# print(perticularColumn.to_string())

# print(df.index)   #for know index range
# print(df.columns)   #all columns name
# print(df.describe()) #discribe your data in min, max, mean, 50% etc
# print(df.head(2)) #get fix amount of data from top , bydefault get first 5
# print(df.tail(2)) #get fix amount of data from bottom , bydefault get last 5
# print(df[11:15]) #get data start 11 to 14
# print(df.State.array) #get perticularColumn data in array
# print(df.to_numpy()) #convert whole data in numpy array
# print(df.sort_index(axis=0, ascending=False)) #sorting data
# print(df.loc[[2,3],['Administration','State']]) #get specific data
# print(df.drop('State',axis=1)) #delete the perticular columns and row
# print(df.iloc[0,3]) #get perticular value

# changeValue =df.loc[0,'State'] = 'Gujrat' #chage the perticular value
# print(df.to_string())



#dropna()
# print(df.dropna(axis=1)) #delete that row which has empty cell

    # axis 
        # =>if axis = 1 so that is considering columns , if 0 that considering rows
        # =>if can't mentioned axis by default set 0

    # how()
        # =>how take two parameters ['any', 'all']
        # =>[any] remove rows which cell was empty 
        # =>[all] remove only rows which fully empty but can not remove that row which contain any one value

    #subet=["Column name"]
        # =>subset delete that row which contain empty cell in column that mention in subset not delete other rows
# print(df.dropna(subset=['Salary']))
    
    #implace=True
        # =>which makes the changes in data frame itself if True.

    # thresh: thresh takes integer value which tells minimum amount of na values to drop. 
# print(df.dropna(thresh=1))




#fillna()
# print(df.fillna('Shrut'))
# print(df.fillna({"Position":"CEO","Level":"10","Salary":1000000}))

    #method(['ffill','bfill'])
        # =>method parameter fill data auto from upper or lower depend on parameter
        # =>also can give axis=1 or 0

    #[value],inplace=True
        # =>value put in all empty cell

    #[value],limit = 2  
        # =>which row has 2 cell empty when put value



# plot()
# s.plot() or df.plot()
# plt.plot(kind)
    # =>kind:
        # line,bar,barh,hist,box,area,pie,scatter

import matplotlib.pyplot as plt 
df.plot(kind='line', color=['red','green','orange'])
plt.title('Position salary')
plt.xlabel('level')
plt.ylabel('Salary')
plt.show()