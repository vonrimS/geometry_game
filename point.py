class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def falls_in_rectangle(self, rectangle):
    if rectangle.lowleft.x < self.x < rectangle.upright.x \
    and rectangle.lowleft.y < self.y < rectangle.upright.y:
      return True
    else:
      return False
  

  def distance(self, Point):
    d = ((Point.x - self.x)**2 + (Point.y - self.y)**2)**0.5
    return d




