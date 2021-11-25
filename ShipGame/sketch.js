var PLAY = 1;
var END = 0;
var gameState = PLAY;

var skybg, waterbg, startd, soundd, shipimg, helicopterimg, bombimg, gameOverimg;
var helicopterGroup, bombGroup;
var score = 0;

function preload() {
  skybg = loadImage("skybg.jpg");
  waterbg = loadImage("waterbg.png");
  shipimg = loadImage("ship.png");
  helicopterimg = loadImage("helicopter.png");
  bombimg = loadImage("bomb.png");
  gameOverimg = loadImage("gameOver.png");
  soundd = loadSound('mixkit-explosion-in-battle-2809.wav');
  startd = loadSound('happy-media-music-opener.mp3');
}

function setup() {
  createCanvas(800, 450);
  water = createSprite(400, 320);
  water.addImage("water", waterbg);
  water.velocityX = -5;
  //creating water ground
  helicopter = createSprite(800, 80, 200, 50);
  helicopter.addImage("helicopter", helicopterimg);
  helicopter.setVelocity(-5, 0);
  helicopter.scale = 0.5;

  ship = createSprite(30, 280);
  ship.addImage("ship", shipimg);
  ship.scale = 0.25;
  //creating ship

  helicopterGroup = new Group();
  //creating helicopter group

  bombGroup = new Group();
  //creating bomb group

  //ship.debug = "true";

}


function draw() {

  background(skybg);
  fill("yellow");
  textSize(15);
  text("SURVIVAL TIME: " + score, 600, 30);

  if (keyDown("RIGHT_ARROW")) {
    ship.x = ship.x + 3;
  }

  if (keyDown("LEFT_ARROW")) {
    ship.x = ship.x - 3;
  }

  if (bombGroup.isTouching(ship)) {
    soundd.play();
    startd.play();
    gameState = END;
  }



  //gameState play
  if (gameState === PLAY) {
    //increase score
    score = score + Math.round(frameCount / 300);
    spawnBomb();
    spawnHelicopter();
    //Call user defined function

  }

  //gameState end
  else if (gameState === END) {
    ship.addImage("ship", gameOverimg);
    water.velocityX = 0;
    ship.x = 400;
    ship.y = 250;
    ship.scale = 0.6;
    //water velocity becomes zero

    helicopterGroup.destroyEach();
    //destroy Helicopter group

    bombGroup.destroyEach();
    //destroy bomb group
  }

  //for infinite background 
  if (water.position.x < 300) {
    water.position.x = 400;
  }

  drawSprites();
}


function spawnHelicopter() {
  if (frameCount % 200 === 0) {
    helicopter = createSprite(800, 80, 200, 50);
    helicopter.addImage("helicopter", helicopterimg);
    helicopter.setVelocity(-5, 0);

    helicopter.scale = 0.6;

    helicopterGroup.add(helicopter);
  }
}

function spawnBomb() {
  if (frameCount % 50 === 0) {
    bomb = createSprite(Math.round(random(helicopter.x - 10, helicopter.x + 10)), 80, 5, 5);
    bomb.addImage("bomb", bombimg);
    bomb.setVelocity(0, 5);
    bomb.scale = 0.25;
    bombGroup.add(bomb);
  }
  // create bombs at random position
  //use Math.random
}




