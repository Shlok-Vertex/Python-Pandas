import pandas as pd

l = [1,2,3,4,5]
x = [1, 2, 3, 4, 5]

var = pd.DataFrame(l)
var1 = pd.Series(x,index=['a', 'b', 'c', 'd', 'e'], name='numbers')
print(var)
print(var1)
print(type(var))
print(type(var1))