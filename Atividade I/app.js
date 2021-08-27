// Processar Dados
function processData(allText) {
    var allTextLines = allText.split(/\r\n|\n/);
    var headers = allTextLines[0].split(',');
    var lines = [];

    for (var i=1; i<allTextLines.length; i++) {
        var data = allTextLines[i].split(',');
        if (data.length == headers.length) {

            var tarr = {};
            for (var j=0; j<headers.length; j++) {
                let  key = headers[j]
                let  value = data[j]
                tarr[key]= value
                
            }
            
            lines.push(tarr);
        }
    }

    return lines;
    // console.log(lines)
    // var centro_Value = lines[0].casosAcumulados
    // var posicaoBarraCentro = calcularPosicaoBarra(centro_Value)
    // var alturaBarraCentro = calcularAlturaBarra(centro_Value)
    // var posicaoTextCentro = calcularPosicaoYTexto(centro_Value)

    // var nordeste_Value = lines[1].casosAcumulados
    // var norte_Value = lines[2].casosAcumulados
    // var sudeste_Value = lines[3].casosAcumulados
    // var sul_Value = lines[4].casosAcumulados
}

// Cálculo das Posições
// 680 é a posição Y do eixo X
// Valor de Y da barra: 680 - (valor do banco / 40)
// Altura da Barra: (valor do banco / 40)
// Posição Y do texto: Y da Barra - 5
// 40 é o valor de pixels por número de casos definido pela equipe

function calcularPosicaoYBarra(valor) {
    return 680 - (valor / 40);
}

function calcularAlturaBarra(valor) {
    return (valor / 40);
}

function calcularPosicaoYTexto(valor) {
    return 680 - (valor / 40) - 5;
}

$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "https://raw.githubusercontent.com/HenriqueFranc/Computa-o-Gr-fica/main/Atividade%20I/df.csv",
        dataType: "text",
        success: function(data) {
            var dados = processData(data);
            
            // Dados de Cada Região
            var centroOeste = dados[0];
            var Nordeste = dados[1];
            var Norte = dados[2];
            var Sudeste = dados[3];
            var Sul = dados[4];
            
            // Modificando o Gráfico
            var centro_oeste = document.querySelector(".centro-oeste");
            centro_oeste.children[0].setAttribute("height",  calcularAlturaBarra(centroOeste.casosAcumulados));
            centro_oeste.children[0].setAttribute("y",  calcularPosicaoYBarra(centroOeste.casosAcumulados));
            centro_oeste.children[1].setAttribute("y",  calcularPosicaoYTexto(centroOeste.casosAcumulados))
            centro_oeste.children[2].innerHTML = centroOeste.regiao
            
            var nordeste = document.querySelector(".nordeste");
            nordeste.children[0].setAttribute("height",  calcularAlturaBarra(Nordeste.casosAcumulados));
            nordeste.children[0].setAttribute("y",  calcularPosicaoYBarra(Nordeste.casosAcumulados));
            nordeste.children[1].setAttribute("y",  calcularPosicaoYTexto(Nordeste.casosAcumulados))
            nordeste.children[2].innerHTML = Nordeste.regiao
        
            var norte = document.querySelector(".norte");
            norte.children[0].setAttribute("height",  calcularAlturaBarra(Norte.casosAcumulados));
            norte.children[0].setAttribute("y",  calcularPosicaoYBarra(Norte.casosAcumulados));
            norte.children[1].setAttribute("y",  calcularPosicaoYTexto(Norte.casosAcumulados))
            norte.children[2].innerHTML = Norte.regiao
        
            var sudeste = document.querySelector(".sudeste");
            sudeste.children[0].setAttribute("height",  calcularAlturaBarra(Sudeste.casosAcumulados));
            sudeste.children[0].setAttribute("y",  calcularPosicaoYBarra(Sudeste.casosAcumulados));
            sudeste.children[1].setAttribute("y",  calcularPosicaoYTexto(Sudeste.casosAcumulados))
            sudeste.children[2].innerHTML = Sudeste.regiao
        
            var sul = document.querySelector(".sul");
            sul.children[0].setAttribute("height",  calcularAlturaBarra(Sul.casosAcumulados));
            sul.children[0].setAttribute("y",  calcularPosicaoYBarra(Sul.casosAcumulados));
            sul.children[1].setAttribute("y",  calcularPosicaoYTexto(Sul.casosAcumulados))
            sul.children[2].innerHTML = Sul.regiao
        }
    });
});