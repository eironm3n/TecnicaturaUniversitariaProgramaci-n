function iniciarJuego(){
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
}

function seleccionarPersonajeJugador(){
    let inputZuko = document.getElementById('zuko')
    let inputKatara = document.getElementById('katara')
    let inputAang = document.getElementById('aang')
    let inputToph = document.getElementById('toph')

    if(inputZuko.checked){
    alert('Seleccionaste a Zuko')
    }else if(inputKatara.checked){
    alert('Seleccionaste a Katara')
    }else if(inputAang.checked){
    alert('Seleccionaste a Aang')
    }else if(inputToph.checked){
    alert('Seleccionaste a Toph')
    }
}




windows.addEventListener('load',iniciarJuego);