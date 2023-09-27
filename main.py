#Using curly brackets#
hagop={"Age": 17, "Aprx Weight": 195, "Aprx Height": "6'1"}
print(hagop); print()

#Using dict() function#
hagop=dict(age=17, aprxWeight=195, aprxHeight="6'1")
print(hagop);print()

#Nested Dictionaries#
ketchedjians={"Hagop": {"Age": 17, "Aprx Weight": 195, "Aprx Height": "6'1"}, "Vatche": {"Age": "Chem kider", "Aprx Weight": 210, "Aprx Height": "6'0"}}
print(ketchedjians);print()

#Accessing Info#
print(hagop["age"]); print()
print(hagop.keys()); print()
print(hagop.values()); print()
print(hagop.get("aprxHeight")); print()

for i in hagop:
  print(i)
print()
for i in hagop.values():
  print(i)
print()
for x, y in hagop.items():
  print(x, y)
print()

#Updating Values#
hagop["age"]= 18
hagop["church"]= "tbir"
print(hagop); print()

#Deleting Items#
hagop.pop("age")
print(hagop); print()
hagop.popitem()
print(hagop); print()
del hagop["aprxWeight"]
print(hagop); print()