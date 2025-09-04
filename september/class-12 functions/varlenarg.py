""" def sum(a,b):
    print(a,b)

sum(1,2)
sum(1,2,3)
sum(1,2,3,4)
sum(1,2,3,4,5)
sum(1,2,3,4,5,6) """


def sum(a,*b):
    print("a value--""a","b value---""b")

sum(1,2)
sum(1,2,3)
sum(1,2,3,4)
sum(1,2,3,4,5)
sum(1,2,3,4,5,6)