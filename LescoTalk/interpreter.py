from prueba1 import *

def inter(lista):
    if isinstance(lista,list):
        ptk=alexico(lista,0,[]);
        if ptk[1]=="letra" and len(ptk)==2:
            letra=convl(ptk,'',0)
            if letra == "CH":
                printt(letra,0,"palabra")
            elif letra == "LL":
                printt(letra,0,"palabra")
            elif letra == "RR":
                printt(letra,0,"palabra")
            else:
                printt(letra,0,ptk[1])
        elif ptk[1]=="letra" and len(ptk)!=2:
            palabra=convl(ptk,'',0)
            if len(ptk)==6:
                pale=convl(ptk,'',0)
                if pale=="UCR":
                    printt(pale,0,"palabra")
                elif pale=="TEC":
                    printt(pale,0,"palabra")
                else:
                    flag2=False
                    for i in range(len(palabra)):
                        if flag2==True:
                            flag2=False
                            comp=palabra[i-1]+palabra[i]
                            printt(comp,0,"palabra")
                        elif palabra[i]=="C":
                            if i==len(ptk)/2:
                                if palabra[i+1]=="H":
                                    flag2=True
                            else:
                                printt(palabra,i,ptk[1])
                        else:
                            printt(palabra,i,ptk[1])
            else:
                flag=False
                for i in range(len(palabra)):
                    if flag==True:
                        flag=False
                        comp=palabra[i-1]+palabra[i]
                        printt(comp,0,"palabra")
                    elif palabra[i]=="C":
                        if i==len(ptk)/2:
                            if palabra[i+1]=="H":
                                flag=True
                        else:
                            printt(palabra,i,ptk[1])
                    else:
                        printt(palabra,i,ptk[1])
        elif ptk[1]=="palabra":
            Prpp=convp(ptk,'',0)
            printt(Prpp,0,ptk[1])
    else:
        return "error"

def printt(pal,l,q):
    if q=="letra":
        prueba(pal[l])
    elif q=="palabra":
        prueba(pal)
        
def alexico(lis,cont,lr):
    if  lis[cont]== 0:
        return lr
    elif lis[cont] >0 and lis[cont] <= 30:
        lr.append(str(lis[cont]))
        lr.append("letra")
        cont+=1
        return alexico(lis, cont, lr)
    elif lis[cont] > 30 and lis[cont] <= 44:
        lr.append(str(lis[cont]))
        lr.append("palabra")
        cont+=1
        return alexico(lis, cont, lr)
    elif lis[cont] > 44 and lis[cont] <= 70:
        lr.append(str(lis[cont]))
        lr.append("frase")
        cont+=1
        return alexico(lis, cont, lr)

def convl(lis,letra,cont):
    if cont== len(lis):
        return letra
    elif lis[cont] == "1":
        letra+= 'A'
        return convl(lis,letra,cont+2)
    elif lis[cont] == "2":
        letra+= 'B'
        return convl(lis,letra,cont+2)
    elif lis[cont] == "3":
        letra+= "C"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "4":
        letra+= "CH"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "5":
        letra+= "D"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "6":
        letra+= "E"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "7":
        letra+= "F"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "8":
        letra+= "G"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "9":
        letra+= "H"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "10":
        letra+= "I"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "11":
        letra+= "J"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "12":
        letra+= "K"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "13":
        letra+= "L"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "14":
        letra+= "LL"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "15":
        letra+= "M"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "16":
        letra+= "N"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "17":
        letra+= "Ñ"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "18":
        letra+= "O"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "19":
        letra+= "P"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "20":
        letra+= "Q"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "21":
        letra+= "R"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "22":
        letra+= "RR"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "23":
        letra+= "S"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "24":
        letra+= "T"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "25":
        letra+= "U"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "26":
        letra+= "V"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "27":
        letra+= "W"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "28":
        letra+= "X"
        return convl(lis,letra,cont+2)
    elif lis[cont] == "29":
        letra+= "Y"
        return convl(lis,letra,cont+2)
    elif lis[cont] == '30':
        letra+= "Z"
        return convl(lis,letra,cont+2)
    
def convp(lis,palabra,cont):
    if cont== len(lis):
        return palabra
    elif lis[cont] == "31":
        palabra+= 'San José '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "32":
        palabra+= 'Cartago '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "33":
        palabra+= 'Heredia '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "34":
        palabra+= 'Alajuela '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "35":
        palabra+= 'Guanacaste '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "36":
        palabra+= 'Puntarenas '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "37":
        palabra+= 'Limón '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "38":
        palabra+= 'Él '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "39":
        palabra+= 'Ella '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "40":
        palabra+= 'Ellos '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "41":
        palabra+= 'Ellas '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "42":
        palabra+= 'Nosotros '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "43":
        palabra+= 'Yo '
        return convp(lis,palabra,cont+2)
    elif lis[cont] == "44":
        palabra+= 'Tú '
        return convp(lis,palabra,cont+2)

inter([25,3,21,0])