function Login() {

    let login = document.getElementById("inputEmail").innerHTML()
    let senha = document.getElementById("inputPassword").innerHTML()
        // if (login == "teste" && senha == "senha") {
        //     window.location.href = "Home.html"
        // } else {
        //     alert("Tente colocar teste e senha")
        // }

    var name = 'testes1'
    var message = 'testesss'

    var entry = {
        login: login,
        senha: senha
    };

    fetch(`/loginEntrada`, {
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
                console.log(data);
            });
        })
        .catch(function(error) {
            console.log("Fetch error: " + error);
        });


}