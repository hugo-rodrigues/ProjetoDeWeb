function InicioEuro() {
    const url = '/paginaEuro'
    fetch(url)
        .then(response => response.json())
        .then(json => {

            document.getElementById("mudancaEuro").innerHTML = JSON.stringify(json.euroVariacao)
            document.getElementById("statusEuro").innerHTML = JSON.stringify(json.euroCompra)
            if (json.dolarVariacao > 1) {
                document.getElementById("recomendacaoEuro").innerHTML = 'Comprar'
            } else {
                document.getElementById("recomendacaoEuro").innerHTML = 'Nao Comprar'
            }

        })
}


InicioEuro()