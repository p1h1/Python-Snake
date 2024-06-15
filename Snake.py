import turtle
import time
import random
import tkinter as tk

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Main game loop
def main_game():
    global score
    global segments
    global head

    while True:
        wn.update()

        # Check for a collision with the border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset score
            score = 0
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

            # Display game over message
            game_over = turtle.Turtle()
            game_over.speed(0)
            game_over.color("red")
            game_over.penup()
            game_over.hideturtle()
            game_over.goto(0, 0)
            game_over.write("Game Over", align="center", font=("Courier", 36, "normal"))

            # Create play again button using tkinter
            def play_again():
                # Clear game over message
                game_over.clear()

                # Reset head position and direction
                head.goto(0, 0)
                head.direction = "stop"

                # Clear segments
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()

                # Reset score
                score = 0
                score_display.clear()
                score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

                # Restart main game loop
                main_game()

            # Create a tkinter button
            root = tk.Toplevel()
            root.geometry("+{}+{}".format(wn.window_width() // 2 - 150, wn.window_height() // 2 - 75))
            button = tk.Button(root, text="Play Again", command=play_again)
            button.pack()

            # Run tkinter main loop
            root.mainloop()

            break

        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Increase score
            score += 1
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for head collision with body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()

                # Reset score
                score = 0
                score_display.clear()
                score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

                # Display game over message
                game_over = turtle.Turtle()
                game_over.speed(0)
                game_over.color("red")
                game_over.penup()
                game_over.hideturtle()
                game_over.goto(0, 0)
                game_over.write("Game Over", align="center", font=("Courier", 36, "normal"))

                # Create play again button using tkinter
                def play_again():
                    # Clear game over message
                    game_over.clear()

                    # Reset head position and direction
                    head.goto(0, 0)
                    head.direction = "stop"

                    # Clear segments
                    for segment in segments:
                        segment.goto(1000, 1000)
                    segments.clear()

                    # Reset score
                    score = 0
                    score_display.clear()
                    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

                    # Restart main game loop
                    main_game()

                # Create a tkinter button
                root = tk.Toplevel()
                root.geometry("+{}+{}".format(wn.window_width() // 2 - 150, wn.window_height() // 2 - 75))
                button = tk.Button(root, text="Play Again", command=play_again)
                button.pack()

                # Run tkinter main loop
                root.mainloop()

                break

        time.sleep(0.1)

# Start the main game loop
main_game()

# Keep the window open until it is closed by the user
wn.mainloop()
