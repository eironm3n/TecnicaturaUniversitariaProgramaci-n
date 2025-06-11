let patenteSeleccionadaOriginal = null;

// Timer
function actualizarTimer() {
    const now = new Date();
    document.getElementById('timer').textContent = now.toLocaleString();
}

// Verificación de estado del servidor
function verificarEstadoServidor() {
    fetch('/listar')
    .then(response => {
        if (response.ok) {
            document.getElementById('estadoServidor').textContent = 'Online';
            document.getElementById('puntoEstado').className = 'online';
        } else {
            document.getElementById('estadoServidor').textContent = 'Offline';
            document.getElementById('puntoEstado').className = 'offline';
        }
    })
    .catch(() => {
        document.getElementById('estadoServidor').textContent = 'Offline';
        document.getElementById('puntoEstado').className = 'offline';
    });
}

// Listar patentes
function listarPatentes() {
    fetch('/listar')
    .then(response => response.json())
    .then(data => {
        const tbody = document.querySelector('#patentesTable tbody');
        tbody.innerHTML = '';
        data.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.patente}</td>
                <td>${item.ingreso}</td>
            `;
            row.setAttribute('data-pagado', item.pagado);

            if (item.pagado) {
                row.style.backgroundColor = '#e0e0e0';
                row.style.color = '#7f8c8d';
            }

            row.addEventListener('click', function() {
                document.querySelectorAll('#patentesTable tbody tr').forEach(r => r.classList.remove('selected'));
                this.classList.add('selected');
                patenteSeleccionadaOriginal = this.cells[0].innerText;
                document.getElementById('patenteInput').value = patenteSeleccionadaOriginal;

                const pagado = this.getAttribute('data-pagado') === 'true';
                document.getElementById('cobrarBtn').disabled = pagado;
            });

            tbody.appendChild(row);
        });
    });
}

// Alta
document.getElementById('altaBtn').addEventListener('click', function() {
    const patente = document.getElementById('patenteInput').value.trim();
    if (patente !== "") {
        fetch('/alta', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({patente})
        })
        .then(response => {
            if (response.ok) {
                listarPatentes();
                document.getElementById('patenteInput').value = "";
                patenteSeleccionadaOriginal = null;
            }
        });
    }
});

// Actualizar
document.getElementById('actualizarBtn').addEventListener('click', function() {
    const patenteNueva = document.getElementById('patenteInput').value.trim();
    if (patenteSeleccionadaOriginal && patenteNueva !== "") {
        fetch('/actualizar', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({patente_original: patenteSeleccionadaOriginal, patente_nueva: patenteNueva})
        })
        .then(response => {
            if (response.ok) {
                listarPatentes();
                patenteSeleccionadaOriginal = null;
                document.getElementById('patenteInput').value = "";
            }
        });
    }
});

// Eliminar
document.getElementById('eliminarBtn').addEventListener('click', function() {
    if (patenteSeleccionadaOriginal) {
        fetch('/eliminar', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({patente: patenteSeleccionadaOriginal})
        })
        .then(response => {
            if (response.ok) {
                listarPatentes();
                patenteSeleccionadaOriginal = null;
                document.getElementById('patenteInput').value = "";
            }
        });
    }
});

// Cobrar
document.getElementById('cobrarBtn').addEventListener('click', function() {
    const precioHora = parseFloat(document.getElementById('precioHoraInput').value);
    if (patenteSeleccionadaOriginal) {
        fetch('/cobrar', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({patente: patenteSeleccionadaOriginal, precio_hora: precioHora})
        })
        .then(response => response.json())
        .then(data => {
            if (data.monto_total !== undefined) {
                alert(`Monto a cobrar: $${data.monto_total}`);
                listarPatentes();
                patenteSeleccionadaOriginal = null;
                document.getElementById('patenteInput').value = "";
            } else {
                alert(data.message);
            }
        });
    }
});

// Inicialización
document.addEventListener('DOMContentLoaded', function() {
    listarPatentes();
    actualizarTimer();
    setInterval(actualizarTimer, 1000);
    setInterval(verificarEstadoServidor, 3000);
});
