document.addEventListener("DOMContentLoaded", () => {
    const patenteInput = document.getElementById("patente");
    const sectorInput = document.getElementById("sector");
    const tiempoEstimadoInput = document.getElementById("tiempo_estimado");
    const ingresoInput = document.getElementById("ingreso");
    const egresoInput = document.getElementById("egreso");
    const tablaBody = document.getElementById("tabla-body");
    const reloj = document.getElementById("reloj");

    function actualizarReloj() {
        const ahora = new Date();
        reloj.textContent = ahora.toLocaleTimeString();
    }
    setInterval(actualizarReloj, 1000);
    actualizarReloj();

    function limpiarInputs() {
        patenteInput.value = "";
        sectorInput.value = "";
        tiempoEstimadoInput.value = "";
        ingresoInput.value = "";
        egresoInput.value = "";
    }

    function cargarDatos() {
        fetch("/vehiculos")
            .then(res => res.json())
            .then(data => {
                tablaBody.innerHTML = "";
                data.forEach(v => {
                    const tr = document.createElement("tr");
                    tr.innerHTML = `
                        <td>${v.id}</td>
                        <td>${v.patente}</td>
                        <td>${v.sector}</td>
                        <td>${v.ingreso}</td>
                        <td>${v.egreso || ""}</td>
                        <td>${v.tiempo_estimado}</td>
                        <td>${v.tiempo_total}</td>
                        <td>${v.precio_hora.toFixed(2)}</td>
                        <td>${v.precio_total.toFixed(2)}</td>
                        <td>${v.pago_confirmado ? "Sí" : "No"}</td>
                    `;
                    tr.dataset.id = v.id;
                    tablaBody.appendChild(tr);
                });
            });
    }

    cargarDatos();

    document.getElementById("btn-registrar").addEventListener("click", () => {
        const data = {
            patente: patenteInput.value.trim(),
            sector: sectorInput.value.trim(),
            tiempo_estimado: tiempoEstimadoInput.value.trim(),
            ingreso: ingresoInput.value.trim(),
            egreso: egresoInput.value.trim()
        };

        if (!data.patente || !data.sector) {
            alert("Debe completar Patente y Sector.");
            return;
        }

        fetch("/registrar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(res => {
            if (!res.ok) throw new Error("Error al registrar");
            return res.json();
        })
        .then(() => {
            alert("Vehículo registrado correctamente.");
            limpiarInputs();
            cargarDatos();
        })
        .catch(err => alert(err.message));
    });

    document.getElementById("btn-buscar").addEventListener("click", () => {
        const patente = prompt("Ingrese la patente a buscar (sin guion):");
        if (!patente) return;

        fetch(`/buscar?patente=${encodeURIComponent(patente.trim())}`)
        .then(res => {
            if (!res.ok) throw new Error("Vehículo no encontrado.");
            return res.json();
        })
        .then(v => {
            alert(`Patente: ${v.patente}\nSector: ${v.sector}\nIngreso: ${v.ingreso}\nEgreso: ${v.egreso || "No egresado"}\nPrecio Total: ${v.precio_total.toFixed(2)}`);
        })
        .catch(err => alert(err.message));
    });

    document.getElementById("btn-cobrar").addEventListener("click", () => {
        const selectedRow = document.querySelector("#tabla-body tr.table-active");
        if (!selectedRow) {
            alert("Seleccione un vehículo en la tabla para cobrar.");
            return;
        }
        const vehiculoId = selectedRow.dataset.id;

        fetch("/cobrar", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({id: vehiculoId})
        })
        .then(res => {
            if (!res.ok) throw new Error("Error al cobrar.");
            return res.json();
        })
        .then(data => {
            alert(`Cobro realizado. Total: $${data.precio_total}`);
            cargarDatos();
        })
        .catch(err => alert(err.message));
    });

    // Selección fila tabla para cobrar
    tablaBody.addEventListener("click", (e) => {
        const tr = e.target.closest("tr");
        if (!tr) return;
        tablaBody.querySelectorAll("tr").forEach(row => row.classList.remove("table-active"));
        tr.classList.add("table-active");
    });

    // Exportar Excel
    document.getElementById("export-excel").addEventListener("click", () => {
        window.location.href = "/exportar/excel";
    });

    // Exportar CSV
    document.getElementById("export-csv").addEventListener("click", () => {
        window.location.href = "/exportar/csv";
    });
});
