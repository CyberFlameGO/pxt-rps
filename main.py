def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

rockImage = images.create_image("""
    . . . . .
    . # # # .
    # # # # #
    # # # # #
    . . . . .
    """)
paperImage = images.icon_image(IconNames.SQUARE)
scissorsImage = images.icon_image(IconNames.SCISSORS)