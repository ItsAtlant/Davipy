import davipy as dv #import the library


#define your string 
your_string = "ciaoatutti"


# define your new string and choose a range it will upper scale from 5 to 9
string_with_upper = dv.stringUPPER(your_string,5,10)
#print it
print( "\n\n\n\n"+string_with_upper+ "\n\n\n\n")

# you can even do it with only 1 character
string_with_1_upper = dv.stringUPPER(your_string,3)
#print it
print(string_with_1_upper+ "\n\n\n\n")



#you can do the same thing with the lower


#define your string 
your_string = "HELLOEVERYONE"

# define your new string and choose a range it will upper scale from 6 to 12
string_with_lower = dv.stringlower(your_string,6,13)
#printit
print(string_with_lower+ "\n\n\n\n")

# you can even do it with only 1 character
string_with_1_lower = dv.stringlower(your_string,5)
#printit
print(string_with_1_lower + "\n\n\n\n")