const input = Object.values(data);
const shape = input.length;
let openSet = [];
let closedSet = [];
const w = 640;
const h = 640;

// Grid constructor function
function Grid(size) {
  this.f = size * size;
  this.g = 0;
  this.h = 0;
  this.arr = new Array(size);
  for (let i = 0; i < size; i++) {
    this.arr[i] = new Array(size);
  }

  this.show = function show() {
    rect(0, 0, w, h);
    for (let i = 0; i < shape; i++) {
      for (let j = 0; j < shape; j++) {
        fill(255, 255, 0);
        const current = this.arr[i][j];
        if (current.n === 0) {
          fill(255, 255, 155);
        }
        rect(w / shape * current.j, h / shape * current.i, h / shape, w / shape);
        fill(0);
        textSize(28);
        textAlign(CENTER, CENTER);
        const offset = w / shape * 0.5;
        text(current.n, w / shape * current.j + offset, h / shape * current.i + offset);
      }  
    }
  }
}

// Tile constructor function.
function Tile(i, j) {
  this.i = i;
  this.j = j;
  this.n = -1;
  this.endPos = [];
}

// snail is the final grid layout.
const snail = new Grid(shape);

// get position of zero in the final grid.
function zeroPos(size) {
  if (size % 2 === 0) {
    // even number
    return [size / 2, size / 2];
  }
  // odd number
  return [(size - 1) / 2, (size - 1) / 2];
}

let n = 1;

// Fill the snail with the right numbers.
function recursiveSnail(start, end) {
  if (end === 0) {
    return;
  }
  // get first row
  for (let m = start; m < end; m++) {
    snail.arr[start][m] = new Tile(start, m);
    snail.arr[start][m].n = n;
    n += 1;
  }
  // get last column
  for (let m = start; m <= end; m++) {
    snail.arr[m][end] = new Tile(m, end);
    snail.arr[m][end].n = n;
    n += 1;
  }
  // get last row
  for (let m = end - 1; m > start; m--) {
    snail.arr[end][m] = new Tile(end, m);
    snail.arr[end][m].n = n;
    n += 1;
  }
  // get first column
  for (let m = end; m > start; m--) {
    snail.arr[m][start] = new Tile(m, start);
    snail.arr[m][start].n = n;
    n += 1;
  }
  recursiveSnail(start + 1, end - 1);
}
recursiveSnail(0, shape - 1);
snail.arr[zeroPos(shape)[0]][zeroPos(shape)[1]].n = 0;

function findNumber(currentGrid, number) {
  for (let i = 0; i < currentGrid.arr.length; i++) {
    for (let j = 0; j < currentGrid.arr[i].length; j++) {
      if (currentGrid.arr[i][j].n === number) {
        return [i, j];
      }
    }
  }
  return null;
}

function createGrid() {
  let initialGrid = new Grid(shape);
  for (let i = 0; i < shape; i++) {
    for (let j = 0; j < shape; j++) {
      initialGrid.arr[i][j] = new Tile(i, j);
      initialGrid.arr[i][j].n = input[i][j];
      initialGrid.arr[i][j].endPos = findNumber(snail, initialGrid.arr[i][j].n);
    }
  }
  return initialGrid;
}

// Get the tiles surrounding the "0" tile.
function getNeighbors(currentGrid) {
  surrounding = [];
  zero = findNumber(currentGrid, 0);
  if (zero[0] > 0) {
    surrounding.push(currentGrid.arr[zero[0] - 1][zero[1]])
  }
  if (zero[1] > 0) {
    surrounding.push(currentGrid.arr[zero[0]][zero[1] - 1])
  }
  if (zero[0] < shape - 1)
  {
    surrounding.push(currentGrid.arr[zero[0] + 1][zero[1]])
  }
  if (zero[1] < shape - 1)
  {
    surrounding.push(currentGrid.arr[zero[0]][zero[1] + 1])
  }
  return (surrounding);
}

initialGrid = createGrid();
openSet.push(initialGrid);

