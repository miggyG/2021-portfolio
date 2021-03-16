from cube import Cube
from sphere import Sphere
from pyramid import Pyramid

print("welcome to shape calculator. Lets find the surface area and volume of some shapes")
play = True
while play== True:

  whatshape = input("what shape would you like to use Box, Sphere, or Pyramid: ")
  whatshape = whatshape.lower()

  #For a box
  if whatshape == "box":
    print("for a box we will need the Width the Length and the Height")
    w = input("what is the Width: ")
    l = input("what is the Lenght: ")
    h = input("what is the Height: ")
    v = Cube.getVolume(int(l),int(w),int(h))
    a = Cube.getSurfaceArea(int(l),int(w),int(h))
    print("The Volume of your box is: ",round(v,6))
    print("The Surface Area of your box is: ",round(a,6))

    #For a sphere
  elif whatshape == "sphere":
    print("for a Sphere we will neeed the total Length(the diamater)")
    l = input("what is the Length: ")
    l = int(l)/2
    v = Sphere.getVolume(l)
    a = Sphere.getSurfaceArea(l)
    print("The Volume of your sphere is: ",round(v,6))
    print("The Surface Area of your sphere is: ",round(a,6))

    #For a pyramid
  elif whatshape == "pyramid":
    print("for a pyramid we will need the Width the Lenght of the base and the Height of the pyramid")
    w = input("what is the Width: ")
    l = input("what is the Lenght: ")
    h = input("what is the Height: ")
    v = Pyramid.getVolume(int(l),int(w),int(h))
    a = Pyramid.getSurfaceArea(int(l),int(w),int(h))
    print("The Volume of your pyramid is: ",round(v,6))
    print("The Surface Area of your pyramid is: ",round(a,6))

    #if what they entered was invalid
  else:
    print("what you entered was invalid please enter Cube Sphere or Pyramid")
  
  playAgain = input("Would you like to try another shape:(y/n) ")
  playAgain = playAgain.lower()
  if playAgain == "y":
    play = True
  else:
    print("Hope to see you again!")
    play = False