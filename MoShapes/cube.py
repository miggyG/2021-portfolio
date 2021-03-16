class Cube:
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
    volume = l*w*h
    return volume

  #Volume
  def getSurfaceArea(l,w,h):
    area = 2*(l*w+l*h+w*h)
    return area

