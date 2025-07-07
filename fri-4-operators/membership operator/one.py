enames =['RG','SG','PG']  #list
st_names=('Rahul','sonia')  #touple
eis={101,102,103,104}  #set
byte_values=bytes([0,25,35,45,55])
ba_values=bytearray([0,25,35,45,55])
fz_values=frozenset({0,25,34,333})
range_values=range(500)
ename="Rahul Gandhi"
print('RG' in enames)
print('Z' in enames)
print('Rahul' in st_names)
print('Rajesh' in st_names)
print(101 in eis)
print(466 in eis)
print(35 in byte_values)
print(55 in ba_values)
""" print(333 in frozenset) """#type error
print(333 in fz_values)
print(456 in range_values)
print(500 in range_values)
print(0 in range_values)
print("Rahul Gandhi" in ename)
print("Gandhi" in ename)


# here we use in and not in 
print(333 in fz_values)
print(333 not in fz_values)


#to verify element present in sequence or not



