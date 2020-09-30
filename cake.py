import turtle
from PIL import Image


def goto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def yuan():
    turtle.color('#FFFFFF',"#FF9933")
    goto(0,-200)
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()

def huabian():
    goto(0,0)
    turtle.color('#FF9933')
    for _ in range(20):
        turtle.right(18)
        turtle.begin_fill()
        turtle.forward(220)
        turtle.circle(40,180)
        turtle.goto(0,0)
        turtle.right(180)
        turtle.end_fill()

def neitu():
    turtle.color('#FF9933',"#FFCC33")

    goto(0,-25)
    for _ in range(12):
        turtle.begin_fill()
        turtle.circle(150,60)
        turtle.left(90)
        turtle.circle(150,60)
        turtle.end_fill()

def write():
    goto(-40,10)
    turtle.color("white")
    turtle.write("伍仁月饼祝您中秋快乐",font={"Time","10px","bold"})
    turtle.done()
    img = turtle.getscreen()
    img.getcanvas().postscript(file="duck.eps")
    im = Image.open("./duck.eps")
    im.save("pic.png", "JPEG")


if __name__ == '__main__':
    turtle.speed(10)
    huabian()
    yuan()
    neitu()
    write()
