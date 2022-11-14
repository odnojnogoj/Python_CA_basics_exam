# Turimas sąrašas, pvz.:

# canvas = [
#   "abc",
#   "ded"
# ]

# Sukurkite funkciją "addFrame", kuri pridėtų rėmelį ir grąžintų pamodifikuotą sąrašą:

# canvas_with_frame = [
#   "*****"
#   "*abc*",
#   "*ded*",
#   "*****"
# ]

# Pastaba: sąrašas gali ir neturėti nei vieno elemento arba turėtų tusčių elementų. pvz.
# canvas = [] arba canvas = [""]

# Jeigu sąrašas yra tusčias arba visi elementą tušti išmeskite klaidą - "Error: empty canvas provided".
# Beje, sąraše esantis tekstas, gali būti ir skirtingo ilgio. Todėl rėmelis turėtų būti brėžiamas pagal ilgiausią saraše esantį elementą.


canvas = ["a", "ee", "fff"]
print("Initial list: ", canvas)

def addFrame(canvas):
  if len(canvas) == 0 or not any(canvas) == True:
    return print("Error: empty canvas provided")
  else:
    canvas_with_frame = canvas.copy()
    for index, item in enumerate(canvas_with_frame):
      canvas_with_frame[index] = "*" + item + "*"
    frame = "*" * (len(max(canvas_with_frame, key=len)))
    canvas_with_frame.insert(0, frame)
    canvas_with_frame.append(frame)
    return print("Framed list: ", canvas_with_frame)
    
addFrame(canvas)
