const arr = Object.values(data);
const shape = arr.length;
console.log(arr);
const openSet = [];
const closedSet = [];
let startNode;
const w = 640;
const h = 640;

function Tile(i, j) {
  this.i = i;
  this.j = j;
  this.f = 0;
  this.g = 0;
  this.h = 0;
  this.n = -1;
  this.endPos = -1;

  this.show = function(col) {
    fill(col);
    rect(w / shape * (this.j), h /shape * (this.i), w / shape, h / shape);
    fill(0, 102, 153, 204);
    textSize(32);
    textAlign(CENTER, CENTER);
    if ( this.endPos != -1 && mouseX >= w / shape * (this.j) && mouseX <= w / shape * (this.j) + w / shape &&
            mouseY >= h /shape * (this.i) && mouseY <= h /shape * (this.i) + h / shape) {
      fill(255, 155, 100);
      rect(w / shape * (this.endPos % shape - 1), h /shape * Math.ceil(this.endPos / shape - 1), w / shape, h / shape);
    }
    text(this.n, w / shape * (this.j + .5), h / shape * (this.i + .5));
  }
}

const grid = new Array(shape);
for (let i = 0; i < shape; i++) {
  grid[i] = new Array(shape);
}

for (var i = 0; i < shape; i++) {
  for (var j = 0; j < shape; j++) {
    grid[i][j] = new Tile(i, j);
    grid[i][j].n = arr[i][j];
    if (arr[i][j] == 0) {
      startNode = grid[i][j];
      grid[i][j].endPos = zeroPos();
    }
  }

}

function numbers() {
  // create array from 1 to n^2 - 1.
  const snail = new Array(shape);
  let j = 1;
  for (let i = 0; i < shape; i += 1) {
    snail[i] = new Array(shape).fill(0);
    for (let n = 0; n < shape; n += 1) {
      snail[i][n] = j;
      j += 1;
    }
  }
  snail[shape - 1][shape - 1] = 0;
  return snail;
}

const nb = numbers();

function getSnail() {
  const snail = new Array(shape);
  for (let k = 0; k < shape; k++) {
    snail[k] = new Array(shape);
  }
  return snail;
}

let snail = getSnail();
let end = shape - 1;
let st = 0;
let n = 1;
function recursiveSnail(st, end) {
  console.log("recurse " + end);
  console.log(st);
  if (end === 0) {
    console.log("return");
    return;
  }
  // get first row
  for (let m = st; m <= end; m++) {
    snail[st][m] = n;
    n += 1;
  }
  // get last column
  for (let m = st; m <= end; m++) {
    snail[m][end] = n;
    n += 1;
  }
  // get last row
  for (let m = end - 1; m > st; m--) {
    snail[end][m] = n;
    n += 1;
    console.log("pushed " + nb[shape - 1][m]);
  }
  for (let m = end; m > st; m--) {
    snail[m][st] = n;
    n += 1;
  }
  end -= 1;
  st += 1;
  recursiveSnail(st, end);
/*
  1,2,3
  6,9,8
  7,4,5

  1 2 3
  8 9 4
  7 6 5
*/
}
recursiveSnail(st, end);
console.log("snaiiil");
console.log(snail);

function getEndState() {
  endState = new Array(shape);
  let i = j = 0;
  for (i; i < shape; i++) {
    endState[i] = new Array(shape);
    j = 0;
    while (j < shape && startNode.endPos > i * shape + j + 1) {
      endState[i][j] = new Tile(i, j);
      endState[i][j].n = i * shape + j + 1;
      j++;
    }
    if (startNode.endPos == i * shape + j + 1) {
      endState[i][j] = new Tile(i, j);
      endState[i][j].n = 0;
      j++;
    }
    while (j < shape && startNode.endPos < i * shape + j + 1) {
      endState[i][j] = new Tile(i, j);
      endState[i][j].n = i * shape + j;
      j++;
    }
  }
  j++;
  return endState;
}

openSet.push(startNode);
//startNode.f = heuristics(startNode)

console.log("startNode: " + startNode.n);

console.log(grid);

function setup() {
  createCanvas(640, 640);
}

function zeroPos(){
  if (shape % 2 == 0) {
    // even number
    return shape * shape / 2 + shape / 2;
  } else {
    // odd number
    return (shape * shape + 1) / 2;
  }
}
endstate = getEndState();

function draw() {


  background(5, 55, 155);
  for (var i = 0; i < shape; i++) {
    for (var j = 0; j < shape; j++) {
      grid[i][j].show(color(255));
    }
  }
  for (var i = 0; i < shape; i++) {
    for (var j = 0; j < shape; j++) {
      snail[i][j].show(color(255));
    }
  }
/*     for (var i = 0; i < openSet.length; i++) {
        openSet[i].show(color(55, 255, 155));
    } */
}