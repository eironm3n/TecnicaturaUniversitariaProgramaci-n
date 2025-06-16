const $=sel=>document.querySelector(sel);

const cargarTabla=async()=>{
  const res=await fetch('/vehiculos');
  const datos=await res.json();
  $('#tbody').innerHTML = datos.map(r=>`
    <tr data-id="${r[0]}">
      <td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]||''}</td><td>${r[5]||''}</td>
      <td>${r[8]==='Si'? (r[7]||''):`<button class='btnCobrar'>Cobrar</button>`}</td>
    </tr>`).join('');
};

$('#btnRegistrar').onclick=async()=>{
  const fd={patente:$('#patente').value, sector:$('#sector').value, precio_hora:$('#precioHora').value};
  const res=await fetch('/registrar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(fd)});
  if(res.ok){ cargarTabla(); } else alert(await res.text());
};

$('#tbody').addEventListener('click', async e=>{
  if(e.target.classList.contains('btnCobrar')){
    const id=e.target.closest('tr').dataset.id;
    await fetch('/cobrar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id})});
    cargarTabla();
  }
  const tr=e.target.closest('tr');
  if(tr){
    $('#ingreso').value=tr.children[2].textContent;
    $('#egreso').value=tr.children[3].textContent;
    $('#tiempoEstimado').value=tr.children[4].textContent;
  }
});

window.onload = cargarTabla;