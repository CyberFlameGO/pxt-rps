def on_gesture_shake():
    global myHand
    myHand = randint(1, 3)
    if myHand == 1:
        rockImage.show_image(0)
    if myHand == 2:
        paperImage.show_image(0)
    if myHand == 3:
        scissorsImage.show_image(0)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

myHand = 0
scissorsImage: Image = None
paperImage: Image = None
rockImage: Image = None
rockImage = images.create_image("""
    . . . . .
    . # # # .
    # # # # #
    # # # # #
    . . . . .
    """)
paperImage = images.icon_image(IconNames.SQUARE)
scissorsImage = images.icon_image(IconNames.SCISSORS)