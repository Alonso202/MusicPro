function listaProductos(arregloProductos){
    let mostrar = document.getElementById("id01").style.display='block'
    let etiqueta = document.querySelector(".mostrar")
    let contenedor = ''
    for (let producto of arregloProductos){
        contenedor=contenedor+'<tr><td class="producto-col">'+producto.nombre+'</td><td class="producto-col">'+producto.valor+'</td></tr>'    }
    etiqueta.innerHTML = contenedor
    return (arregloProductos , mostrar)
}
function mostrarProductosDespachados(arregloProductos){
    let mostrar = document.getElementById("id02").style.display='block'
    let etiqueta = document.querySelector(".mostrarPedidos")
    let contenedor = ''
    for (let producto of arregloProductos){
        contenedor=contenedor+'<tr><td class="producto-col">'+producto.nombre+'</td><td class="producto-col">'+producto.valor+'</td></tr>'
        
    }
    etiqueta.innerHTML = contenedor
    return (arregloProductos , mostrar)

}
function mandarBodega(){
     console.log("Mandando información")
}
function enviarPedido(){
    console.log("Se a enviado a cliente")
}

