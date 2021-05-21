import json

#saglabāto datu izmantošana katrai lietošanas reizei
with open("putnudati.json", "r", encoding = 'utf-8') as fails:
    dati = fails.read()

putnudati = json.loads(dati)
#datu nolasīšanas beigas

def izvelne():
    print("\nSveiciens, putnu vērotāj!\nKādu darbību veiksi?")
    print("1: parādīt visus dienasgrāmatas ierakstus")
    print("2: pievienot jaunu ierakstu")
    print("3: meklēt dienasgrāmatas ierakstu")
    print("4: saglabāt un beigt darbu")

    #sākas datu ievade
    darbiba = input("\nIevadi skaitli!")
    #beidzas datu ievade

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

    #visi dati tiek parādīti
    print("\nVisi ieraksti:\n")
    for putns in putnudati:
        for p in putns:
            print(f'{p}: {putns[p]}')
        print()
    #koda beigas

    izvelne()


def pievienot():
    putns = {} 

    #sākas datu ievade   
    nosaukumsLV = input("\nIevadi putna latvisko nosaukumu!")
    nosaukumsLAT = input("Ievadi putna latīnisko nosaukumu!") 
    datums = input("Ievadi novērojuma datumu!")
    laiks = input("Ievadi novērojuma laiku!")
    vieta = input("Ievadi novērojuma vietu!")
    piezimes = input("Ievadi novērojuma piezīmes!")
    #beidzas datu ievade

    #dati tiek saglabāti masīvā
    putns["nosaukumsLV"] = nosaukumsLV
    putns["nosaukumsLAT"] = nosaukumsLAT
    putns["datums"] = datums
    putns["laiks"] = laiks
    putns["vieta"] = vieta
    putns["piezimes"] = piezimes

    putnudati.append(putns)
    #beidzas datu saglabāšana

    print("\nNovērojums ir pievienots dienasgrāmatai\n")

    meklesana(nosaukumsLV)

    izvelne()


#meklētie dati tiek parādīti
def meklesana(*args):
    if len(args)==0:

        #sākas datu ievade
        nosaukums = input("\nIevadi putna latvisko nosaukumu!")
        #beidzas datu ievade

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
#koda beigas

    if not atrasts:
        print("\nIeraksti par putnu nav atrasti\n")
    izvelne()


def beigas():

    #dati tiek saglabāti JSON failā
    dati = json.dumps(putnudati, ensure_ascii = False)
    with open("putnudati.json", "w", encoding = 'utf-8') as fails:
        fails.write(dati)
    #saglabāšana beidzas

    print("\nIeraksti ir saglabāti dienasgrāmatā.\nUz tikšanos, putnu vērotāj!\n")


izvelne()