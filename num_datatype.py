a = 50
print(a, "is of type", type(a))

b = 60.5
print(b, "is of type", type(b))
print(b, "is complex number?", isinstance(60.5, int))

c = 1 + 2j
print(c, "is complex number", isinstance(1 + 2j, complex))