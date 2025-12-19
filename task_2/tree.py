import turtle

def draw_tree(branch_length, level):
    if level == 0:
        return
    
    turtle.forward(branch_length)
    
    position = turtle.position()
    heading = turtle.heading()
    angle = 30
    
    turtle.left(angle)
    draw_tree(branch_length * 0.7, level - 1)
    
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()
    
    turtle.right(angle)
    draw_tree(branch_length * 0.7, level - 1)
    
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()

def main():
    level = int(input("Enter the level: "))
    
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("brown")
    
    draw_tree(100, level)
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()