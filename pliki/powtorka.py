#print("hello")
#print("world")
print("hello \n world")

x = 2
print(x)
print("x=", x)

y = input("y=?")
print(type(y))
print(type(float(y))) # tu zmieniami typ y tylko dla funkcji print
print(type(y)) # z y nic nie zrobiliśmy globalnie, nadal jest str

y = float(y) # tu następuje zmiana typu y
print(type(y))

