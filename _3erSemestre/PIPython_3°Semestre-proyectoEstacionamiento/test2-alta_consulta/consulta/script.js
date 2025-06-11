// Actualizar el timer cada segundo
function actualizarHora() {
    const timer = document.getElementById('timer');
    const ahora = new Date();
    const hora = ahora.toLocaleTimeString();
    timer.textContent = `Hora actual: ${hora}`;
}

setInterval(actualizarHora, 1000);
actualizarHora(); // llamada inicial

// Manejar el agregado de patentes a la tabla
let contador = 1;
let filaSeleccionada = null;

document.getElementById('agregarBtn').addEventListener('click', function() {
    const patenteInput = document.getElementById('patenteInput');
    const patente = patenteInput.value.trim();

    if (patente === '') {
        alert('Por favor ingrese una patente válida.');
        return;
    }

    const tablaBody = document.querySelector('#tablaPatentes tbody');
    const nuevaFila = document.createElement('tr');

    const celdaNumero = document.createElement('td');
    celdaNumero.textContent = contador++;

    const celdaPatente = document.createElement('td');
    celdaPatente.textContent = patente;

    const celdaHora = document.createElement('td');
    const ahora = new Date();
    celdaHora.textContent = ahora.toLocaleTimeString();

    nuevaFila.appendChild(celdaNumero);
    nuevaFila.appendChild(celdaPatente);
    nuevaFila.appendChild(celdaHora);

    // Hacer clic en la fila → seleccionar para actualizar
    nuevaFila.addEventListener('click', function() {
        seleccionarFila(this);
    });

    tablaBody.appendChild(nuevaFila);

    patenteInput.value = '';
    patenteInput.focus();
});

// Manejar la selección de fila
function seleccionarFila(fila) {
    // Desmarcar la fila anterior
    if (filaSeleccionada) {
        filaSeleccionada.classList.remove('selected');
    }

    filaSeleccionada = fila;
    filaSeleccionada.classList.add('selected');

    // Poner la patente en la casilla
    const patente = filaSeleccionada.cells[1].textContent;
    document.getElementById('patenteInput').value = patente;

    // Habilitar el botón de Actualizar
    document.getElementById('actualizarBtn').disabled = false;
}

// Manejar la actualización de la fila seleccionada
document.getElementById('actualizarBtn').addEventListener('click', function() {
    if (!filaSeleccionada) {
        alert('Seleccione una fila primero.');
        return;
    }

    const patenteInput = document.getElementById('patenteInput');
    const nuevaPatente = patenteInput.value.trim();

    if (nuevaPatente === '') {
        alert('Por favor ingrese una patente válida.');
        return;
    }

    // Actualizar la celda de patente
    filaSeleccionada.cells[1].textContent = nuevaPatente;

    // Limpiar selección
    filaSeleccionada.classList.remove('selected');
    filaSeleccionada = null;

    patenteInput.value = '';
    patenteInput.focus();

    // Deshabilitar el botón de Actualizar
    document.getElementById('actualizarBtn').disabled = true;
});
