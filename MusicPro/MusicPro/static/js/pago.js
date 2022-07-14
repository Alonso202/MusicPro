
function traerStorageCarrito(){
    return JSON.parse(localStorage.getItem('carrito'))
}

let arregloProductos = traerStorageCarrito();
let totalCarritoUSD = 0
let totalCarrito = 0
fetch('https://mindicador.cl/api/dolar/').then(respuesta => respuesta.json())
    .then(data => {
        let valorDolar = data.serie[0].valor
        let hValorTotal = document.querySelector('.total-pedido-dolar')
        let valorEnDolar = Math.round(parseInt(totalCarrito) / valorDolar * 100) / 100

        hValorTotal.innerText = valorEnDolar

        totalCarritoUSD = totalCarritoUSD + valorEnDolar
        console.log(totalCarritoUSD)
})

for (producto of arregloProductos){
    let cantidadValor = producto.cantidadP * producto.precioP
    totalCarrito = totalCarrito + cantidadValor
}
console.log(totalCarrito)
document.getElementById("total-pedido").innerHTML=totalCarrito


function borrarTodo(){
    let carritoVacio = []
    carritoVacio = JSON.stringify(carritoVacio)
    entregarStorageCarrito(carritoVacio)
    cantidadCarrito();

    console.log('Se limpio el carrito')
}