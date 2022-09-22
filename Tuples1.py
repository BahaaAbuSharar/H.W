# Ex1:
tuple1 = (10, 20, 30, 40, 50)
c = ()
for i in tuple1:
    c = (i,) + c
print(c)
