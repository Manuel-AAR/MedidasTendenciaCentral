import math

n = 0 #numero total de elementos
r = 0 #rango
c = 0 #clase
ic = 0 #indice de clase
Clases = []#
Xi = []#
XiSquare = []#
XiCube = []#
Li = 0.0#
fi = []#
Fi = []#
Xifi = []#
MediaAritmetica = 0.0#

Mediana = 0.0#
DesviacionMedia = 0.0#
DesviacionMediana = 0.0#
DesviacionTipica = 0.0#
Moda = 0.0#
Varianza = 0.0#
Momento1 = 0.0#
Momento2 = 0.0#
Momento3 = 0.0#
Delta1 = 0.0#
Delta2 = 0.0#
Sesgo = 0.0#

XiMenosMediaAbs = []#
XiMenosMediaAbsSquare = []#
fiporXiMenosMediaAritAbs = []#
fiporXiMenosMediaAbsSquare = []#
XiMenosMeAbs = []#
fiporXiMenosMeAbs = []#
fiporXiSquare = []#
fiporXiCube = []#

def Ordenar(valores):
    return sorted(valores)

def NumeroElementos(valores):
    global n
    n = len(valores)
    print(f"\t -> N = {n}")

def Rango(valores):
    Ls = max(valores)
    Li = min(valores)
    result = (Ls - Li) + 1
    global r
    print(f"\t -> RANGO: r = ({Ls}-{Li})+1 = {result}")
    r = result

def Clase():
    global c
    global n
    x = math.sqrt(n)
    c = round(x)
    print(f"\t -> CLASE: C = \u221A{n} = {x} = {c}")

def IndiceClase():
    global c
    global r
    global ic
    x = r/c
    ic = math.ceil(x)
    print(f"\t -> INDICE DE CLASE: Ic = {r}/{c} = {x} = {ic}")

def sinRepetir(valores):
    #print(f"SIN REPETIR = {list(set(valores))}")
    return list(set(valores))

def GetClases(valores, ic):
    global c
    result = []
    current = []
    x = 0
    for i in range(0, c):
        for j in range(0,ic):
            current.append(min(valores)+x)
            x += 1
        result.append(current)
        current = []
    return result
    
def GetXi(valores):
    result = []
    for subarray in valores:
        middle_value = sum(subarray) / len(subarray)
        result.append(middle_value)
    return result

def GetFrecuenciaAbsoluta(valoresSinRepetir, valores):
    result = []
    for subarray in valoresSinRepetir:
        frequency = sum(valores.count(value) for value in subarray)
        result.append(frequency)
    return result

def GetFrecuenciaAbsolutaAcumulada(valores):
    result = []
    cumulative_sum = 0
    for value in valores:
        cumulative_sum += value
        result.append(cumulative_sum)
    return result

def GetXifi():
    result = []
    for x in range(0,len(Xi)):
        result.append(Xi[x] * fi[x])
    return result

def GetMediaAritmetica():
    global MediaAritmetica
    MediaAritmetica = sum(Xifi)/n
    print(f"\t -> MEDIA ARITMETICA = {sum(Xifi)}/{n} = {MediaAritmetica}")

def XiMenosMediaAritmeticaAbs():
    global Xi
    global MediaAritmetica
    result = []
    for element in Xi:
        difference = abs(element - MediaAritmetica)
        result.append(round(difference,2))
    return result

def fiporXiMenosMediaAritmericaAbs():
    global fi
    global XiMenosMediaAbs
    result = []
    for x in range(0,len(fi)):
        result.append(round(fi[x] * XiMenosMediaAbs[x],2))
    return result

def GetMediana():
    global Clases
    global MediaAritmetica
    global Mediana
    global Fi
    global Li
    global ic
    for index, subarray in enumerate(Clases):
        subarray_min = min(subarray)
        subarray_max = max(subarray)
        if subarray_min < MediaAritmetica < subarray_max:
            Li = subarray_min - 0.5
            break
    Mediana = Li+((n/2 - Fi[index - 1])/fi[index])*ic
    print(f"\t -> MEDIANA = {Li}+(({n}/2 - {Fi[index - 1]})/{fi[index]})*{ic} = {Mediana}")

def XiMenosMedianaAbs():
    global Xi
    global Mediana
    result = []
    for element in Xi:
        difference = abs(element - Mediana)
        result.append(round(difference,2))
    return result

def fiporXiMenosMedianaAbs():
    global fi
    global XiMenosMeAbs
    result = []
    for x in range(0,len(fi)):
        result.append(round(fi[x] * XiMenosMeAbs[x],2))
    return result


def GetDesviacionMedia():
    global DesviacionMedia
    global fiporXiMenosMediaAritAbs
    global n
    DesviacionMedia = sum(fiporXiMenosMediaAritAbs)/n
    print(f"\t -> DESVIACION MEDIA = {sum(fiporXiMenosMediaAritAbs)}/{n} = {DesviacionMedia}")

