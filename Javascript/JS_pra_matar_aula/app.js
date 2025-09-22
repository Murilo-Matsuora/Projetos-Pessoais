const trgt = document.getElementById("target");
const restartBtn = document.getElementById("restartButton");
const minSpeed = 3;
const maxSpeed = 8;
let mouseX = 0;
let mouseY = 0;
let targetX = parseInt(trgt.style.left);
let targetY = parseInt(trgt.style.top);
const slow = 2000;
let alive = true;
let gameHasBegun = false;
let bestTime = 0;

trgt.addEventListener("click", () => {
  console.log("oi");
  document.getElementById("deathScreen").style.display = "none";
  trgt.textContent = "O";
  // trgt.style.backgroundColor = "aqua";
  // targetX = 0;
  // targetY = 0;
  // trgt.style.left = "50%";
  // trgt.style.top = "50%";

  
  
});

trgt.addEventListener("mouseover", () => {
  console.log("perdeu");
  stopTimer();
  alive = false;
  gameHasBegun = false;
  trgt.textContent = "X";
  // trgt.style.backgroundColor = "red";
  document.getElementById("timerDeath").textContent = document.getElementById("timer").textContent;
  document.getElementById("deathScreen").style.display = "block";
});

window.addEventListener("mousemove", (event) => {
  mouseX = event.clientX;
  mouseY = event.clientY;
  if(alive && !gameHasBegun){
    resetTimer();
    startTimer();
    trgt.src = "./pacman.gif"
    requestAnimationFrame(update);
    console.log("gameHasBegun");
    gameHasBegun = true;
  
  }
  
  
});

restartBtn.addEventListener("click", () => {
  console.log("restart");
  stopTimer();
  alive = true;
  gameHasBegun = false;
  trgt.src = "./pacman_idle.gif"
  trgt.textContent = "O";
  // trgt.style.backgroundColor = "aqua";
  document.getElementById("deathScreen").style.display = "none";

  trgt.style.transform = "rotate(0deg)";
  
  trgt.style.left = "50px";
  trgt.style.top = "50px";

  targetX = parseInt(trgt.style.left);
  targetY = parseInt(trgt.style.top);

});

window.onload = () => {
  trgt = document.getElementById("target");
  trgt.style.left = "50px";
  trgt.style.top = "50px";
  targetX = parseInt(trgt.style.left);
  targetY = parseInt(trgt.style.top);
};


function update() {
  if (!alive) {
    return; // alive the animation if the target is hovered
  }
  console.log(trgt.style.left);
  let diffX =
    (Math.pow(mouseX - targetX, 2) * Math.sign(mouseX - targetX)) / slow;
  let diffY =
    (Math.pow(mouseY - targetY, 2) * Math.sign(mouseY - targetY)) / slow;

    
  const angle = Math.atan2(diffY, diffX);
  trgt.style.transform = `rotate(${angle}rad)`;

  if (
    diffX !== 0 &&
    diffY !== 0 &&
    Math.pow(Math.abs(diffX), 2) + Math.pow(Math.abs(diffY), 2) < minSpeed
  ) {
    diffX =
      (minSpeed * diffX) / Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
    diffY =
      (minSpeed * diffY) / Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
  }
  if (
    diffX !== 0 &&
    diffY !== 0 &&
    Math.pow(Math.abs(diffX), 2) + Math.pow(Math.abs(diffY), 2) > maxSpeed
  ) {
    diffX =
      (maxSpeed * diffX) / Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
    diffY =
      (maxSpeed * diffY) / Math.sqrt(Math.pow(diffX, 2) + Math.pow(diffY, 2));
  }

  

  targetX += diffX;
  targetY += diffY;

  trgt.style.left = targetX + "px";
  trgt.style.top = targetY + "px";

  requestAnimationFrame(update);
}

requestAnimationFrame(update);


let startTime,
  elapsed = 0,
  timerInterval;

function timeToString(time) {
  // const hrs = Math.floor(time / 3600000);
  const mins = Math.floor((time % 3600000) / 60000);
  const secs = Math.floor((time % 60000) / 1000);
  const ms = Math.floor((time % 1000) / 10);
  return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}.${ms.toString().padStart(2, "0")}`;
}

function startTimer() {
  startTime = Date.now() - elapsed;
  timerInterval = setInterval(() => {
    elapsed = Date.now() - startTime;
    document.getElementById("timer").textContent = timeToString(elapsed);
  }, 10); // update every second
}

function stopTimer() {
  clearInterval(timerInterval);
}

function resetTimer() {
  clearInterval(timerInterval);
  if (elapsed > bestTime) {
    bestTime = elapsed;
    document.getElementById("personalBest").textContent = "PB: " + timeToString(bestTime);
  }
  elapsed = 0;
  document.getElementById("timer").textContent = "00:00.00";
}

window.onload = () => {
  requestAnimationFrame(update);
};
