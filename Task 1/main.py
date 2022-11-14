# Turimas "users" masyvas. 

# Parašykite funkciją "filterAdultDogOwers", kuri atlikas nurodytas veiksmsus:
# 1. Kaip argumentą priims masyvą
# 2. Grąžins pilnamečius "users", kurie turi augintinį.

users = [
  { "id": '1', "name": 'John Smith', "age": 20, "hasDog": True },
  { "id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False },
  { "id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True },
  { "id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False },
  { "id": '5', "name": 'Alex John', "age": 25, "hasDog": True },
  { "id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True },
  { "id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True },
  { "id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False },
  { "id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True },
]


def filterAdultDogOwers(users):
  return list(filter(lambda user: user["hasDog"] and user["age"]>= 18, users))
  
print(filterAdultDogOwers(users))