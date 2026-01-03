# prueba hoja 40

def f (x,y): # type: ignore
    x = x + 3 # type: ignore
    y.append(23) # type: ignore
    print (x , y) # type: ignore

x = 22
y = [22]
f(x , y)
print (x , y)   

# numero octagonal se usa 0o

print(0o123)

# numero hexagonal, se usa 0x

print(0x123)