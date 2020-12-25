import turtle
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("black")

def S(x):
    t.speed(x)
S(1000)

def cir(x):
    t.circle(x)
def col(y):
    t.pencolor(y)
color = ['yellow','blue','green','red']


'''
for c in color:
    col(c)
    for i in range(360):
        cir(i)
        t.lt(i)
  '''  

print("fffffff")

for i in range(360):
    for c in color:
        col(c)
        cir(i)
        t.lt(i)

