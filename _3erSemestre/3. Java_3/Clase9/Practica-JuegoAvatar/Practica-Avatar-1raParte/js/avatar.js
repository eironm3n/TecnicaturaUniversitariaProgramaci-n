function iniciarJuego(){
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
}

function seleccionarPersonajeJugador(){
    let personajeAleatorio = aleatorio(1,4);
    let spanPersonajeJugador = document.getElementById('personaje-jugador')

    if(personajeAleatorio == 1){
        spanPersonajeJugador.innerHTML = 'Piñaso'
    }else if(personajeAleatorio == 2){
        spanPersonajeJugador.innerHTML = 'Patadaso'
    }else if(personajeAleatorio == 3){
        spanPersonajeJugador.innerHTML = 'Barridaso'
    }else{
        alert('Selecciona un personaje')
    }
}

function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

windows.addEventListener('load',iniciarJuego);
