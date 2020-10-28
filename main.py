def pickShape():
    global myHand
    myHand = randint(1, 3)
    if myHand == rockIndex:
        rockImage.show_image(0)
    if myHand == paperIndex:
        paperImage.show_image(0)
    if myHand == scissorsIndex:
        scissorsImage.show_image(0)

def on_gesture_shake():
    pickShape()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

myHand = 0
scissorsImage: Image = None
paperImage: Image = None
rockImage: Image = None
scissorsIndex = 0
paperIndex = 0
rockIndex = 0
rockIndex = 1
paperIndex = 2
scissorsIndex = 3
rockImage = images.create_image("""
    . . . . .
    . # # # .
    # # # # #
    # # # # #
    . . . . .
    """)
paperImage = images.icon_image(IconNames.SQUARE)
scissorsImage = images.icon_image(IconNames.SCISSORS)