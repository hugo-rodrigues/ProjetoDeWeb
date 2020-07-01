function submit_message() {
    let email = document.getElementById("inputEmail").innerHTML()
    let senha = document.getElementById("inputPassword").innerHTML()
    let emailConfirmacao = document.getElementById("inputEmail1").innerHTML()
    let senhaConfirmacao = document.getElementById("inputPassword1").innerHTML()
    let usuario = document.getElementById("inputUsuario").innerHTML()


    if (email == emailConfirmacao && senha == senhaConfirmacao) {
        var entry = {
            email: email,
            senha: senha,
            usuario: usuario
        };

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
                    console.log(data.message);
                });
            })
            .catch(function(error) {
                console.log("Fetch error: " + error);
            });
    }


}