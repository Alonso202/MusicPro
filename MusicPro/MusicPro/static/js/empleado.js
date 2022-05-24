function login(){
    var credentials = btoa("admin:admin");
    var auth = { "Authorization" :  `Basic ${credentials}`};
    fetch('http://127.0.0.1:8000/api/empleados/',{ headers : auth }).then(respuesta => respuesta.json())
    .then(data => {
        let user = document.getElementById("username").value;
        let pass= document.getElementById('password').value;
        for( usuario of data){
            if(usuario.username == user && usuario.password == pass ){
                console.log("Logeado")
                if(usuario.puesto == 1){
                    window.location = "http://127.0.0.1:8000/bodeguero";
                }
                if(usuario.puesto == 2){
                    window.location = "http://127.0.0.1:8000/vendedor";
                }
                if(usuario.puesto == 3){
                    window.location = "http://127.0.0.1:8000/contador";                    
                }
            }
            else{
                console.log("Datos no coinciden")
            }
            }
        })
}