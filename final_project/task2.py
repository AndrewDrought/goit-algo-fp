import turtle


def draw_tree(branch_length, t, angle):
    if branch_length < 5:
        return
    else:
        t.forward(branch_length)
        t.right(angle)
        draw_tree(branch_length - 15, t, angle)
        t.left(angle * 2)
        draw_tree(branch_length - 15, t, angle)
        t.right(angle)
        t.backward(branch_length)


def main():
    iterations = int(input("Введіть рівень рекурсії: "))
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("red")
    draw_tree(iterations, t, 45)
    window.exitonclick()


if __name__ == "__main__":
    main()
