
// continue

for(let contando=0 ; contando<= 10 ; contando++ ){
    if (contando % 2 !== 0){
        continue    // esto continuara a la siguiente iteración
    }
    console.log(contando)   // esto mostraria 0,2,4,6,8,10
}

console.log("Termina el ciclo al encontrar el primer número par");
