def addition (a,b):
    return a + b

def subtraktion (a,b):
    return a-b

def multiplikation(a,b):
    return a*b

def division(a,b):
    try:
        resultat = a / b
        print(resultat)
    except ZeroDivisionError:
        print("du kan inte dividera med 0. använd ett annat tal")

def upphöjt(a,b):
    return a**b

def heltalsdivision (a,b):
    return a//b



while True:
    operator = input("välj ett räknesätt: + - * / ** //, eller q för att avsluta")

    if operator == "+":
        tal1 = float(int(input("skriv in det första talet")))
        tal2 = float(int(input("skriv in det andra talet")))
        summa = addition(tal1,tal2)
        print(summa)

    if operator == "-":
        tal1 = float(int(input("skriv in det första talet")))
        tal2 = float(int(input("skriv in det andra talet")))
        differens = subtraktion(tal1,tal2)
        print(differens)

    if operator == "*":
        tal1 = float(int(input("skriv in det första talet")))
        tal2 = float(int(input("skriv in det andra talet")))
        produkt = multiplikation(tal1,tal2)
        print(produkt)

    if operator == "/":
        tal1 = float(int(input("skriv in det första talet")))
        tal2 = float(int(input("skriv in det andra talet")))
        kvot = division(tal1,tal2)
        print(kvot)

    if operator == "**":
        tal1 = float(int(input("skriv in det första talet")))
        tal2 = float(int(input("skriv in det andra talet")))
        potens = upphöjt(tal1,tal2)
        print(potens)
    
    if operator == "//":
        tal1 = float(int(input("skriv in det första talet")))
        tal2 = float(int(input("skriv in det andra talet")))
        heltalskvot = heltalsdivision(tal1,tal2)
        print(heltalskvot)
    
    if operator == 'q':
        print("programmet avslutas.......")
        break



  