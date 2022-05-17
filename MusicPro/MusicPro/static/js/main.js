crearStorage();

function crearStorage(){
    if(localStorage.getItem('carrito')==null){
        localStorage.setItem('carrito', '[]')
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
}

//EVENTO CLICK PARA BOTONES
document.querySelectorAll('.boton-producto').forEach(button => {
    button.addEventListener('click', function (){

        idProducto = button.parentNode.querySelector('h4').innerText
        nombre = button.parentNode.querySelector('h5').innerText
        marca = button.parentNode.querySelector('h6').innerText
        precio = button.parentNode.querySelector('span').innerText
        img = button.parentNode.parentNode.querySelector('img').src

        agregarProducto(idProducto, nombre, marca, precio, 1, img);
    })
});

//AGREGAR PRODUCTO CARRITO
function agregarProducto(idProducto, nombre, marca, precio, cantidad, img){
    let producto = {
        idP: idProducto, 
        nombreP: nombre,
        marcaP: marca,
        precioP: precio,
        cantidadP:  cantidad,
        imgP: img
    }

    if (verificarProductoCarrito(producto.idP)){
        console.log('Producto No Agregado')
    }
    else{
        let arregloProductos = traerStorageCarrito();
        arregloProductos.push(producto)
        arregloProductos = JSON.stringify(arregloProductos)
        entregarStorageCarrito(arregloProductos)
        console.log('Producto Agregado')
    }    
}

//VERIFICAR PRODUCTO CARRITO
function verificarProductoCarrito(idProducto){
    let carrito = traerStorageCarrito()

    for (let producto of carrito){
        if(producto.idP === idProducto){
            console.log('Producto existe dentro del carrito')
            return true
        }
    }
    console.log('Producto no existe dentro del carrito')
    return false;
}

//TRAER BASE DE DATOS
function traerStorageCarrito(){
    return JSON.parse(localStorage.getItem('carrito'))
}

//ENTREGA BASE DE DATOS
function entregarStorageCarrito(datos){
    localStorage.setItem('carrito', datos)
}
































//FILTRO DE PRODUCTOS
$(document).ready(function(){
            
    $('.boton-filtrador').click(function(){
        var value = $(this).attr('data-filter');

        if(value == 'todo')
        {
            $('.filtro').show('10000')
        }
        else{
            $('.filtro').not('.'+value).hide('30000');
            $('.filtro').filter('.'+value).show('30000');
        }
    });

    if($('.boton-filtrador').removeClass('active')){
        $(this).removeClass('active')
    }
    $(this).addClass('active')
});