def GetDesviacionMediana():
    global DesviacionMediana
    global fiporXiMenosMeAbs
    global n
    DesviacionMediana = sum(fiporXiMenosMeAbs)/n
    print(f"\t -> DESVIACION CON LA MEDIANA = {sum(fiporXiMenosMeAbs)}/{n} = {DesviacionMediana}")

def GetXiMenosMediaAbsSquare():
    global XiMenosMediaAbsSquare
    global XiMenosMediaAbs
    for element in XiMenosMediaAbs:
        XiMenosMediaAbsSquare.append(round(math.pow(element,2),2))
        
def GetXiSquare(x):
    global XiSquare
    global Xi
    for i in range(0,x):
        XiSquare.append(math.pow(Xi[i],2))
    #print(f"Xi\u00B2 = {XiSquare}")
        

def GetXiCube(x):
    global XiCube
    global Xi
    for i in range(0,x):
        XiCube.append(math.pow(Xi[i],3))
    #print(f"Xi\u00B3 = {XiCube}")

def GetfiporXiMenosMediaAbsSquare():
    global XiMenosMediaAbsSquare
    global fiporXiMenosMediaAbsSquare
    global fi
    for x in range(0,len(fi)):
        fiporXiMenosMediaAbsSquare.append(round(fi[x] * XiMenosMediaAbsSquare[x],2))
    #print(f"fi|Xi-x|\u00B2 = {fiporXiMenosMediaAbsSquare}")


def GetVarianza():
    global fiporXiMenosMediaAbsSquare
    global n
    global Varianza
    Varianza = round(sum(fiporXiMenosMediaAbsSquare)/n,2)
    print(f"\t -> VARIANZA = {round(sum(fiporXiMenosMediaAbsSquare),2)}/{n} = {Varianza}")

def GetDesviacionTipica():
    global fiporXiMenosMediaAbsSquare
    global n
    global DesviacionTipica
    DesviacionTipica = round(math.sqrt(sum(fiporXiMenosMediaAbsSquare)/n),2)
    print(f"\t -> DESVIACION TIPICA = \u221A{round(sum(fiporXiMenosMediaAbsSquare),2)}/{n} = {DesviacionTipica}")

def GetMomento1():
    global Xifi
    global n
    global ic
    global Momento1
    Momento1 = round((sum(Xifi)/n) * ic,2)
    print(f"\t -> MOMENTO 1 = ({sum(Xifi)}/{n})*{ic} = {Momento1}")

def GetfiporXiSquare(x):
    global fi
    global XiSquare
    global fiporXiSquare
    GetXiSquare(x)
    for x in range(0,x):
        fiporXiSquare.append(round(fi[x] * XiSquare[x],2))
    #print(f"fi Xi\u00B2 = {fiporXiSquare}")
        

def GetfiporXiCube(x):
    global fi
    global XiCube
    global fiporXiCube
    GetXiCube(x)
    for x in range(0,x):
        fiporXiCube.append(round(fi[x] * XiCube[x],2))
    #print(f"fi Xi\u00B3 = {fiporXiCube}")


def GetMomento2():
    global Clases
    global Momento2
    global fi
    global ic
    global fiporXiSquare
    while True:
        user_input = input(f"Momento 2 hasta: ")
        
        # Check if the input is a number
        if not user_input.isdigit():
            print("Entrada invalida.")
            continue

        number = int(user_input)

        # Check if the number is within the specified range
        if 1 <= number <= len(Clases):
            break
        else:
            print("numero es mayor que el numero de clases")
    GetfiporXiSquare(number)
    Momento2 = round((sum(fiporXiSquare)/sum(fi[:number]))*math.pow(ic, 2),2)
    print("")
    print(f"\t -> MOMENTO 2 = ({sum(fiporXiSquare)}/{sum(fi[:number])})*{math.pow(ic, 2)} = {Momento2}")

def GetMomento3():
    global Clases
    global Momento3
    global fi
    global ic
    global fiporXiCube
    while True:
        user_input = input(f"Momento 3 hasta: ")
        
        # Check if the input is a number
        if not user_input.isdigit():
            print("Entrada invalida.")
            continue

        number = int(user_input)

        # Check if the number is within the specified range
        if 1 <= number <= len(Clases):
            break
        else:
            print("numero es mayor que el numero de clases")
    GetfiporXiCube(number)
    Momento3 = round((sum(fiporXiCube)/sum(fi[:number]))*math.pow(ic, 3),2)
    print("")
    print(f"\t -> MOMENTO 2 = ({sum(fiporXiCube)}/{sum(fi[:number])})*{math.pow(ic, 3)} = {Momento3}")

def GetDeltas():
    global fi
    global Delta1
    global Delta2
    mayor = max(fi)
    mayor = fi.index(mayor)
    Delta1 = fi[mayor] - fi[mayor-1]
    Delta2 = fi[mayor] - fi[mayor+1]
    print(f"\t -> DELTA 1 = {fi[mayor]}-{fi[mayor-1]} = {Delta1}")
    print("")
    print(f"\t -> DELTA 2 = {fi[mayor]}-{fi[mayor+1]} = {Delta2}")

