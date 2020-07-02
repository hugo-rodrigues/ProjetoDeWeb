function Login() {

    let login = document.getElementById("inputLogin");
    let senha = document.getElementById("inputPassword");

    var entry = {
        login: login.value,
        senha: senha.value
    };


    fetch(`/LoginServico`, {
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

                window.location.href = url + 'home'


            });
        })
        .catch(function(error) {
            console.log("Fetch error: " + error);
        });



}