from random import randint


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def falls_in_rectangle(self, rectangle):
    if rectangle.point1.x < self.x < rectangle.point2.x \
    and rectangle.point1.y < self.y < rectangle.point2.y:
      return True
    else:
      return False

  def distance(self, Point):
    d = ((Point.x - self.x) ** 2 + (Point.y - self.y) ** 2) ** 0.5
    return d


class Rectangle:
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def area(self):
    return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

  def __str__(self):
    return ('Rectangle coordinates: ' +
            str(self.point1.x) + ', ' +
            str(self.point1.y) + ' and ' +
            str(self.point2.x) + ', ' +
            str(self.point2.y) + '\n' +
            'Rectangle area: ' + str(self.area())
            )

# create rectangle object
r1 = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))

print(r1)

# get point and area from user
user_input = Point(float(input('Guess X: ')), float(input('Guess Y: ')))

print(user_input.falls_in_rectangle(r1))




