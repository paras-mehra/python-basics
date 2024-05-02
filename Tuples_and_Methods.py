t = (1111,222,333,444,555,666,777,888,999)
print(t[0:2])

print(t.count(1111))
print(t.index(333))


t[0] = 20 # Tuples are immutable and hence this line throws an error 
print(t)