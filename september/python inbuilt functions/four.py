numbers=[11,18,31,7,8,232,1055]
def even_no(num):
    return num%2==0


filter_obj=filter(even_no,numbers)
print(filter_obj)