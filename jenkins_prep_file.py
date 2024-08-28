a = {"Car Name": "Polo",
     "Car Brand": "Wolkswagon",
     "Car Value": "5 Lacs"}

b = {"Car Name": "Swift",
     "Car Brand": "Suzuki",
     "Car Value": 650000}

x = b.values()
print(x)

b.update({"Car Value": 500000})
print(x)

b.update({"Car Color": "Black"})
print(b)

b.popitem()
print(b)

del b["Car Brand"]
print(b)
