import random
from ascii import *
import os
import sys

def main():
    print "Sveiki atvyke i HANGMAN'a!"

    file_obj = open("zodziu_sarasas.txt", "r")

    praeitas_ilgis = 0
    for zodis in file_obj.readlines():
        ilgiausias_zodis = len(zodis[:-1])
        if praeitas_ilgis < ilgiausias_zodis:
            praeitas_ilgis = ilgiausias_zodis

    lygis = 0
    while not int(lygis) in range(2, praeitas_ilgis+1): #kol lygis nera mums tinkamas - leidziami while loopa
        try:
            lygis = int(raw_input("Ivesk lygi 2-{}   ".format(praeitas_ilgis)))
        except ValueError as e:
            print "ivesk skaiciu"

    gyvybes = 0
    while not int(gyvybes) in range(3, 7): #kol gyvybes nera mums tinkamos - leidziami while loopa
        gyvybes = input("pasirink kiek turesi gyvybiu: 3-6 ")  # choose a shift

    pak_img = 6 - gyvybes

    file_obj = open("zodziu_sarasas.txt", "r")  # galima kursoriu grazint i pradzia - google
    zodziu_sarasas = []

    for zodis in file_obj.readlines():
        zodzio_ilgis = len(zodis[:-1])
        if zodzio_ilgis <= lygis and zodzio_ilgis >= 2:
            zodziu_sarasas.append(zodis[:-1])  # pridedame zodi i sarasa

    zodis_atspek = random.choice(zodziu_sarasas).lower()
    pasleptas_zodis = "_" * (len(zodis_atspek))

    # PADARYTI WHILE CIKLA KURIS SPELIOJA IR ATIDENGIA RAIDES
    # PATIKRINTI AR SPETA RAIDE YRA ZODYJE
    # RASTI SPETOS RAIDES PADETI
    # ATIDENGTI RAIDE

    # for i in range(0, len(zodis)):

    # def kartoti():
    #     restart = raw_input("Would you like to restart this program?")
    #     if restart == "yes" or restart == "y":
    #         python = sys.executable
    #         os.execl(python, python, *sys.argv)
    #     if restart == "n" or restart == "no":
    #         print "Script terminating. Goodbye."
    #     pass

    zodis_neatspetas = True

    while zodis_neatspetas:

        print pasleptas_zodis
        print zodis_atspek

        if pasleptas_zodis == zodis_atspek:
            print "ZODIS ATSPETAS! :)"
            break

        if gyvybes == 0:
            print "TAVE PAKORE :("
            break

        spejimas = raw_input("Spek raide: ").lower()

        if spejimas in zodis_atspek:
            raides = list(zodis_atspek)
            for indexas, value in enumerate(raides):
                if value == spejimas:
                    pasleptas_zodis_list = list(pasleptas_zodis)
                    pasleptas_zodis_list[indexas] = spejimas
                    pasleptas_zodis = "".join(pasleptas_zodis_list)
                    print "atspejai raide! :)"
                    print pasleptas_zodis

        else:
            print "neteisingai :( bandyk dar kart..."
            gyvybes -= 1
            pak_img += 1
            print ("gyvybes: " + str(gyvybes))
            print HANGMANPICS[pak_img]



    while True:
        answer = raw_input('Kartoti? (y/n): ').lower()
        if answer in ('y', 'n'):
            if answer == 'y':
                main()

            else:
                print 'Ate'
            break

main()
