import math
diameter = input("Please Input the Diameter of a Circle: \n")

while True:
    if diameter.isnumeric():
        if float(diameter) > 0:
            diameter = float(diameter)
            area = math.pi*(diameter/2)**2
            circumference = math.pi*diameter
            print("The area and circumference of a circle is:")
            print("Area:", area, "Circumference:", circumference)
            break
        else:
          diameter = input("Incorrect input. Please input valid diameter: \n")
    else:
      diameter = input("Incorrect input. Please input valid diameter: \n")