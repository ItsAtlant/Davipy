import davipy as dv #import the library

#define your list that you want to check

list_with_duplicates = [1,2,2,2,3,1,1,1,4,52,2,1,5,6]

#save your new list
list_without_duplicates = dv.listremoveduplicate(list_with_duplicates)

#print it
print(list_without_duplicates)


#you can even do it with strings
list_with_duplicates = ["Luca","Marco","Lucia","Luigi","Lucia","Devid","Lucia","Luca"]
#so define your list
list_without_duplicates = dv.listremoveduplicate(list_with_duplicates)
#print it
print(list_without_duplicates)

