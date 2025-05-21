const input = document.getElementById("boardProcess");

function seleccionarPersonajeJugador(){
    alert('Seleccionaste a tu personaje 💣')
    const personajeSeleccionado = document.querySelector('input[name="personaje"]:checked')
   if (personajeSeleccionado) {
        alert(`Seleccionaste a ${personajeSeleccionado.id}`);
    } else {
        alert("No seleccionaste ningún personaje");
    }
}
let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

