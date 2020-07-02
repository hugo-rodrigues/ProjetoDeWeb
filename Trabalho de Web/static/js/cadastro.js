function Cadastrar() {
    let email = document.getElementById("inputEmail");
    let senha = document.getElementById("inputPassword");
    let emailConfirmacao = document.getElementById("inputEmail1");
    let senhaConfirmacao = document.getElementById("inputPassword1");
    let usuario = document.getElementById("inputUsuario");


    var entry = {
        email: email.value,
        senha: senha.value,
        usuario: usuario.value
    };
    console.log(entry)
    fetch(`/cadastrar`, {
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

                var url = window.location.href;
                var n = url.search("/cadastro");
                var res = url.slice(0, n)
                window.location.href = res

            });
        })
        .catch(function(error) {
            console.log("Fetch error: " + error);
        });



}