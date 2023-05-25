import davipy as dv #import the library

#you can put relative or absolute path it doesnt matter

#README
#but if you put relative path, you must have your dataframe in the same folder as 
#your program file

#define your dataframe

dataframe = "realwage.csv"

#use this function
dv.reportfile(dataframe)

#it will generate a file with a quick report of your dataframe


#you can even use a for

dataframes = ["realwage.csv", "titanic3.xls"]

for dataframe in dataframes:
    dv.reportfile(dataframe)