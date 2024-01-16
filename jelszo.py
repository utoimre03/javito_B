def belepes():
    print("Első feladat:")
    fnev = input("\tAdja meg a felhasználónevét! ")
    jszo = input("\tAdja meg a jelszavát! ")

    if fnev == "bori99" and jszo == "Szivecske<3":
        print("\tBelépés engedélyezve.")
    elif fnev == "Bagaméri" or jszo == "vanília fagylalt":
        print("\tBelépés megtagadva.")
    elif fnev == "bori99" or jszo == "hibásjelszó":
        print("\tBelépés megtagadva.")
    elif fnev == "hibásfelhasználó" or jszo == "Szivecske<3":
        print("\tBelépés megtagadva.")


    while not (fnev == "bori99" and jszo == "Szivecske<3"):
        print()
        print("Első feladat:")
        fnev = input("\tAdja meg a felhasználónevét! ")
        jszo = input("\tAdja meg a jelszavát! ")
        print("\tBelépés engedélyezve.")
