console.log("salve")

const URL_TO_FETCH = 'https://randomuser.me/api/';
fetch(URL_TO_FETCH, {
        method: 'get' // opcional 
    })
    .then(function(response) {
        // use a resposta 
        console.log(response)
    })
    .catch(function(err) { console.error(err); });