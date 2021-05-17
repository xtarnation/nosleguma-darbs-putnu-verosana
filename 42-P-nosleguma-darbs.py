import json

with open("putnudati.json", "r", encoding = 'utf-8') as fails:
    dati = fails.read()

putnudati = json.loads(dati)

def izvelne():
    print("\nSveiciens, putnu vērotāj!\nKādu darbību veiksi?")
    print("1: parādīt visus dienasgrāmatas ierakstus")
    print("2: pievienot jaunu ierakstu")
    print("3: meklēt dienasgrāmatas ierakstu")
    print("4: saglabāt un beigt darbu")
    darbiba = input("\nIevadi skaitli!")
    if darbiba == "1":
        ieraksti()
    elif darbiba == "2":
        pievienot()
    elif darbiba == "3":
        meklesana()
    elif darbiba == "4":
        beigas()
    else:
        print("\nIzvēlies vienu no minētajiem skaitļiem!\n")
        izvelne()

def ieraksti():
    print("\nVisi ieraksti:\n")
    for putns in putnudati:
        for p in putns:
            print(f'{p}: {putns[p]}')
        print()
    izvelne()


def pievienot():
    putns = {}    
    nosaukumsLV = input("\nIevadi putna latvisko nosaukumu!")
    nosaukumsLAT = input("Ievadi putna latīnisko nosaukumu!") 
    datums = input("Ievadi novērojuma datumu!")
    laiks = input("Ievadi novērojuma laiku!")
    vieta = input("Ievadi novērojuma vietu!")
    piezimes = input("Ievadi novērojuma piezīmes!")

    putns["nosaukumsLV"] = nosaukumsLV
    putns["nosaukumsLAT"] = nosaukumsLAT
    putns["datums"] = datums
    putns["laiks"] = laiks
    putns["vieta"] = vieta
    putns["piezimes"] = piezimes

    putnudati.append(putns)
    print("\nNovērojums ir pievienots dienasgrāmatai\n")

    meklesana(nosaukumsLV)

    izvelne()


def meklesana(*args):
    if len(args)==0:
        nosaukums = input("\nIevadi putna latvisko nosaukumu!")
    else:
        nosaukums = args[0]
    nosaukums = nosaukums.capitalize()
    atrasts = False
    for p in putnudati:
        if nosaukums in p["nosaukumsLV"]:
            print("\nPutns ir atrasts\n")
            atrasts = True
            for putns in p:
                print(f"{putns}: {p[putns]}")
    if not atrasts:
        print("\nIeraksti par putnu nav atrasti\n")
    izvelne()


def beigas():
    dati = json.dumps(putnudati, ensure_ascii = False)
    with open("putnudati.json", "w", encoding = 'utf-8') as fails:
        fails.write(dati)
    print("\nIeraksti ir saglabāti dienasgrāmatā.\nUz tikšanos, putnu vērotāj!\n")


izvelne()