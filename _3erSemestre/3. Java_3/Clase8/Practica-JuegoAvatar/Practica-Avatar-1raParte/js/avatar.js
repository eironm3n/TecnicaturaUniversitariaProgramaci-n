function iniciarJuego(){
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
}

function seleccionarPersonajeJugador(){
    if(document.getElementById('zuko').checked){
        alert('Seleccionaste a Zuko')
    }
}



windows.addEventListener('load',iniciarJuego);