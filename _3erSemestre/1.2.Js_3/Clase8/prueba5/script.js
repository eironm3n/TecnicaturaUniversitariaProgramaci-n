// =============================================
// Visualizador del Salto del Caballo
// =============================================
// Descripción: muestra un recorrido del caballo en
// - Tablero estático (izquierda)
// - Tablero animado (centro)
// - Índice de posiciones (derecha)
// Se puede pausar / continuar durante la animación.

// ---------- Configuración y estado ----------
let tablero = [];
let visitado = [];
let n = 8;                  // tamaño del tablero
let retardo = 300;          // milisegundos entre pasos
let ejecutando = false;
let pausa = false;
let recorrido = [];         // lista de posiciones visitadas en orden

// Desplazamientos del caballo (x, y)
const movX = [ 2, 1,-1,-2,-2,-1, 1, 2 ];
const movY = [ 1, 2, 2, 1,-1,-2,-2,-1 ];

// ---------- Elementos de la interfaz ----------
const tableroAnimado = document.getElementById('tableroAnimado');
const tableroEstatico = document.getElementById('tableroEstatico');
const tableroIndice  = document.getElementById('tableroIndice');

const btnIniciar = document.getElementById('btnIniciar');
const btnPausar  = document.getElementById('btnPausar');
const inputTam   = document.getElementById('tamTablero');

// ---------- Eventos ----------
btnIniciar.addEventListener('click', () => {
  if (ejecutando) return;
  n = parseInt(inputTam.value);
  if (n < 5 || n > 10) { alert('El tamaño debe estar entre 5 y 10'); return; }
  inicializarTableros();
  ejecutando = true;
  pausa = false;
  recorrido = [];
  recorridoCaballo(0, 0, 1).then(() => {
    ejecutando = false;
    actualizarTableroEstatico();
  });
});

btnPausar.addEventListener('click', () => {
  if (!ejecutando) return;
  pausa = !pausa;
  btnPausar.textContent = pausa ? 'Continuar' : 'Pausar';
});

// ---------- Inicialización de estructuras ----------
function inicializarTableros() {
  // Dimensiones de grillas
  tableroAnimado.style.gridTemplateColumns = `repeat(${n}, var(--tam-celda))`;
  tableroEstatico.style.gridTemplateColumns = `repeat(${n}, var(--tam-celda))`;
  tableroIndice .style.gridTemplateColumns = `repeat(${n}, var(--tam-celda-indice))`;

  // Reset DOM
  tableroAnimado.innerHTML = '';
  tableroEstatico.innerHTML = '';
  tableroIndice .innerHTML = '';

  // Crear celdas DOM
  for (let i = 0; i < n * n; i++) {
    tableroAnimado.appendChild(document.createElement('div'));
    tableroEstatico.appendChild(document.createElement('div'));
    tableroIndice .appendChild(document.createElement('div'));
  }

  // Matrices de datos
  tablero  = Array.from({ length: n }, () => Array(n).fill(0));
  visitado = Array.from({ length: n }, () => Array(n).fill(false));
}

// ---------- Utilidades ----------
const esperar = (ms) => new Promise(res => setTimeout(res, ms));

async function esperarReanudacion() {
  while (pausa) { await esperar(100); }
}

function esValido(x, y) {
  return x >= 0 && y >= 0 && x < n && y < n && !visitado[x][y];
}

function grado(x, y) {
  let c = 0;
  for (let i = 0; i < 8; i++) {
    const nx = x + movX[i];
    const ny = y + movY[i];
    if (esValido(nx, ny)) c++;
  }
  return c;
}

// ---------- Backtracking con heurística de Warnsdorff ----------
async function recorridoCaballo(x, y, paso) {
  if (pausa) await esperarReanudacion();

  tablero[x][y] = paso;
  visitado[x][y] = true;
  recorrido.push({ x, y });

  actualizarTableroAnimado(paso);
  actualizarTableroIndice();
  await esperar(retardo);

  if (paso === n * n) return true; // recorrido completo

  // Ordenar movimientos por menor grado (heurística)
  const movimientos = [];
  for (let i = 0; i < 8; i++) {
    const nx = x + movX[i];
    const ny = y + movY[i];
    if (esValido(nx, ny)) movimientos.push({ nx, ny, g: grado(nx, ny) });
  }
  movimientos.sort((a, b) => a.g - b.g);

  for (const m of movimientos) {
    if (await recorridoCaballo(m.nx, m.ny, paso + 1)) return true;
  }

  // Retroceso
  tablero[x][y] = 0;
  visitado[x][y] = false;
  recorrido.pop();

  actualizarTableroAnimado(paso - 1);
  actualizarTableroIndice();
  await esperar(retardo);

  return false;
}

// ---------- Actualización visual ----------
function actualizarTableroAnimado(pasoActual) {
  const celdas = tableroAnimado.children;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const idx = i * n + j;
      const celda = celdas[idx];
      const val = tablero[i][j];
      celda.textContent = val || '';
      celda.className = '';
      if (val) celda.classList.add('visitada');
      if (val === pasoActual) celda.classList.add('actual');
    }
  }
}

function actualizarTableroEstatico() {
  const celdas = tableroEstatico.children;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const idx = i * n + j;
      const celda = celdas[idx];
      const val = tablero[i][j];
      celda.textContent = val || '';
      celda.className = val ? 'visitada' : '';
    }
  }
}

function actualizarTableroIndice() {
  const celdas = tableroIndice.children;
  for (const c of celdas) {
    c.textContent = '';
    c.className = '';
  }

  recorrido.forEach((pos, i) => {
    const celda = celdas[i];
    if (!celda) return;
    celda.textContent = `${pos.x},${pos.y}`;
    celda.classList.add('visitada');
  });

  if (recorrido.length) {
    const celdaActual = celdas[recorrido.length - 1];
    if (celdaActual) celdaActual.classList.add('actual');
  }
}
