function InicioPerfil() {
    const url = '/EnviarDadosEditar'
    fetch(url)
        .then(response => response.json())
        .then(json => {

            document.getElementById("loginAtual").innerHTML = JSON.stringify(json.login)
            document.getElementById("emailAtual").innerHTML = JSON.stringify(json.email)
            document.getElementById("senhaAtual").innerHTML = JSON.stringify(json.senha)

            // if (json.dolarVariacao > 1) {
            //     document.getElementById("recomendacaoDolar").innerHTML = 'Comprar'
            // } else {
            //     document.getElementById("recomendacaoDolar").innerHTML = 'Nao Comprar'
            // }

        })
}

function EditarPerfil() {
    let email = document.getElementById("email");
    let senha = document.getElementById("senha");

    let usuario = document.getElementById("login");



    var entry = {
        email: email.value,
        senha: senha.value,
        usuario: usuario.value
    };
    console.log(entry)


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

                console.log(data)

            });
        })
        .catch(function(error) {
            console.log("Fetch error: " + error);
        });


}



InicioPerfil()