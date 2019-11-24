import turtle

def main():
    turtle.hideturtle()
    turtle.penup()#画笔关闭
    turtle.goto(-270, 180)
    turtle.pendown()#画笔开启

    turtle.pensize(4)
    turtle.pencolor('red')

    #绘制弓
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(50)

    #绘制长
    turtle.penup()
    turtle.goto(-40,180)
    turtle.pendown()

    turtle.left(105)
    turtle.forward(180)

    turtle.penup()
    turtle.goto(-150,22)
    turtle.pendown()
    turtle.left(120)
    turtle.forward(200)

    turtle.penup()
    turtle.goto(-130,180)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(300)
    turtle.left(135)
    turtle.forward(50)

    turtle.penup()
    turtle.goto(-130,22)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(180)

    #维修，加点曲线
    turtle.left(10)
    turtle.forward(10)
    turtle.left(10)
    turtle.forward(10)
    turtle.left(10)
    turtle.forward(30)
    turtle.penup()

    turtle.mainloop()

if __name__ == '__main__':
    main()