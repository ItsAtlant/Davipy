import davipy as dv

# you can put relative or absolute path it doesnt matter

# README
# but if you put relative path, you must have your dataframe in the same folder as
# your program file


filename = "realwage.csv"
dv.reportfile(filename)  # it generates a dataframe report of your dataframe (.txt format)


# multiple dataframes usage
dataframes = ["realwage.csv", "titanic3.xls"]
for dataframe in dataframes:
    dv.reportfile(dataframe)
