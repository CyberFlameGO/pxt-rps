function pickShape () {
    myHand = randint(1, 3)
    if (myHand == rockIndex) {
        rockImage.showImage(0)
    }
    if (myHand == paperIndex) {
        paperImage.showImage(0)
    }
    if (myHand == scissorsIndex) {
        scissorsImage.showImage(0)
    }
}
input.onGesture(Gesture.Shake, function () {
    pickShape()
})
let myHand = 0
let scissorsImage: Image = null
let paperImage: Image = null
let rockImage: Image = null
let scissorsIndex = 0
let paperIndex = 0
let rockIndex = 0
rockIndex = 1
paperIndex = 2
scissorsIndex = 3
rockImage = images.createImage(`
    . . . . .
    . # # # .
    # # # # #
    # # # # #
    . . . . .
    `)
paperImage = images.iconImage(IconNames.Square)
scissorsImage = images.iconImage(IconNames.Scissors)
