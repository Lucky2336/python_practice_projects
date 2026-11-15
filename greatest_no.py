def greater_no(a, b, c):
    if a> b and a> c:
        return a
    if b > a and b> c: return b
    if c > a and c > b: return c

a = 2    
b = 3
c = 4    
print(greater_no(a, b, c))
