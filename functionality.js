//variables globales
var valores = []; //valores ingresados por el usuario y utilizados al procesar la info
var n = 0.0, r = 0.0, c = 0.0, ic = 0.0;//n = numero de elementos, r = rango, c = clase, ic = indice de clase
var clases = [], Li = 0.0;
var Xi = [], fi = [], Fi = [], Xifi = [];
var XiSq = [], XiCube = []; //XiSq = Xi², XiCube = Xi³
var fi_XiSq = [], fi_XiCube = []; //fi_XiSq = fi * Xi², fi_XiCube = fi * Xi³
var Dx = 0.0, DMe = 0.0, DTipica = 0.0, Varianza = 0.0;
var X = 0.0, Me = 0.0, Mo = 0.0; //X = Media, Me = Mediana, Mo = Moda
var Delta1 = 0.0, Delta2 = 0.0, Sesgo = 0.0;
var Momento1 = 0.0, Momento2 = 0.0, Momento3 = 0.0;
var Momento1Limit = 0.0, Momento2Limit = 0.0, Momento3Limit = 0.0;
var XiDiffXAbs = [], XiDiffXAbsSq = []; //XiDiffXAbs = |Xi - X|, XiDiffXAbsSq = |Xi - X|²
var fi_XiDiffXAbs = [], fi_XiDiffXAbsSq = []; //fi_XiDiffXAbs = fi|Xi - X|, fi_XiDiffXAbsSq = fi|Xi - X|²
var XiDiffMeAbs = [], fi_XiDiffMeAbs = []; //XiDiffMeAbs = |Xi - Me|, fi_XiDiffMeAbs = fi|Xi - Me|

//formulas string
var RangeF = "", ClaseF = "", IcF = "", MediaF = "", MedianaF = "", MoF = "";
var DxF = "", DMeF = "", VarianzaF = "", DTipicaF = "";
var Momento1F = "", Momento2F = "", Momento3F = "", Delta1F = "", Delta2F = "", SesgoF = "";

function Restart() {
    RangeF = "", ClaseF = "", IcF = "", MediaF = "", MedianaF = "", MoF = "";
    DxF = "", DMeF = "", VarianzaF = "", DTipicaF = "";
    Momento1F = "", Momento2F = "", Momento3F = "", Delta1F = "", Delta2F = "", SesgoF = "";
    valores = [];
    n = 0.0, r = 0.0, c = 0.0, ic = 0.0;
    clases = [], Li = 0.0;
    Xi = [], fi = [], Fi = [], Xifi = [];
    XiSq = [], XiCube = [];
    fi_XiSq = [], fi_XiCube = [];
    Dx = 0.0, DMe = 0.0, DTipica = 0.0, Varianza = 0.0;
    X = 0.0, Me = 0.0, Mo = 0.0;
    Delta1 = 0.0, Delta2 = 0.0, Sesgo = 0.0;
    Momento1 = 0.0, Momento2 = 0.0, Momento3 = 0.0;
    XiDiffXAbs = [], XiDiffXAbsSq = [];
    fi_XiDiffXAbs = [], fi_XiDiffXAbsSq = [];
    XiDiffMeAbs = [], fi_XiDiffMeAbs = [];


}


//funciones
function Ordenar() {
    valores.sort((a, b) => a - b);
}

function GetNumeroElementos() {
    n = valores.length;
}

function GetRango() {
    let Ls = Math.max(...valores);
    let Li = Math.min(...valores);
    r = (Ls - Li) + 1;
    RangeF = "("+ Ls.toString() + "-" + Li.toString() +") + 1 = " + r.toString();
}

function GetClase() {
    let temp = Math.round(Math.sqrt(n)*100)/100;
    c = Math.round(temp);
    ClaseF = "\\sqrt{" + n.toString() + "} = " + temp.toString() + " = " + c.toString();
}

function GetIndiceClase() {
    let temp = Math.round((r/c)*100)/100;
    ic = Math.round(temp);
    IcF = "\\frac{"+ r.toString() + "}{" + c.toString() + "} = " + temp.toString() + " = " + ic.toString();
}

function GetSinRepetir() {
    return Array.from(new Set(valores));
}

function GetClases() {
    let temp = []
    let counter = 0;
    let little = Math.min(...GetSinRepetir());
    while(little + counter <= Math.max(...GetSinRepetir())) {
        for(let j = 0; j < ic; j++) {
            temp.push(little + counter);
            counter++;
        }
        clases.push(temp);
        temp = [];
    }
}

function GetXi() {
    clases.forEach(element => {
        Xi.push(element.reduce(function(acc, current) {return acc + current;}, 0)/element.length);
    });
}

