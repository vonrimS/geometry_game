from random import randint
import turtle

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

class GuiRectangle(Rectangle):
  def draw(self, canvas):
    # go to a certain coordinate
    canvas.penup()
    # side a, side b
    a = self.point2.x - self.point1.x
    b = self.point2.y - self.point1.y
    # get new coordinate of point1
    canvas.goto(self.point1.x, self.point1.y)
    canvas.pendown()
    canvas.forward(a)
    canvas.left(90)
    canvas.forward(b)
    canvas.left(90)
    canvas.forward(a)
    canvas.left(90)
    canvas.forward(b)
    # finish drawing



class GuiPoint(Point):
  def draw(self, canvas, size=15, color='red'):
    canvas.penup()
    canvas.goto(self.x, self.y)
    canvas.pendown()
    canvas.dot(size, color)
    turtle.done()


# gui_rectangle = GuiRectangle(Point(randint(0, 90), randint(0, 90)),\
#                              Point(randint(100, 400), randint(100, 400)))
#
# # canvas
# canvas = turtle.Turtle()
#
# gui_rectangle.draw(canvas=canvas)
# print(gui_rectangle.area())


# create rectangle object
r1 = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))

print(r1)

# get point and area from user
user_point = GuiPoint(float(input('Guess X: ')), float(input('Guess Y: ')))
user_area = float(input('Guess rectangle area: '))

# print the result
print('Your point was inside rectangle: ', user_point.falls_in_rectangle(r1))
print('Your area was off by: ', r1.area() - user_area)

myturtle = turtle.Turtle()
r1.draw(canvas=myturtle)

user_point.draw(canvas=myturtle)