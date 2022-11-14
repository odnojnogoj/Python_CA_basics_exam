# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserMedianAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus medianą.
# 2. funkcija "getOldestUser" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins vyriausio vartotojo vardą.

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

from statistics import median

def getUserMedianAge(users):
  return median([x["age"] for x in users])

print(getUserMedianAge(users))

def getOldestUser(users):
  age = max([x["age"] for x in users])
  oldest = list(filter(lambda user: user["age"] == age, users))
  return oldest[0]["name"]

print(getOldestUser(users))