function Getfi() {
    clases.forEach(element => {
        let count = 0;
        element.forEach(subelement => {
            count += valores.filter(function(value) {return value === subelement;}).length;
        });
        fi.push(count);
    });
}

function GetFi() {
    let cumulativeSum = 0;
    for (let i = 0; i < fi.length; i++) {
        cumulativeSum += fi[i];
        Fi.push(cumulativeSum);
    }
}

function GetXifi() {
    for(let i = 0; i < Xi.length; i++) {
        Xifi.push(Xi[i] * fi[i]);
    }
}

function GetMedia() {
    let temp = Xifi.reduce(function(acc, current) {return acc + current;}, 0);
    X = Math.round((temp/n)*100)/100;
    MediaF = "\\frac{" + temp.toString() + "}{" + n.toString() + "} = " + X.toString();
}

function GetXiDiffXAbs() {
    for (var i = 0; i < Xi.length; i++) {
        XiDiffXAbs.push(Math.round(Math.abs(Xi[i] - X) * 100) / 100);
    }
}

function Getfi_XiDiffXAbs() {
    for(let i = 0; i < fi.length; i++) {
        fi_XiDiffXAbs.push(Math.round(fi[i] * XiDiffXAbs[i] * 100)/100);
    }
}

function GetMe() {
    let i = 0;
    for(i = 0; i < clases.length; i++) {
        arr_min = Math.min(...clases[i]);
        arr_max = Math.max(...clases[i]);
        if (arr_min < X && X < arr_max) {
            Li = arr_min - 0.5;
            break;
        }
    }
    Me = Math.round((Li + ((n/2 - Fi[i - 1])/fi[i])*ic)*100)/100;
    MedianaF = Li.toString() + "+\\Big(\\frac{\\frac{" + n.toString() +"}{2} - " + Fi[i - 1].toString() +"}{" + fi[i].toString() + "}\\Big)*" + ic.toString() + " = " + Me.toString();
}

function GetXiDiffMeAbs() {
    for (var i = 0; i < Xi.length; i++) {
        XiDiffMeAbs.push(Math.round(Math.abs(Xi[i] - Me) * 100) / 100);
    }
}

function Getfi_XiDiffMeAbs() {
    for(let i = 0; i < fi.length; i++) {
        fi_XiDiffMeAbs.push(Math.round(fi[i] * XiDiffMeAbs[i] * 100)/100);
    }
}

function GetDx() {
    let temp = Math.round(fi_XiDiffXAbs.reduce(function(acc, current) {return acc + current;}, 0)*100)/100;
    Dx = Math.round((temp/n)*100)/100;
    DxF = "\\frac{" + temp.toString() + "}{" + n.toString() + "} = " + Dx.toString();
}

function GetDMe() {
    let temp = Math.round(fi_XiDiffMeAbs.reduce(function(acc, current) {return acc + current;}, 0)*100)/100;
    DMe = Math.round((temp/n) * 100)/100;
    DMeF = "\\frac{" + temp.toString() + "}{" + n.toString() + "} = " + DMe.toString();
}

function GetXiDiffXAbsSq() {
    for(let i = 0; i < XiDiffXAbs.length; i++) {
        XiDiffXAbsSq.push(Math.round(Math.pow(XiDiffXAbs[i], 2)*100)/100);
    }
}

function Getfi_XiDiffXAbsSq() {
    for(let i = 0; i < fi.length; i++) {
        fi_XiDiffXAbsSq.push(Math.round(fi[i] * XiDiffXAbsSq[i] * 100)/100);
    }
}

function GetVarianza() {
    let temp = Math.round(fi_XiDiffXAbsSq.reduce(function(acc, current) {return acc + current;}, 0)*100)/100;
    Varianza = Math.round((temp/n) * 100)/100;
    VarianzaF = "\\frac{" + temp.toString() + "}{" + n.toString() + "} = " + Varianza.toString();
}

function GetDTipica() {
    let temp = Math.round(fi_XiDiffXAbsSq.reduce(function(acc, current) {return acc + current;}, 0)*100)/100;
    DTipica = Math.round(Math.sqrt(temp/n) * 100)/100;
    DTipicaF = "\\sqrt{\\frac{" + temp.toString() + "}{" + n.toString() + "}} = " + DTipica.toString();
}

