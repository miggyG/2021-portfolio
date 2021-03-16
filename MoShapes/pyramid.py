import math
class Pyramid:
  #variables
  l = 0
  w = 0
  h = 0
  
  #constructor
  def __init__(self,l,w,h):
    self.l = l
    self.w = w
    self.h = h

  #Volume
  def getVolume(l,w,h):
    volume = 0.3333333*((l*w)*h)
    return volume

  #surface area
  def getSurfaceArea(l,w,h):
    area = (l*w)+((l*math.sqrt(((w/2)*(w/2))+(h*h)))+(w*math.sqrt(((l/2)*(l/2))+(h*h))))
    return area
