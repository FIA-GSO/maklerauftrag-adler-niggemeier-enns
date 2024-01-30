import math

def berechne_grundflaeche(laenge, breite):
    return laenge * breite

def main():
    print("Willkommen zum Raumgrundflächenberechner!")

    gesamtflaeche = 0

    while True:
        try:
            anzahl_raeume = int(input("Geben Sie die Anzahl der zu berechnenden Räume ein (oder 'exit' zum Beenden): "))
            if anzahl_raeume <= 0:
                print("Bitte geben Sie eine gültige positive Zahl ein.")
                continue
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

    for i in range(1, anzahl_raeume + 1):
        print(f"\nRaum {i}:")
        while True:
            try:
                laenge = float(input("Länge des Raumes (in Metern): "))
                breite = float(input("Breite des Raumes (in Metern): "))
                if laenge <= 0 or breite <= 0:
                    print("Bitte geben Sie gültige positive Werte ein.")
                    continue
                break
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

        grundflaeche = berechne_grundflaeche(laenge, breite)
        gesamtflaeche += grundflaeche
        print(f"Die Grundfläche des Raumes beträgt {grundflaeche} Quadratmeter.")

    print(f"\nDie Gesamtfläche aller Räume beträgt {gesamtflaeche} Quadratmeter.")
    print("\nVielen Dank für die Verwendung des Raumgrundflächenberechners!")

if __name__ == "__main__":
    main()

