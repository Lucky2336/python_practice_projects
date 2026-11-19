import re

t = "The rain in Spain"
x = re.search("^The.*Spain$", t)
y = re.search(r"\bS\w+", t)
print(x.span())
print(y.start())



txt = "neuziland"

#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))

#Without the flag, the example would return all character:
print(re.findall("\w", txt))


#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))