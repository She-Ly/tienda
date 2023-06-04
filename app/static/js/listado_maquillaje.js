
(function(){
    const btnsComprarMaquillaje=document.querySelectorAll('.btnComprarMaquillaje');
     let codigoMaquillajeSeleccionado=null;

    btnsComprarMaquillaje.forEach((btn)=>{
        btn.addEventListener('click',function(){
            codigoMaquillajeSeleccionado=this.id;
            confirmarCompra();
        })
    })
    
    const confirmarCompra=async()=>{
       await fetch('http://127.0.0.1:5000/comprarMaquillaje',{
         method:'POST',
         mode:'same-origin',
         credentials:'same-origin'
         headers:{
            'Content-Type':'application/json',
            'X-XSRF-TOKEN':''
         },
         body:JSON.stringify({
            'codigo': codigoMaquillajeSeleccionado
         })
        }) .then(response =>{
            if(!response.ok){
                console.error("Error!")
            }
            return response.json();

        }).then(data =>{
            console.log("Producto comprado")
        }).catch(error=>{
            console.error("Error ${error}")
        })

    }
    
})();