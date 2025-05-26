let board = [];
let visited = [];
let n = 8;
let delay = 300;
let running = false;
let paused = false;
let pathPositions = [];

const dx = [2, 1, -1, -2, -2, -1, 1, 2];
const dy = [1, 2, 2, 1, -1, -2, -2, -1];

const boardContainer = document.getElementById('board');
const boardCountContainer = document.getElementById('boardCount');
const positionsIndexContainer = document.getElementById('positionsIndex');

const startBtn = document.getElementById('start');
const pauseBtn = document.getElementById('pause');

startBtn.addEventListener('click', () => {
  if (running) return;
  n = parseInt(document.getElementById('size').value);
  if (n < 5 || n > 10) return;
  initBoards();
  running = true;
  paused = false;
  pathPositions = [];
  knightTour(0, 0, 1);
});

pauseBtn.addEventListener('click', () => {
  paused = !paused;
  pauseBtn.textContent = paused ? 'Continuar' : 'Pausar';
});

function initBoards() {
  // Main board
  boardContainer.innerHTML = '';
  boardContainer.style.gridTemplateColumns = `repeat(${n}, 45px)`;
  // Count board
  boardCountContainer.innerHTML = '';
  boardCountContainer.style.gridTemplateColumns = `repeat(${n}, 45px)`;

  board = Array.from({ length: n }, () => Array(n).fill(0));
  visited = Array.from({ length: n }, () => Array(n).fill(false));

  for (let i = 0; i < n * n; i++) {
    const cell = document.createElement('div');
    cell.className = 'cell';
    boardContainer.appendChild(cell);
  }

  for (let i = 0; i < n * n; i++) {
    const cell = document.createElement('div');
    cell.className = 'cell';
    boardCountContainer.appendChild(cell);
  }

  positionsIndexContainer.innerHTML = '';
}

function delayMs(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function knightTour(x, y, moveCount) {
  if (paused) {
    await waitUntilResumed();
  }

  board[x][y] = moveCount;
  visited[x][y] = true;
  pathPositions.push({ x, y });

  updateBoards();
  updatePositionsIndex();

  await delayMs(delay);

  if (moveCount === n * n) {
    running = false;
    return true;
  }

  for (let i = 0; i < 8; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (isSafe(nx, ny)) {
      const success = await knightTour(nx, ny, moveCount + 1);
      if (success) return true;
    }
  }

  // Backtrack
  board[x][y] = 0;
  visited[x][y] = false;
  pathPositions.pop();
  updateBoards();
  updatePositionsIndex();
  await delayMs(delay);
  return false;
}

function isSafe(x, y) {
  return x >= 0 && y >= 0 && x < n && y < n && !visited[x][y];
}

function updateBoards() {
  const mainCells = boardContainer.querySelectorAll('.cell');
  mainCells.forEach((cell, idx) => {
    const row = Math.floor(idx / n);
    const col = idx % n;
    cell.textContent = board[row][col] ? board[row][col] : '';
    cell.classList.toggle('visited', visited[row][col]);
  });

  const countCells = boardCountContainer.querySelectorAll('.cell');
  countCells.forEach((cell, idx) => {
    const row = Math.floor(idx / n);
    const col = idx % n;
    cell.textContent = board[row][col] ? board[row][col] : '';
    // Usa otro color para que destaque en el segundo tablero
    cell.style.backgroundColor = board[row][col] ? '#a8dadc' : '#f0f2f5';
    cell.style.color = board[row][col] ? '#1d3557' : '#ccc';
  });
}

function updatePositionsIndex() {
  if (pathPositions.length === 0) {
    positionsIndexContainer.innerHTML = 'Sin movimientos aún.';
    return;
  }
  let html = pathPositions.map(
    (pos, idx) => `${idx + 1}: (${pos.x}, ${pos.y})`
  ).join('<br/>');
  positionsIndexContainer.innerHTML = html;
}

function waitUntilResumed() {
  return new Promise(resolve => {
    const interval = setInterval(() => {
      if (!paused) {
        clearInterval(interval);
        resolve();
      }
    }, 100);
  });
}
