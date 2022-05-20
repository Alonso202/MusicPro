poblarCarrito()
let valorTotalCarrito = parseInt(document.querySelector('.total-pago h2 span').innerText)
let Moneda = document.querySelector('.total-pago h2 .moneda').innerText

//POBLAR CARRITO
function poblarCarrito(){
    let arregloProductos = traerStorageCarrito();
    let totalCarrito = 0
    let weaRancia = ''
    let hValorTotal = document.querySelector('.total-pago h2 span')

    if(arregloProductos == 0){
        let cuerpoTable = document.querySelector('.centralizacion')

        cuerpoTable.innerHTML = '<tr><td colspan="3"><h2 class="titulo-vacio">Tu carrito está vacío</h2><img class="imagen-vacio" src="../static/img/carritoVacio.svg"></td></tr>'
        hValorTotal.innerText = totalCarrito
        
        let todoSpad = document.querySelector('.spad')
        todoSpad.removeAttribute('style')
    }
    else{
        let cuerpoTable = document.querySelector('.centralizacion')

        

        for (producto of arregloProductos){
            let cantidadValor = producto.cantidadP * producto.precioP
            totalCarrito = totalCarrito + cantidadValor
            weaRancia = weaRancia + '<span style="display: none;">'
            +producto.idP+'</span><tr class="carrito-producto"><td class="producto-col"><img src="'
            +producto.imgP+'"><div class="pc-title"><h4>'
            +producto.nombreP+'</h4><a onclick="borrarProducto(`'+producto.idP+'`)" href="#'
            +producto.nombreP+'">Eliminar Producto</a></div></td><td class="cantidad-col"><div class="boton-grupo" role="group" aria-label="Basic example">'
            +producto.cantidadP+'</div></td><td class="total-col">$'
            +cantidadValor+'</td></tr>'
        }
        hValorTotal.innerText = totalCarrito
        cuerpoTable.innerHTML = weaRancia

        //ALGO QUE NO SIRVE DE NADA
        if(arregloProductos.length == 1)
        {
            let todoSpad = document.querySelector('.spad')
            todoSpad.setAttribute('style', 'padding-bottom: 237px;')
        }
    }
}

//BORRAR PRODUCTO CARRITO, PARAMETRO EN STRING
function borrarProducto(idProducto){
    let arregloProductos = traerStorageCarrito();

    let nuevoCarrito = []

    for(let producto of arregloProductos)
    {
        if(producto.idP !== idProducto)
        {
            nuevoCarrito.push(producto)
        }
    }

    nuevoCarrito = JSON.stringify(nuevoCarrito)
    entregarStorageCarrito(nuevoCarrito)
    console.log('Producto Borrado del Carrito')

    cantidadCarrito();
    poblarCarrito();
    document.querySelector('.total-pago h2 .moneda').innerText = 'CLP'
    valorTotalCarrito = parseInt(document.querySelector('.total-pago h2 span').innerText)
}

//BORRAR TODOS LOS PRODUCTOS
function borrarTodo(){
    let carritoVacio = []
    carritoVacio = JSON.stringify(carritoVacio)
    entregarStorageCarrito(carritoVacio)
    cantidadCarrito();
    poblarCarrito()

    console.log('Se limpio el carrito')
    valorTotalCarrito = parseInt(document.querySelector('.total-pago h2 span').innerText)
    document.querySelector('.total-pago h2 .moneda').innerText = 'CLP'
}

//FUNCION API MONEDA DOLAR
function apiDolar(){
    fetch('https://mindicador.cl/api/dolar/').then(respuesta => respuesta.json())
    .then(data => {
        let valorDolar = data.serie[0].valor
        let hValorTotal = document.querySelector('.total-pago h2 span')
        let hMoneda = document.querySelector('.total-pago h2 .moneda')

        let valorEnDolar = Math.round(parseInt(valorTotalCarrito) / valorDolar * 100) / 100


        hValorTotal.innerText = valorEnDolar
        hMoneda.innerText = 'USD'
    }) 
}
