function InicioDolar() {
    const url = '/paginaDolar'
    fetch(url)
        .then(response => response.json())
        .then(json => {

            document.getElementById("mudancaDolar").innerHTML = JSON.stringify(json.dolarVariacao)
            document.getElementById("statusDolar").innerHTML = JSON.stringify(json.dolarCompra)
            if (json.dolarVariacao > 1) {
                document.getElementById("recomendacaoDolar").innerHTML = 'Comprar'
            } else {
                document.getElementById("recomendacaoDolar").innerHTML = 'Nao Comprar'
            }

        })
}


InicioDolar()