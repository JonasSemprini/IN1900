d = {0:6, 1:3, 2:7} 
print(d[1]) #skriver ut 3

d2 = {"Norway: "Oslo", "Sweden": "Stockholm", "France": "Paris"}
d2["Nepal"] = "Kathmandu"

d3 = {(0,0): "lowerleft", (1,1): "upperright"}

d.update(d2) #Legg en hel dictionary d2 til d

if key in d:
  print("Key: %s Value: %s" % (key, d[key]))
else:
  print("%s is not found" % key)

value = d.get(key)
if value != None:
  print("Key %s Value: %s" % (key, value))
else:
  print()

d.keys()
list(d.keys())#liste av nøkklene i dictionarien
d.values()
list(d.values()) #liste av verdiene i dictionarien
