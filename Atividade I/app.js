// valor de y: 680 - valor do banco / 40
// height: valor do banco / 40
// posição y do texto: height - 5
// 40 é o valor de pixels por número de casos

function calcularPosicaoBarra(valor) {
    return 680 - (valor / 40);
}

function calcularAlturaBarra(valor) {
    return (valor / 40);
}

function calcularPosicaoYTexto(valor) {
    return 680 - (valor / 40) - 5;
}

function read () {
    return fetch('df.csv')
    .then(response => {
        return response.text()
    })
}

var d = read();
console.log(d);
 



