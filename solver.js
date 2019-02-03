const arr = Object.values(data);
const shape = arr.length;
const openSet = [];
const closedSet = [];
let startNode;
const w = 640;
const h = 640;

// Tile constructor function.
function Tile(i, j) {
  this.i = i;
  this.j = j;
  this.f = 0;
  this.g = 0;
  this.h = 0;
  this.n = -1;
  this.endPos = -1;

  this.show = function show(col) {
    fill(col);
    rect(w / shape * (this.j), h / shape * (this.i), w / shape, h / shape);
    fill(0, 102, 153, 204);
    textSize(32);
    textAlign(CENTER, CENTER);
    if (this.endPos !== -1 && mouseX >= w / shape * (this.j) && mouseX <= w / shape * (this.j) + w / shape
            && mouseY >= h / shape * (this.i) && mouseY <= h / shape * (this.i) + h / shape) {
      fill(255, 155, 100);
      rect(w / shape * (this.endPos % shape - 1), h / shape * Math.ceil(this.endPos / shape - 1), w / shape, h / shape);
    }
    text(this.n, w / shape * (this.j + 0.5), h / shape * (this.i + 0.5));
  };
}

const grid = new Array(shape);
for (let i = 0; i < shape; i++) {
  grid[i] = new Array(shape);
}

// get position of zero in the final grid.
function zeroPos() {
  if (shape % 2 === 0) {
    // even number
    return shape * shape / 2 + shape / 2;
  }
  // odd number
  return (shape * shape + 1) / 2;
}

function createGrid() {
  for (let i = 0; i < shape; i++) {
    for (let j = 0; j < shape; j++) {
      grid[i][j] = new Tile(i, j);
      grid[i][j].n = arr[i][j];
      if (arr[i][j] === 0) {
        startNode = grid[i][j];
        grid[i][j].endPos = zeroPos();
      }
    }
  }
}

createGrid();

function getSnail() {
  const snail = new Array(shape);
  for (let k = 0; k < shape; k++) {
    snail[k] = new Array(shape);
  }
  return snail;
}

const snail = getSnail();
let n = 1;

function recursiveSnail(start, end) {
  if (end === 0) {
    return;
  }
  // get first row
  for (let m = start; m < end; m++) {
    snail[start][m] = new Tile(start, m);
    snail[start][m].n = n;
    n += 1;
  }
  // get last column
  for (let m = start; m <= end; m++) {
    snail[m][end] = new Tile(m, end);
    snail[m][end].n = n;
    n += 1;
  }
  // get last row
  for (let m = end - 1; m > start; m--) {
    snail[end][m] = new Tile(end, m);
    snail[end][m].n = n;
    n += 1;
  }
  // get first column
  for (let m = end; m > start; m--) {
    snail[m][start] = new Tile(m, start);
    snail[m][start].n = n;
    n += 1;
  }
  recursiveSnail(start + 1, end - 1);
}
recursiveSnail(0, shape - 1);
snail[Math.ceil(zeroPos() / shape) - 1][(zeroPos() % shape) - 1].n = 0;
openSet.push(startNode);
// startNode.f = heuristics(startNode)

console.log('startNode: ' + startNode.n);

console.log(grid);

function setup() {
  createCanvas(640, 640);
}

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
