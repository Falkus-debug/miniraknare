def addition (a,b):
    return a + b

def subtraktion (a,b):
    return a-b

def multiplikation(a,b):
    return a*b

def division(a,b):
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        print("du kan inte dividera med 0. använd ett annat tal")
        return "ogiltig"

def upphöjt(a,b):
    return a**b

def heltalsdivision (a,b):
    return a//b


#--------- Huvudprogram ---------

val = ""
while val != "q":
    print(
        """
            Välkommen till miniräknaren!
            1. Addera           2. Subtrahera
            3. Multiplicera     4. Dividera
            5. Upphöjt          6. Heltalsdivision
            q. Avsluta
        """
        )
    val = input("välj ett av alternativen")

    if val == "1":
        tal1 = float((input("skriv in det första talet")))
        tal2 = float((input("skriv in det andra talet")))
        summa = addition(tal1,tal2)
        print(f"summan är {summa}")

    if val == "2":
        tal1 = float((input("skriv in det första talet")))
        tal2 = float((input("skriv in det andra talet")))
        differens = subtraktion(tal1,tal2)
        print(f"differensen är {differens}")

    if val == "3":
        tal1 = float((input("skriv in det första talet")))
        tal2 = float((input("skriv in det andra talet")))
        produkt = multiplikation(tal1,tal2)
        print(f"produkten är {produkt}")

    if val == "4":
        tal1 = float((input("skriv in det första talet")))
        tal2 = float((input("skriv in det andra talet")))
        kvot = division(tal1,tal2)
        print(f"kvoten är {kvot}")

    if val == "5":
        tal1 = float((input("skriv in det första talet")))
        tal2 = float((input("skriv in det andra talet")))
        potens = upphöjt(tal1,tal2)
        print(f"potensen är {potens}")

    if val == "6":
        tal1 = float((input("skriv in det första talet")))
        tal2 = float((input("skriv in det andra talet")))
        heltalskvot = heltalsdivision(tal1,tal2)
        print(f"heltalskvoten är {heltalskvot}")

    if val == 'q':
        print("programmet avslutas.......")
        break



  