import davipy as dv


example_lower_str = "ciaoatutti"
string_with_upper = dv.stringUPPER(example_lower_str, 5, 10)
print(string_with_upper)

# you can even do it with only 1 character
print(dv.stringUPPER(example_lower_str, 3))  # Excepted result ...


example_upper_str = "HELLOEVERYONE"
# define your new string and choose a range it will upper scale from 6 to 12
print(dv.stringlower(example_upper_str, 6, 13))

# you can even do it with just one character
print(dv.stringlower(example_upper_str, 5))
