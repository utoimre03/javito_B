class Auto:

    def __init__(self, nev: str, gyartdat: int):
        self.nev = nev
        self.gyartdat = gyartdat

    kocsi = []
    beFile = open("auto.txt", "r", encoding="UTF-8")
    beFile.readline()
    beFile.readlines()
    beFile.close()

def tabla():
    print("III/Tabla")
    print("\t")

def flotta():
    print("III/Flotta:")
    print("\tAutók száma: 7")

def ertekes():
    print("III/Értékes:")
    print("\tA legfiatalabb autó: Opel Corsa(2019))")
