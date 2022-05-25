
function listaProductos(arregloProductos){
    let mostrar = document.getElementById("id01").style.display='block'
    let etiqueta = document.querySelector(".mostrar")
    let contenedor = ''
    for (let producto of arregloProductos){
        contenedor=contenedor+'<tr><td class="producto-col">'+producto.imagen+'<div class="pc-title"><h4>'+producto.nombre+'</h4></div></td><td class="precio-col">$'+producto.valor+'</td></tr>'
    }
    etiqueta.innerHTML = contenedor
    return (arregloProductos , mostrar)
}