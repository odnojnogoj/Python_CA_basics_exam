# Sukurkite funkciją "addDigits", kuri priims sveiką skaičių nuo 10 iki 999 ir grąžins jo skaitmenų sumą. 

# Pvz.
# Jeigu duota 34, funckiją turėtų grąžinti 7.
# Jeigu duota 999, funckija turėtų grąžinti 27.


def addDigits(number):
  if number < 10 or number > 999:
    return print("Error. Input number from 10 to 999!")
  elif number % 1 != 0:
    return print("Error. Input whole number!")
  else:
    sum = 0
    for digit in str(number):
      sum += int(digit)
    return sum

print(addDigits(34))
print(addDigits(999))
