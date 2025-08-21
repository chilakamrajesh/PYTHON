d1={}
emp={
    'eid':101,
    'ename':"Rahul gandhi",
    'esal':450000,
    'email':'rg@gamil.com',
    'email':'sg@gmail.com'
}
#print(emp['loc'])  #keyError
#update
print("*Updating")
emp['ename'] = "sonia gandhi"
emp['avail']=False     #new key:value pair added
print(emp)