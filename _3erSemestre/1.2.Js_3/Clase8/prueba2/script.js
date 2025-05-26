let board = [];
let visited = [];
let n = 8;
let delay = 300;
let running = false;
let paused = false;

const dx = [2, 1, -1, -2, -2, -1, 1, 2];
const dy = [1, 2, 2, 1, -1, -2, -2, -1];

const boardContainer = document.getElementById('board');
const startBtn = document.getElementById('start');
const pauseBtn = document.getElementById('pause');

startBtn.addEventListener('click', () => {
  if (running) return;
  n = parseInt(document.getElementById('size').value);
  if (n < 5 || n > 10) return;
  initBoard();
  running = true;
  paused = false;
  knightTour(0, 0, 1);
});

pauseBtn.addEventListener('click', () => {
  paused = !paused;
  pauseBtn.textContent = paused ? 'Continuar' : 'Pausar';
});

function initBoard() {
  boardContainer.innerHTML = '';
  boardContainer.style.gridTemplateColumns = `repeat(${n}, 50px)`;
  board = Array.from({ length: n }, () => Array(n).fill(0));
  visited = Array.from({ length: n }, () => Array(n).fill(false));
  for (let i = 0; i < n * n; i++) {
    const cell = document.createElement('div');
    cell.className = 'cell';
    boardContainer.appendChild(cell);
  }
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
  updateBoard();
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

  board[x][y] = 0;
  visited[x][y] = false;
  updateBoard();
  await delayMs(delay);
  return false;
}

function isSafe(x, y) {
  return x >= 0 && y >= 0 && x < n && y < n && !visited[x][y];
}

function updateBoard() {
  const cells = boardContainer.querySelectorAll('.cell');
  cells.forEach((cell, idx) => {
    const row = Math.floor(idx / n);
    const col = idx % n;
    cell.textContent = board[row][col] ? board[row][col] : '';
    cell.classList.toggle('visited', visited[row][col]);
  });
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
