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

    tablaBody.appendChild(nuevaFila);

    patenteInput.value = '';
    patenteInput.focus();
});
