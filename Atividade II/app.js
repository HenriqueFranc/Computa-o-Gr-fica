function putpixel(x, y) {
    var svgNS = "http://www.w3.org/2000/svg";  

    var myCircle = document.createElementNS(svgNS,"circle"); 
    myCircle.setAttributeNS(null,"class","mycircle");
    myCircle.setAttributeNS(null,"cx",x);
    myCircle.setAttributeNS(null,"cy",y);
    myCircle.setAttributeNS(null,"r", 1);
    
    document.querySelector("svg").appendChild(myCircle);
}

// Implementação do DDA

function DDA(X1,Y1, X2,Y2)
{
    let step;
    let X, Y, Xinc, Yinc;
    step = Math.abs(X2 - X1);
    if (Math.abs(Y2 - Y1) > step)
        step = Math.abs(Y2-Y1);
    
    Xinc = (X2 - X1)/step;
    Yinc = (Y2 - Y1)/step;
    X = X1;
    Y = Y1;

    while(X < X2) {
        putpixel(Math.round(X),Math.round(Y));
        X = X + Xinc;
        Y = Y + Yinc;
    }
}

// Implementação do Bresenham

function bresenham(X1,Y1, X2,Y2) {
    let dx = X2 - X1;
    let dy = Y2 - Y1;

    let x = X1;
    let y = Y1;

    let p = (2 * dy) - dx;
    while (x != X2 && y != Y2) {
        if (p < 0) {
            x = x + 1;
            p = p + (2 * dy);
            putpixel(x, y); 
        } else {
            x = x + 1;
            y = y + 1;
            putpixel(x, y);
            p = p + (2 * dy) - (2 * dx);
        }
    }
}

// Implementação do Algoritmo de Círculo Simples

function PlotPoint(xc, yc, x, y)
{
    putpixel(xc + x, yc + y);
    putpixel(xc - x, yc + y);
    putpixel(xc + x, yc - y);
    putpixel(xc - x, yc - y);
    putpixel(xc + y, yc + x);
    putpixel(xc - y, yc + x);
    putpixel(xc + y, yc - x);
    putpixel(xc - y, yc - x);
}

function algoritmoCirculoSimples(xc, yc, r)
{
    let x,y;
    let yr;
    x = 0;
    y = r;
    yr = r;
    PlotPoint(xc, yc, x, y);
    
    while (x < yr)
    {
        x = x + 1;
        yr = Math.sqrt(r*r-x*x);
        y = Math.round(yr);
        PlotPoint(xc,yc,x,y);
    }
}

// Implementação do Ponto Médio para Círculos

function pontoMedioParaCirculo(xc, yc, r){
    let x, y, p;
    x = 0;
    y = r;
    p = 1 - r;
    PlotPoint(xc, yc, x, y);  
    
    while (x < y)
    {
        x = x + 1;
        if (p < 0)
            p = p + 2*x + 1;
        else {
            y = y - 1;
            p = p + 2*(x - y) + 1;
        }

        PlotPoint(xc, yc, x, y);  
    }
}

// Form

function execução(id){
    
    let pontos;
    let chave = selecao(id);

    switch (chave) {

        case 'DDA':
            pontos = receberInputRetas('x1','x2','y1','y2');
            DDA(pontos[0],pontos[1],pontos[2],pontos[3]);
            bresenham(0,0,0,0);
            break;

        case 'Bresenham':
            pontos = receberInputRetas('x1','x2','y1','y2');
            bresenham(pontos[0],pontos[1],pontos[2],pontos[3]);
            break;
        case 'Ponto Médio':
            pontos = receberInputCirculo('raio','x1circulo','y1circulo');
            pontoMedioParaCirculo(pontos[0],pontos[1],pontos[2]);
            break;

        case 'Círculo Simples':
            pontos = receberInputCirculo('raio','x1circulo','y1circulo');
            algoritmoCirculoSimples(pontos[0],pontos[1],pontos[2]);
            break;

        default:
            break;
    }
}

function selecao(id){
    var e = document.getElementById(id);
    var strUser = e.options[e.selectedIndex].text;
    return strUser;
}

function receberInputRetas(idx1,idx2,idy1,idy2){
 
    var X1 = document.getElementById(idx1);
    var valueX1 = parseFloat(X1.value);
    var X2 = document.getElementById(idx2);
    var valueX2 = parseFloat(X2.value);
    var Y1 = document.getElementById(idy1);
    var valueY1 = parseFloat(Y1.value);
    var Y2 = document.getElementById(idy2);
    var valueY2 = parseFloat(Y2.value);

    return [valueX1,valueY1,valueX2,valueY2]
}

function receberInputCirculo(idRaio, idx1, idy1){
    var raio = document.getElementById(idRaio);
    var valueRaio = parseFloat(raio.value);
    var X1 = document.getElementById(idx1);
    var valueX1 = parseFloat(X1.value);
    var Y1 = document.getElementById(idy1);
    var valueY1 = parseFloat(Y1.value);

    return [valueX1, valueY1, valueRaio]
}

function limparSvg(){
    let node = document.querySelector("svg");
    node.querySelectorAll('*').forEach(n => n.remove());
}