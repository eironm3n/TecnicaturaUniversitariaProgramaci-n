

//async/await
async function funcionConPromesaYAwait() {
    let miPromesa = new Promise(resolver=>{
        resolver('Promesa con await');
    })
    console.log(await miPromesa)
}

funcionConPromesaYAwait();

// Promesas, await, async y setTimeOut
async function funcionConPromesaAwaitTimeout() {
    let miPromesa = new Promise(resolver => {
        console.log('Inicio función');
        setTimeout(()=>resolver('Promesa con await y TimeOut'),3000);
        console.log('Fin función');
    })
    console.log(await miPromesa)
}
funcionConPromesaAwaitTimeout();

