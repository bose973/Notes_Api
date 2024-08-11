def give_name(fname : str,lname : str = "bose"):
    return fname+" "+lname

fname="bill"
lname="gates"
name = give_name(fname,lname)
print(name)