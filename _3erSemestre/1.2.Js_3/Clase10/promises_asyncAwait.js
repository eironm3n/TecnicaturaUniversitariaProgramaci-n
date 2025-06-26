

//async/await
async function funcionConPromesaYAwait() {
    let miPromesa = new Promise(resolver=>{
        resolver('Promesa con await');
    })
    console.log(await miPromesa)
}

funcionConPromesaYAwait();

