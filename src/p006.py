### Escaping the maze ###


def turn_right():
    for _ in range(3):
        turn_left()

not_lost = 4
while not at_goal():
    if not not_lost:
        move()
        not_lost = 4
    elif right_is_clear():
        turn_right()
        move()
        not_lost -= 1
        print(not_lost)
    elif front_is_clear():
        move()
        not_lost = 4
    else:
        turn_left()
        not_lost = 4