function GetMomento1() {
    let temp = Xifi.reduce(function(acc, current) {return acc + current;}, 0);
    if (Momento1Limit == 0) {
        Momento1 = Math.round(((temp/n) * ic)*100)/100;
        Momento1F = "\\frac{" + temp.toString() + "}{" + n.toString() + "}*" + ic.toString() + " = " + Momento1.toString();
    } else {
        let temp2 = fi.slice(0, Momento1Limit).reduce((accumulator, currentValue) => accumulator + currentValue, 0);
        Momento1 = Math.round(((temp/temp2) * ic)*100)/100;
        Momento1F = "\\frac{" + temp.toString() + "}{" + temp2.toString() + "}*" + ic.toString() + " = " + Momento1.toString();
    }
    
}

function GetXiSq(limit) {
    for(let i = 0; i < limit; i++) {
        XiSq.push(Math.pow(Xi[i],2));
    }
}

function GetXiCube(limit) {
    for(let i = 0; i < limit; i++) {
        XiCube.push(Math.pow(Xi[i], 3));
    }
}

function Getfi_XiSq(limit) {
    GetXiSq(limit)
    for(let i = 0; i < limit; i++) {
        fi_XiSq.push(Math.round(fi[i] * XiSq[i] *100)/100);
    }
}

function Getfi_XiCube(limit) {
    GetXiCube(limit)
    for(let i = 0; i < limit; i++) {
        fi_XiCube.push(Math.round(fi[i] * XiCube[i] *100)/100);
    }
}

function GetMomento2() {
    Getfi_XiSq(Momento2Limit);
    let temp = fi_XiSq.reduce(function(acc, current) {return acc + current;}, 0);
    let temp2 = fi.slice(0, Momento2Limit).reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    Momento2 = Math.round(((temp/temp2)*Math.pow(ic,2))*100)/100;
    Momento2F = "\\frac{" + temp.toString() + "}{" + temp2.toString() + "}*" + Math.pow(ic,2) + " = " + Momento2.toString();
}

function GetMomento3() {
    Getfi_XiCube(Momento3Limit);
    let temp = fi_XiCube.reduce(function(acc, current) {return acc + current;}, 0);
    let temp2 = fi.slice(0, Momento3Limit).reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    Momento3 = Math.round(((temp/temp2)*Math.pow(ic,3))*100)/100;
    Momento3F = "\\frac{" + temp.toString() + "}{" + temp2.toString() + "}*" + Math.pow(ic,3) + " = " + Momento3.toString();
}

function GetDeltas() {
    let mayor =  fi.indexOf(Math.max(...fi));
    if (mayor == 0) {
        Delta1 = fi[mayor];
        Delta1F = fi[mayor].toString() + "- 0 = " + Delta1.toString();
    } else {
        Delta1 = fi[mayor] - fi[mayor-1];
        Delta1F = fi[mayor].toString() + "-" + fi[mayor-1].toString() + " = " + Delta1.toString();
    }

    if (mayor == fi.length) {
        Delta2 = fi[mayor]
        Delta2F = fi[mayor].toString() + "- 0 = " + Delta2.toString();

    } else {
        Delta2 = fi[mayor] - fi[mayor+1];
        Delta2F = fi[mayor].toString() + "-" + fi[mayor+1].toString() + " = " + Delta2.toString();
    }
}

function GetMo() {
    Mo = Math.round((Li + (Delta1/(Delta1+Delta2))*ic)*100)/100;
    MoF = Li.toString() + "+(" + Delta1.toString() + "/" + Delta1.toString() + "+" + Delta2.toString() + ")*" + ic.toString() + " = " + Mo.toString(); 
}

function GetSesgo() {
    Sesgo = Math.round(((X - Mo)/Varianza)*1000)/1000;
    SesgoF = "\\frac{" + X.toString() + "-" + Mo.toString() + "}{" + Varianza.toString() + "} = " + Sesgo.toString()
}

function Start(arr, Mom1, Mom2, Mom3) {
    if(arr === undefined || Mom1 ==undefined || Mom2 == undefined || Mom3  == undefined) {
        return "datos invalidos";
    }
    valores = arr;
    Momento1Limit = Mom1;
    Momento2Limit = Mom2;
    Momento3Limit = Mom3;
    Ordenar();
    GetNumeroElementos();
    GetRango();
    GetClase();
    GetIndiceClase();
    GetSinRepetir();
    GetClases();
    GetXi();
    Getfi();
    GetFi();
    GetXifi();
    GetMedia();
    GetXiDiffXAbs();
    Getfi_XiDiffXAbs();
    GetMe();
    GetXiDiffMeAbs();
    Getfi_XiDiffMeAbs();
    GetDx();
    GetDMe();
    GetXiDiffXAbsSq();
    Getfi_XiDiffXAbsSq();
    GetVarianza();
    GetDTipica();
    GetMomento1();
    GetMomento2();
    GetMomento3();
    GetDeltas();
    GetMo();
    GetSesgo();
}