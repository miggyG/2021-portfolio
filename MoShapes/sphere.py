class Sphere:
  #variables
  l = 0
  
  #constructor
  def __init__(self,l):
    self.l = l

  #Volume
  def getVolume(l):
    volume = (4*3.14159265358979323*(l*l*l))/3
    return volume

  #Surface area
  def getSurfaceArea(l):
    area = 4*(l*l)*3.14159265358979323
    return area
