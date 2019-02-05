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
  this.endPos = [];

  // method for drawing a tile in the browser
  this.show = function show(col, pos) {
    fill(col);
    rect(w / shape * (this.j), h / shape * (this.i), w / shape, h / shape);
    fill(255, 255, 255, 100);
    if (pos === 1) {
      textSize(28);
      textAlign(CENTER, TOP);
    }
    else {
      textSize(16);
      textAlign(CENTER, BOTTOM);
    }
    // highlight the final position for each tile on hover
    if (this.endPos && mouseX >= w / shape * (this.j) && mouseX <= w / shape * (this.j) + w / shape
            && mouseY >= h / shape * (this.i) && mouseY <= h / shape * (this.i) + h / shape) {
      fill(255, 255, 100, 100);
      rect(w / shape * (this.endPos[1]), h / shape * (this.endPos[0]), (w / shape), (h / shape));
    }
    text(this.n, w / shape * (this.j + 0.5), h / shape * (this.i + 0.5));
  };
}

const grid = new Array(shape);
for (let i = 0; i < shape; i++) {
  grid[i] = new Array(shape);
}

// get position of zero in the final grid.
function zeroPos(size) {
  if (size % 2 === 0) {
    // even number
    return [size / 2, size / 2];
  }
  // odd number
  return [(size - 1) / 2, (size - 1) / 2];
}

// The "snail" is the final layout of tiles, as specified in the subject.
function getSnail() {
  const snail = new Array(shape);
  for (let k = 0; k < shape; k++) {
    snail[k] = new Array(shape);
  }
  return snail;
}

const snail = getSnail();
let n = 1;

// Fill the snail with the right numbers.
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
snail[zeroPos(shape)[0]][zeroPos(shape)[1]].n = 0;

function findNumber(grid, number) {
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j].n === number) {
        return [i, j];
      }
    }
  }
  return null;
}

function createGrid() {
  for (let i = 0; i < shape; i++) {
    for (let j = 0; j < shape; j++) {
      grid[i][j] = new Tile(i, j);
      grid[i][j].n = arr[i][j];
      grid[i][j].endPos = findNumber(snail, grid[i][j].n);
      if (arr[i][j] === 0) {
        startNode = grid[i][j];
        grid[i][j].endPos = findNumber(snail, 0);
      }
    }
  }
}

// Get the tiles surrounding the "0" tile.
function getSurrounding() {
  surrounding = [];
  zero = findNumber(grid, 0);
  if (zero[0] > 0) {
    surrounding.push(grid[zero[0] - 1][zero[1]])
  }
  if (zero[1] > 0) {
    surrounding.push(grid[zero[0]][zero[1] - 1])
  }
  if (zero[0] < shape - 1)
  {
    surrounding.push(grid[zero[0] + 1][zero[1]])
  }
  if (zero[1] < shape - 1)
  {
    surrounding.push(grid[zero[0]][zero[1] + 1])
  }
  return (surrounding);
}

// TODO Function to move a tile
function move(arr, from, to) {
  tmp = arr[from[0]][from[1]];
}

createGrid();

openSet.push(startNode);
// startNode.f = heuristics(startNode)

around = getSurrounding();
// calculate Manhattan distance before change
function mhDistance() {
  let sum = 0;
  for (let i = 0; i < shape; i++) {
    for (let j = 0; j < shape; j++) {
      if (grid[i][j].n === 0) {
        continue;
      }
      sum += Math.abs(i - grid[i][j].endPos[0]) + Math.abs(j - grid[i][j].endPos[1]);
      grid[i][j].f = sum;
    }
  }
  return sum;
}


/*
console.log(around);
console.log("Manhattan distance: " + mhDistance());
let newGrid = grid.slice();
let tmp = newGrid[0][0];
newGrid[0][0] = newGrid[0][1];
newGrid[0][1] = tmp;
console.log(newGrid);
*/


// p5js setup
function setup() {
  createCanvas(640, 640);
}

// p5js draw loop
function draw() {

  if (openSet.length > 0) {
    // we can keep going
    for (let i = 0; i < openSet.length; i++)
    {
      
    }
  } else {
    // no solution
  }

  background(0, 0, 0);
  for (let i = 0; i < shape; i++) {
    for (let j = 0; j < shape; j++) {
      grid[i][j].show(color(0, 0, 255, 100), 1);
    }
  }
  for (var i = 0; i < shape; i++) {
    for (var j = 0; j < shape; j++) {
      snail[i][j].show(color(255, 255, 255, 100), 0);
    }
  }
    for (var i = 0; i < openSet.length; i++) {
        openSet[i].show(color(55, 255, 155, 50), 1);
    }
}
