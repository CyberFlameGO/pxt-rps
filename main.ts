input.onGesture(Gesture.Shake, function () {
    myHand = randint(1, 3)
    if (myHand == 1) {
        rockImage.showImage(0)
    }
    if (myHand == 2) {
        paperImage.showImage(0)
    }
    if (myHand == 3) {
        scissorsImage.showImage(0)
    }
})
let myHand = 0
let scissorsImage: Image = null
let paperImage: Image = null
let rockImage: Image = null
rockImage = images.createImage(`
    . . . . .
    . # # # .
    # # # # #
    # # # # #
    . . . . .
    `)
paperImage = images.iconImage(IconNames.Square)
scissorsImage = images.iconImage(IconNames.Scissors)
