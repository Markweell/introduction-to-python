#string
print(type("Hello word")) # str
print(type('Hello word')) # str
print(type('''Hello word''')) # str
print(type("""Hello word""")) # str

# Number 
print(type(30)) # int
print(type(30.3 )) # float

# Bolean
print(type(False)) # bool

# List
print(type([12,123,123,123])) # List
print(type([12,False,123,'string'])) # List

# Tuplas
print(type((10,12,12,'123'))) # Tupla, como una lista, pero inmutable

# Dictionaries.
print(type({"name": "Marcos"})) # dict

# None
print(type(None))