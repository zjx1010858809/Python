import turtle
import time

#签名
def showname():
    turtle.pu()
    turtle.goto(-100,-200)
    turtle.color('red')
    turtle.write('张家祥',font=('Arial',40,'normal'))
#矩形
def rectangle():
    turtle.pd()
    turtle.right(180)
    turtle.begin_fill()
    for i in range(2):
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(400)
    turtle.end_fill()
    turtle.pu()

#五角星
def five_star(size,angle,x,y,):
    turtle.goto(x, y)
    turtle.pd()
    turtle.right(angle)
    turtle.fillcolor('yellow')
    turtle.color('yellow')
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
    turtle.pu()

#主程序
def main():
    turtle.fillcolor('red')
    turtle.color('red')
    turtle.pensize(2)

    turtle.pu()
    turtle.goto(-200,100)


    #画矩形
    rectangle()

    #画大五角星
    turtle.home()
    five_star(80,0,-180,50)

    #画小五角星
    angles,x_positions,y_positions = [30,10,-10,-30],[-60,-40,-40,-60],[80,50,20,-10]
    for angle,x_position,y_position in zip(angles,x_positions,y_positions):
        turtle.home()
        five_star(20,angle,x_position,y_position)


    #签名
    showname()

    #隐藏小乌龟
    turtle.ht()
    #显示窗口
    turtle.mainloop()



if __name__=='__main__':
    main()