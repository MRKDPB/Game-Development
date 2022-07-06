var wheel1, wheel2, wheel3, wheel4, wheelmove, wheel;

function preload() {

    wheelmove = loadAnimation("wheel4.png", "wheel3.png", "wheel2.png", "wheel1.png");

}

function setup() {
    createCanvas(1380, 400);
    wheel = createSprite(100, 100, 30, 30);
    wheel.addAnimation('moving', wheelmove);
    wheel.addSpeed(5, 0);
    wheel.scale = 0.6;


}

function draw() {
    background("white");

    drawSprites();
    if (wheel.position.x > 1350) {
        wheel.position.x = 0;
    }
}
