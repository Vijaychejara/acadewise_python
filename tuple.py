thistuple = ("apple","apple","banana", "cherry")
print(type(thistuple))
print(thistuple)
print(thistuple.index("banana"))
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
