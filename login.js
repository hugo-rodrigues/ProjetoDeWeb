function Login() {
    console.log("oi")
    let login = document.getElementById("inputEmail").innerHTML()
    let senha = document.getElementById("inputPassword").innerHTML()
    if (login == "teste" && senha == "senha") {
        window.location.href = "Home.html"
    } else {
        alert("Tente colocar teste e senha")
    }
}

function Cadastrar() {

    window.location.href = "Cadastro.html"
}