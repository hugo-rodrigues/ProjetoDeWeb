function InicioPerfil() {
    const url = '/EnviarDadosEditar'
    fetch(url)
        .then(response => response.json())
        .then(json => {

            // document.getElementById("mudancaDolar").innerHTML = JSON.stringify(json.dolarVariacao)
            // document.getElementById("statusDolar").innerHTML = JSON.stringify(json.dolarCompra)
            // if (json.dolarVariacao > 1) {
            //     document.getElementById("recomendacaoDolar").innerHTML = 'Comprar'
            // } else {
            //     document.getElementById("recomendacaoDolar").innerHTML = 'Nao Comprar'
            // }

        })
}

function EditarPerfil() {
    let email = document.getElementById("inputEmail").innerHTML()
    let senha = document.getElementById("inputPassword").innerHTML()

    let usuario = document.getElementById("inputUsuario").innerHTML()



    var entry = {
        email: email,
        senha: senha,
        usuario: usuario
    };

    fetch(`/EditarDados`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        })
        .then(function(response) {
            if (response.status !== 200) {
                console.log(`Looks like there was a problem. Status code: ${response.status}`);
                return;
            }
            response.json().then(function(data) {
                console.log(data.message);
            });
        })
        .catch(function(error) {
            console.log("Fetch error: " + error);
        });



}
InicioPerfil()