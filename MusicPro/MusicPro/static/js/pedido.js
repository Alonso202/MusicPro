function login(){
    fetch('http://127.0.0.1:8000/api/pedidos/').then(respuesta => respuesta.json())
    .then(data => {
        let id = document.querySelectorAll('.pedido_id');
        for( pedido of data){            
                if(pedido.id == id){
                    for (let productos of pedido.productoCarrito){
                        console.log(productos.nombre)
                    }
                }
        }
        })
        
}



function mostrarProductos(){
    fetch('http://127.0.0.1:8000/api/pedidos/').then(respuesta => respuesta.json())
    .then(data => {
        let id = document.getElementById("pedido_id").innerText;
        for( pedido of data){            
                if(pedido.id == id){
                    for (let productos of pedido.productoCarrito){
                        console.log(productos.nombre)
                    }
                }
        }
        })
        
}