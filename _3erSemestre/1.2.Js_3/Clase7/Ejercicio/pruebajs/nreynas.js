// Visualizador del problema de las N Reinas por terminal (Quokka compatible)

const N = 8; // Puedes cambiar el valor aquí (mínimo 8 recomendado)
let solutions = [];
let currentSolutionIndex = 0;

function isSafe(board, row, col, n) {
  for (let i = 0; i < row; i++) {
    if (board[i] === col || Math.abs(board[i] - col) === Math.abs(i - row)) {
      return false;
    }
  }
  return true;
}

function solveNQueens(n, row = 0, board = []) {
  if (row === n) {
    solutions.push([...board]);
    return;
  }
  for (let col = 0; col < n; col++) {
    if (isSafe(board, row, col, n)) {
      board[row] = col;
      solveNQueens(n, row + 1, board);
    }
  }
}

function drawBoard(board) {
  const n = board.length;
  let output = '';
  for (let row = 0; row < n; row++) {
    let line = '';
    for (let col = 0; col < n; col++) {
      line += board[row] === col ? ' Q ' : ' . ';
    }
    output += line + '\n';
  }
  return output;
}

function showSolution(index) {
  const board = solutions[index];
  console.log("===============================");
  console.log(`\x1b[1mSolución #${index + 1} de ${solutions.length}\x1b[0m`);
  console.log(drawBoard(board));
  console.log("Índices de reinas:", board);
  console.log("===============================\n");
}

// Ejecutar solución
if (N < 4) {
  console.log("N debe ser al menos 4 para tener soluciones válidas.");
} else {
  solveNQueens(N);
  if (solutions.length > 0) {
    for (let i = 0; i < solutions.length; i++) {
      showSolution(i);
    }
  } else {
    console.log("No se encontraron soluciones.");
  }
}
