import math
# 1. Write a program to receive the side of a square and calculate its arealassit min

# 2. Write a program to receive the base and height of a triangle and calculate its area
# 3. Write a program to receive the radius and calculate the area of a circle
# 4. Write a program to receive the factors a, b and c of a quadratic equation and return its solutions

# Select what to calculate
selection = input("What would you like to calculate? Options:\nsquare-area\ntriangle-area\ncircle-area\nquadratics\nChoose one:")
if selection == "square-area": # Calculate area of square
  side = int(input("Enter side length of square:")) # Recieve the side while converting to int at the same time
  area = side * side # apply formula
  print("Area of a square with side lengths of {} is {}".format(side,area)) # output
elif selection == "triangle-area": # Calculate area of triangle
  base = int(input("Enter triangle base length:")) # get base length
  height = int(input("Enter triangle height:")) # get triangle height
  area = base * height / 2
  print("Area of triangle with base length of {} and height of {} is {}".format(base,height,area))
elif selection == "circle-area": # Calculate area of circle (pi*r*2)
  mode = input("Would you like to use:\nradius\nOR\ndiameter\nChoose one:")
  if mode == "radius":
    radius = float(input("Enter circle radius:"))
  elif mode == "diameter":
    radius = float(input("Enter circle diameter:"))/2
  area = math.pi*radius*2
  print("Area of circle with a radius of {} is {}".format(radius,area))
elif selection == "quadratics":
  a = float(input("Enter the coefficient a: "))
  b = float(input("Enter the coefficient b: "))
  c = float(input("Enter the coefficient c: "))
  discrim = b**2 - 4*a*c
  if discrim >= 0:
    root1 = (-b + math.sqrt(discrim)) / (2*a)
    root2 = (b - math.sqrt(discrim)) / (2*a)
    solution = root1, root2
  else:
    solution = None
  if solution != None:
    print("The solutions are {} and {}".format(solution[0],solution[1]))
  else:
    print("There are no real solutions.")