def GetModa():
    global Li
    global Delta1
    global Delta2
    global ic
    global Moda
    Moda = round(Li + (Delta1/(Delta1+Delta2))*ic,2)
    print(f"\t -> MODA = {Li} + ({Delta1}/{Delta1}+{Delta2})*{ic} = {Moda}")

def GetSesgo():
    global MediaAritmetica
    global Moda
    global Varianza
    global Sesgo
    Sesgo = (MediaAritmetica-Moda)/Varianza
    print(f"\t -> SESGO = ({MediaAritmetica}-{Moda})/{Varianza} = {Sesgo}")





print("/////////////////////////////////////////////")
print("Medidas de Tendencia central, Datos Agrupados")
print("/////////////////////////////////////////////")
print("")
#valores = [18,18,24,20,17,20,17,17,17,19,29,19,23,25,28,19,18,30,18,18,26,24,31,22,17,25,26,20,30,20,22,20,24,29,18,25,21,21,17,19]  # Define valores as an empty list
valores = [2,2,2,5,5,5,5,5,8,8,8,8,8,8,8,8,8,11,11,11,11,11,11,11,11,14,14,14,14,14,14,14,14,17,17,17,17,17,17,17]
#valores = [17,14,3,10,10,7,9,19,11,6,10,11,18,15,8,7,12,8,8,10,13,11,7,18,12,14,14,17,15,14,10,3,15,11,2,5,17,12,19,15]
#valores = []
# while True:  # Begin the loop
#     _input = input("Introduzca un valor (o 'y' para salir): ")  # Get user input

#     if _input == "y":  # If input is 'y', break the loop
#         break

#     if _input.isnumeric():  # If input is numeric, append it as a number to valores
#         valores.append(int(_input))
#     else:
#         print("El valor ingresado es invalido")  # If input is neither 'y' nor numeric, print "invalid input"

#
valores = Ordenar(valores)
NumeroElementos(valores)
Rango(valores)
print("")
Clase()
print("")
IndiceClase()
print("")
Clases = GetClases(sinRepetir(valores),ic)
#print(f"Clases = {Clases}")
Xi = GetXi(Clases)
#print(f"Xi = {Xi}")
fi = GetFrecuenciaAbsoluta(Clases,valores)
#print(f"fi = {fi}")
Fi = GetFrecuenciaAbsolutaAcumulada(fi)
#print(f"Fi = {Fi}")
Xifi = GetXifi()
#print(f"Xifi = {Xifi}")
GetMediaAritmetica()
print("")
XiMenosMediaAbs = XiMenosMediaAritmeticaAbs()
#print(f"|Xi-x| = {XiMenosMediaAbs}")
fiporXiMenosMediaAritAbs = fiporXiMenosMediaAritmericaAbs()
#print(f"fi|Xi-x| = {fiporXiMenosMediaAritAbs}")
GetMediana()
print("")
XiMenosMeAbs = XiMenosMedianaAbs()
#print(f"|Xi-Me| = {XiMenosMeAbs}")
fiporXiMenosMeAbs = fiporXiMenosMedianaAbs()
#print(f"fi|Xi-Me| = {fiporXiMenosMeAbs}")
GetDesviacionMedia()
print("")
GetDesviacionMediana()
print("")
GetXiMenosMediaAbsSquare()
print("")
#print(f"|Xi-x|\u00B2 = {XiMenosMediaAbsSquare}")
GetfiporXiMenosMediaAbsSquare()
GetVarianza()
print("")
GetDesviacionTipica()
print("")
GetMomento1()
print("")
GetMomento2()
print("")
GetMomento3()
print("")
GetDeltas()
print("")
GetModa()
print("")
GetSesgo()
print("")

print(f"/Clases\t/Xi\t/fi\t/Fi\t/Xifi\t/|Xi-x|\t/fi|Xi-x|\t/|Xi-Me|\t/fi|Xi-Me|\t/|Xi-x|\u00B2\t/fi|Xi-x|\u00B2\t/Xi\u00B2\t/fiXi\u00B2\t/Xi\u00B3\t/fiXi\u00B3")
for x in range(0, len(Clases)):
    print(f"/{min(Clases[x])}-{max(Clases[x])}\t/{Xi[x]}\t/{fi[x]}\t/{Fi[x]}\t/{Xifi[x]}\t/{XiMenosMediaAbs[x]}\t/{fiporXiMenosMediaAritAbs[x]}\t\t/{XiMenosMeAbs[x]}\t\t/{fiporXiMenosMeAbs[x]}\t\t/{XiMenosMediaAbsSquare[x]}\t\t/{fiporXiMenosMediaAbsSquare[x]}\t\t/{XiSquare[x] if x < len(XiSquare) else ''}\t/{fiporXiSquare[x] if x < len(fiporXiSquare) else ''}\t/{XiCube[x] if x < len(XiCube) else ''}\t/{fiporXiCube[x] if x < len(fiporXiCube) else ''}")    
print("")
print("")
print("")