#git_shape_py

import turtle

# Setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
s.colormode(255) 
t.speed(0)
t.hideturtle()

colors = [(255, 0, 0), (0, 0, 255)]  # red, blue


t.penup()
t.goto(0, 150)
t.color("white")
t.write("Choose a shape by entering a number (1-10):", align="center", font=("Arial", 16, "normal"))
t.goto(0, 120)
t.write("1. Triangle   2. Square   3. Pentagon   4. Hexagon   5. Heptagon", align="center", font=("Arial", 14, "normal"))
t.goto(0, 90)
t.write("6. Octagon   7. Nonagon   8. Decagon   9. 5-Point Star   10. 7-Point Star", align="center", font=("Arial", 14, "normal"))


choice = s.textinput("Shape Choice", "Enter your choice (1-10):")


t.clear()
t.penup()
t.goto(0, 0)
t.pendown()
t.showturtle()

# Use if-elif-else to assign angle
if choice == "1":
    angle = 120         # Triangle
elif choice == "2":
    angle = 90          # Square
elif choice == "3":
    angle = 72          # Pentagon
elif choice == "4":
    angle = 60          # Hexagon
elif choice == "5":
    angle = 360 / 7     # Heptagon ≈ 51.43
elif choice == "6":
    angle = 45          # Octagon
elif choice == "7":
    angle = 40          # Nonagon
elif choice == "8":
    angle = 36          # Decagon
elif choice == "9":
    angle = 144         # 5-Point Star
elif choice == "10":
    angle = 154.29      # 7-Point Star
else:
    angle = 100         # Default if invalid input


for i in range(120):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 4)
    t.right(angle)

t.hideturtle()
turtle.done()





