document.getElementById("start").addEventListener("click", () => {
  const size = parseInt(document.getElementById("size").value);
  startTour(size);
});

const moves = [
  [2, 1], [1, 2], [-1, 2], [-2, 1],
  [-2, -1], [-1, -2], [1, -2], [2, -1]
];

function startTour(n) {
  const board = Array.from({ length: n }, () => Array(n).fill(-1));
  createBoardUI(n);
  board[0][0] = 0;
  moveKnight(board, 0, 0, 1, n);
}

function moveKnight(board, x, y, step, n) {
  if (step === n * n) {
    updateUI(board);
    return true;
  }

  for (let [dx, dy] of moves) {
    const nx = x + dx;
    const ny = y + dy;
    if (isValidMove(board, nx, ny, n)) {
      board[nx][ny] = step;
      if (moveKnight(board, nx, ny, step + 1, n)) return true;
      board[nx][ny] = -1;
    }
  }
  return false;
}

function isValidMove(board, x, y, n) {
  return x >= 0 && y >= 0 && x < n && y < n && board[x][y] === -1;
}

function createBoardUI(n) {
  const boardDiv = document.getElementById("board");
  boardDiv.style.gridTemplateColumns = `repeat(${n}, 50px)`;
  boardDiv.innerHTML = "";
  for (let i = 0; i < n * n; i++) {
    const cell = document.createElement("div");
    cell.className = "cell";
    boardDiv.appendChild(cell);
  }
}

function updateUI(board) {
  const cells = document.querySelectorAll(".cell");
  const n = board.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const idx = i * n + j;
      cells[idx].textContent = board[i][j];
      if (board[i][j] !== -1) {
        cells[idx].classList.add("visited");
      }
    }
  }
}