// calculate Manhattan distance before change
function mhDistance(set) {
  for (let m = 0; m < set.length; m++) {
    let sum = 0;
    for (let i = 0; i < shape; i++) {
      for (let j = 0; j < shape; j++) {
        sum += Math.abs(i - set[m].arr[i][j].endPos[0]) + Math.abs(j - set[m].arr[i][j].endPos[1]);
        
      }
    }
    set[m].h = sum;
  }
}

// duplicate grid, move tile and return new grid
function moveTile(currentGrid, pos_from, pos_to) {
  let newGrid = new Grid(shape);
  newGrid.g = currentGrid.g + 1;
  for (let i = 0; i < currentGrid.arr.length; i++) {
    newGrid.arr[i] = new Array(shape);
    for (let j = 0; j < currentGrid.arr[i].length; j++) {
      newGrid.arr[i][j] = new Tile(i, j);
      newGrid.arr[i][j].n = currentGrid.arr[i][j].n;
      newGrid.arr[i][j].endPos = currentGrid.arr[i][j].endPos;
    }
  }
  let tmp = new Tile(pos_to[0], pos_to[1]);
  tmp.n = currentGrid.arr[pos_from[0]][pos_from[1]].n;
  tmp.endPos = currentGrid.arr[pos_from[0]][pos_from[1]].endPos;
  let tmp2 = new Tile(pos_from[0], pos_from[1]);
  tmp2.n = currentGrid.arr[pos_to[0]][pos_to[1]].n;
  tmp2.endPos = currentGrid.arr[pos_to[0]][pos_to[1]].endPos;

  newGrid.arr[pos_from[0]][pos_from[1]] = tmp2;
  newGrid.arr[pos_to[0]][pos_to[1]] = tmp;

  return newGrid;
}

// get lowest f-score for an array of grids
function lowestF(set) {
  let lowest = set[0];
  for (let i = 0; i < set.length; i++) {
    set[i].f = set[i].h + set[i].g;
    if (set[i].f < lowest.f) {
      lowest = set[i];
    }
  }
  return lowest;
}

// Check if the current grid is the goal
function goal(currentGrid) {
  for (let i = 0; i < shape; i++) {
    for (let j = 0; j < shape; j++) {
      if (currentGrid.arr[i][j].n != snail.arr[i][j].n) {
        return 0;
      }
    }
  }
  return 1;
}

function getIndex(elem, set) {
  for (let i = 0; i < set.length; i++) {
    if (isEqual(set[i], elem) === 1) {
      return i;
    }
  }
  return -1;
}

// Check if two grids are equal
function isEqual(grid1, grid2) {
  if (grid1.arr.length !== grid2.arr.length) {
    return 0;
  }
  for (let i = 0; i < grid1.arr.length; i++) {
    for (let j = 0; j < grid1.arr[i].length; j++) {
      if (grid1.arr[i][j].n !== grid2.arr[i][j].n) {
        return 0;
      }
    }
  }
  return 1;
}


// p5js setup
function setup() {
  createCanvas(640, 640);
  frameRate(30);
}
let current = openSet[0];

// p5js draw loop
function draw() {
  if (openSet.length > 0) {
    // we can keep going
    mhDistance(openSet);
    current = lowestF(openSet);
    console.log("current ", JSON.parse(JSON.stringify(current)));
    if (goal(current) === 1) {
      current.show();
      console.log("finished");
      return;
    }
    const ind = getIndex(current, openSet);
    if (ind >= 0) {
      openSet.splice(getIndex, 1);
    }
    closedSet.push(current);
    neighbors = getNeighbors(current);
    newGrids = [];
    for (let i = 0; i < neighbors.length; i++) {
      newGrids.push(moveTile(current, [neighbors[i].i, neighbors[i].j], findNumber(current, 0)));
    }
    console.log("newGrids ", JSON.parse(JSON.stringify(newGrids)));
    for (let i = 0; i < newGrids.length; i++) {
      if (getIndex(newGrids[i], closedSet) >= 0) {
        continue ;
      }
      if (getIndex(newGrids[i], openSet) < 0) {
        openSet.push(newGrids[i]);
      }
    }
    console.log("open set: ", openSet.length);
    current.show();
  } else {
    console.log("no solution")
    return ;
    // no solution*/
  }
}

function mousePressed() {
  redraw();
}