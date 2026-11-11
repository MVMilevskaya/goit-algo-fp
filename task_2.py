import turtle


def draw_pythagoras_tree(t, length, level):

    if level == 0:
        return

    t.forward(length)

    pos = t.pos()
    heading = t.heading()

    t.left(45)
    draw_pythagoras_tree(t, length * 0.7071, level - 1)

    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

    t.right(45)
    draw_pythagoras_tree(t, length * 0.7071, level - 1)

    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()
    t.backward(length)


def main():
    while True:
        try:
            level = int(input("Введіть рівень рекурсії (наприклад, 1-10): "))
            if level < 1:
                print("Рівень рекурсії має бути більшим за 0.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    screen = turtle.Screen()
    screen.setup(width=900, height=800)
    screen.title(f"Дерево Піфагора (Рівень рекурсії: {level})")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("brown")
    t.pensize(1)

    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()

    initial_length = 120
    draw_pythagoras_tree(t, initial_length, level)

    screen.update()
    print("Малювання завершено! Натисніть на вікно, щоб закрити.")
    screen.exitonclick()


if __name__ == "__main__":
    main()