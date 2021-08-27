// Implementação do DDA

function putpixel(x, y) {
    var svgNS = "http://www.w3.org/2000/svg";  

    var myCircle = document.createElementNS(svgNS,"circle"); 
    myCircle.setAttributeNS(null,"class","mycircle");
    myCircle.setAttributeNS(null,"cx",x);
    myCircle.setAttributeNS(null,"cy",y);
    myCircle.setAttributeNS(null,"r", 1);
    
    document.querySelector("svg").appendChild(myCircle);
}

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

DDA(0, 0, 1280, 720)

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

bresenham(0, 500, 1280, 720)

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

algoritmoCirculoSimples(200,200,100);

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
 
pontoMedioParaCirculo(300,200, 200);

// Form

